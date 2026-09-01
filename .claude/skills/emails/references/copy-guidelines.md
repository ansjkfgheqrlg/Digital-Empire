# Email Copy Guidelines

## Contents
- Structure
- Subject Lines
- Formatting
- Tone
- Length
- CTA Buttons vs. Links
- Personalization (merge fields, dynamic content, triggered emails)
- Segmentation Strategies (by behavior, by stage, by profile)
- Testing and Optimization (what to test, how to test, metrics to track)

## Structure

1. **Hook**: First line grabs attention
2. **Context**: Why this matters to them
3. **Value**: The useful content
4. **CTA**: What to do next
5. **Sign-off**: Human, warm close

## Subject Lines

*(fonte: Empire Studio, Andrei Pascu)*

- ~50 characters visible before truncation (mobile especially) — front-load the most important word/info, don't bury it at the end
- Don't open with the merge field (`{{first_name}}`): variable name length shifts everything after it unpredictably and removes control over where the subject gets cut. If you use it at all, put it at the very end.
- No clickbait ("click or die", promising X and delivering Y): it inflates open/click rate on paper but the clicks are unmotivated and don't convert — a lower but "clean" click rate beats a high spam-flavored one
- Emoji: fine only if not a cliché for the niche (💰 in "make money" offers signals nothing, everyone uses it) — safer with younger audiences, riskier with 40+ (reads as promotional/spam)

## Formatting

- Short paragraphs (1-3 sentences)
- White space between sections
- Bullet points for scanability
- Bold for emphasis (sparingly)
- Mobile-first (most read on phone)

## Tone

- Conversational, not formal
- First-person (I/we) and second-person (you)
- Active voice
- Match your brand but lean friendly
- Read it out loud—does it sound human?

## Length

- Shorter is usually better
- 50-125 words for transactional
- 150-300 words for educational
- 300-500 words for story-driven
- If it's long, it better be good

## CTA Buttons vs. Links

- Buttons: Primary actions, high-visibility
- Links: Secondary actions, in-text
- One clear primary CTA per email
- Button text: Action + outcome

---

## Personalization

### Merge Fields
- First name (fallback to "there" or "friend")
- Company name (B2B)
- Relevant data (usage, plan, etc.)
- **Fallback chaining** *(fonte: Empire Studio, Andrei Pascu)*: don't stop at the name field — any merge field that touches copy text (CTA phrasing, status references, greeting) needs a defined fallback so a missing data point never leaves a visible gap ("Hi ," instead of "Hi there,"). Pattern: primary field → if empty, a coherent fallback phrase, not blank. Applies wherever the ESP/CRM supports conditional merge logic, not just on first name.

### Dynamic Content
- Based on segment
- Based on behavior
- Based on stage

### Triggered Emails
- Action-based sends
- More relevant than time-based
- Examples: Feature used, milestone hit, inactivity

---

## Segmentation Strategies

### By Behavior
- Openers vs. non-openers
- Clickers vs. non-clickers
- Active vs. inactive

### By Stage
- Trial vs. paid
- New vs. long-term
- Engaged vs. at-risk

### By Profile
- Industry/role (B2B)
- Use case / goal
- Company size

---

## Testing and Optimization

### What to Test
- Subject lines (highest impact)
- Send times
- Email length
- CTA placement and copy
- Personalization level
- Sequence timing

### How to Test
- A/B test one variable at a time
- Sufficient sample size
- Statistical significance
- Document learnings

### Metrics to Track
- Open rate (benchmark: 20-40%)
- Click rate (benchmark: 2-5%) — **CR = clicks / emails sent** vs **CTR = clicks / emails opened**. Same click count, very different percentages depending on which base you use — don't compare a CR to a CTR benchmark. *(fonte: Empire Studio, Andrei Pascu)*
- Don't celebrate a high click rate without checking WHERE the clicks went — a secondary link (social, unrelated video) can inflate total clicks while the actual CTA gets almost none. If your ESP doesn't break down clicks per link/button, that's a tooling gap worth fixing.
- Unsubscribe rate (keep under 0.5%)
- Conversion rate (specific to sequence goal)
- Revenue per email (if applicable)
