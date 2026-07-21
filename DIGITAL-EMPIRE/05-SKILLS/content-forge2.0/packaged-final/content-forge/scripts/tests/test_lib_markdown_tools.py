"""Test per lib/markdown_tools.py."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from lib.markdown_tools import (
    extract_headings, extract_links, extract_wikilinks,
    build_toc, word_count, strip_code_blocks, strip_html_comments,
)


def test_extract_headings():
    text = "# Title\n## Section A\n### Sub A.1\n## Section B"
    headings = extract_headings(text)
    assert len(headings) == 4
    assert headings[0].level == 1
    assert headings[1].text == "Section A"
    assert headings[2].level == 3


def test_extract_headings_skip_code():
    text = "## Real heading\n```\n## Fake heading in code\n```\n## Another real"
    headings = extract_headings(text)
    assert len(headings) == 2


def test_explicit_anchor():
    text = "## Section {#custom-anchor}"
    headings = extract_headings(text)
    assert headings[0].anchor == "custom-anchor"


def test_extract_links():
    text = "Check [Google](https://google.com) and [GitHub](https://github.com)"
    links = extract_links(text)
    assert len(links) == 2
    assert links[0][0] == "Google"
    assert links[0][1] == "https://google.com"


def test_extract_wikilinks():
    text = "See [[concept-a]] and [[concept-b|the B]] and [[concept-c#section]]"
    wls = extract_wikilinks(text)
    assert len(wls) == 3
    assert wls[0]["target"] == "concept-a"
    assert wls[1]["alias"] == "the B"
    assert wls[2]["anchor"] == "section"


def test_word_count():
    text = "This is a test with seven words"
    assert word_count(text) == 7


def test_word_count_exclude_code():
    text = "Real words here\n```\ncode that should not count\n```"
    wc = word_count(text, exclude_code=True)
    assert wc == 3  # "Real words here"


def test_build_toc():
    text = "# Title\n## Section A\n### Sub\n## Section B"
    toc = build_toc(text, max_level=3)
    assert "Section A" in toc
    assert "Sub" in toc
    assert "Title" not in toc  # H1 escluso


def test_strip_html_comments():
    text = "Before <!-- comment --> after"
    assert "<!-- comment -->" not in strip_html_comments(text)
    assert "Before" in strip_html_comments(text)
