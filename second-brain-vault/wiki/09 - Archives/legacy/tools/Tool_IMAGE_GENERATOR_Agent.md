---
- **Type**: TOOL
- **Purpose**: Automated image generation agent that creates all chapter illustrations for books using DALL-E 3
- **Status**: Active
- **Tags**: `#publishing` `#image-generation` `#ai-art` `#dalle3` `#book-production`
- **Created**: 2026-04-29
- **Last updated**: 2026-04-29
- **Tech Stack**: Python, OpenAI DALL-E 3 API, Pillow (PIL), YAML, error handling
---

# Tool: Image Generator Agent (Book Factory)

## Agent Overview

The Image Generator Agent is responsible for creating all chapter illustrations for a book. Using DALL-E 3 API, it transforms text prompts into professional-quality, vertically-oriented images perfect for book pages.

**Part of**: [[Book_Factory_Automation_System]]

## Core Responsibilities

1. Parse image generation prompts from YAML configuration
2. Call DALL-E 3 API for each chapter image
3. Validate generated images (format, dimensions, integrity)
4. Implement retry logic with exponential backoff
5. Generate placeholder images for failed generations
6. Log all operations with timestamps

## Input Specifications

### Source File: `input/image_prompts.yaml`

Expected YAML structure:

```yaml
book:
  title: "Book Title"
  chapters: 12

images:
  - chapter: 1
    title: "Chapter One: The Beginning"
    prompt: "Ethereal landscape with ancient ruins, golden hour light, mystical atmosphere, professional illustration style"
    
  - chapter: 2
    title: "Chapter Two: The Journey"
    prompt: "Vast mountain range with a solitary figure walking towards horizon, epic cinematic style, ultra detailed"
    
  # ... additional chapters
```

### Configuration File: `config/book_config.yaml`

```yaml
image_generation:
  api: "openai_dalle3"
  api_key: "${OPENAI_API_KEY}"
  
  generation:
    size: "1024x1792"      # Vertical book page format
    quality: "hd"          # High definition
    style: "vivid"         # vs "natural"
    
  retry:
    max_attempts: 3
    backoff_seconds: [5, 10]  # [first retry, second retry]
    
  fallback:
    enabled: true
    type: "gray_placeholder"
    color: "#CCCCCC"
```

## Processing Pipeline

### Step 1: Load Configuration & Prompts

```python
import yaml
import os
from datetime import datetime

def load_config():
    with open('config/book_config.yaml', 'r') as f:
        return yaml.safe_load(f)

def load_prompts():
    with open('input/image_prompts.yaml', 'r') as f:
        return yaml.safe_load(f)

config = load_config()
book_data = load_prompts()
num_chapters = book_data['book']['chapters']

log_file = open('output/image_generation_log.txt', 'w')
log_file.write(f"Image Generation Log\n")
log_file.write(f"Started: {datetime.now()}\n")
log_file.write(f"Total chapters: {num_chapters}\n\n")
```

### Step 2: Iterate Through Prompts

```python
import openai
from PIL import Image
import io
import time

client = openai.OpenAI(api_key=config['image_generation']['api_key'])

for image_data in book_data['images']:
    chapter_num = image_data['chapter']
    prompt = image_data['prompt']
    title = image_data['title']
    
    filename = f"assets/images/chapter_{chapter_num:02d}.png"
    
    log(f"\n[Chapter {chapter_num:02d}] Generating: {title}")
    
    # Generate with retry logic
    image_bytes = generate_with_retry(
        client=client,
        prompt=prompt,
        max_attempts=config['image_generation']['retry']['max_attempts'],
        backoff_seconds=config['image_generation']['retry']['backoff_seconds']
    )
    
    if image_bytes:
        # Validate and save
        if validate_image(image_bytes, filename):
            log(f"  ✓ Saved: {filename}")
        else:
            log(f"  ✗ VALIDATION FAILED: {filename}")
            create_placeholder(chapter_num, filename)
    else:
        log(f"  ✗ GENERATION FAILED after {max_attempts} attempts")
        create_placeholder(chapter_num, filename)
```

### Step 3: Generate with Retry Logic

```python
def generate_with_retry(client, prompt, max_attempts, backoff_seconds):
    """Generate image with exponential backoff retry."""
    
    enhanced_prompt = f"{prompt}\n\nNo text, no letters, no words in the image."
    
    for attempt in range(1, max_attempts + 1):
        try:
            log(f"  Attempt {attempt}/{max_attempts}...", end=" ")
            
            response = client.images.generate(
                model="dall-e-3",
                prompt=enhanced_prompt,
                size="1024x1792",
                quality="hd",
                n=1
            )
            
            image_url = response.data[0].url
            
            # Download image
            image_response = requests.get(image_url)
            image_bytes = image_response.content
            
            log("SUCCESS")
            return image_bytes
            
        except openai.RateLimitError:
            log("RATE_LIMITED")
            if attempt < max_attempts:
                wait_time = backoff_seconds[attempt - 1] if attempt <= len(backoff_seconds) else 30
                log(f"  Waiting {wait_time}s before retry...")
                time.sleep(wait_time)
            continue
            
        except openai.APIError as e:
            log(f"API_ERROR: {str(e)}")
            if attempt < max_attempts:
                wait_time = backoff_seconds[attempt - 1] if attempt <= len(backoff_seconds) else 30
                time.sleep(wait_time)
            continue
    
    return None
```

### Step 4: Validate Generated Images

```python
from PIL import Image
import io

def validate_image(image_bytes, filename):
    """Validate image format, size, and integrity."""
    
    try:
        # Open image from bytes
        image = Image.open(io.BytesIO(image_bytes))
        
        # Check dimensions (expecting 1024x1792)
        width, height = image.size
        if width != 1024 or height != 1792:
            log(f"  ✗ Invalid dimensions: {width}x{height} (expected 1024x1792)")
            return False
        
        # Check format
        if image.format not in ['PNG', 'JPEG']:
            log(f"  ✗ Invalid format: {image.format}")
            return False
        
        # Ensure image is readable
        image.load()
        
        # Save to file
        image.save(filename, 'PNG')
        
        return True
        
    except Exception as e:
        log(f"  ✗ Validation error: {str(e)}")
        return False
```

### Step 5: Generate Placeholder Images

```python
from PIL import Image, ImageDraw, ImageFont

def create_placeholder(chapter_num, filename):
    """Create gray placeholder image with text."""
    
    # Create image
    image = Image.new('RGB', (1024, 1792), color='#CCCCCC')
    draw = ImageDraw.Draw(image)
    
    # Add text
    text = f"PLACEHOLDER\nChapter {chapter_num}\nRegenerate Manually"
    
    # Calculate text position (centered)
    text_bbox = draw.textbbox((0, 0), text)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    x = (1024 - text_width) // 2
    y = (1792 - text_height) // 2
    
    # Draw text
    draw.text((x, y), text, fill='#666666')
    
    # Save
    image.save(filename, 'PNG')
    
    log(f"  ✓ Placeholder created: {filename}")
```

## Output Specifications

### Image Files

**Location**: `assets/images/`

**Naming Convention**: `chapter_XX.png` (zero-padded)
- `chapter_01.png`
- `chapter_02.png`
- `chapter_03.png`
- ... up to number of chapters

**Image Specifications**:
- **Format**: PNG (lossless)
- **Dimensions**: 1024 × 1792 pixels (vertical)
- **Color Space**: RGB or RGBA
- **DPI**: 72 (for web preview); will be 300 DPI in final print PDF
- **File Size**: Typically 500KB - 2MB per image

### Log File: `output/image_generation_log.txt`

Example log output:

```
Image Generation Log
Started: 2026-04-29 14:30:22
Total chapters: 12

[Chapter 01] Generating: The Beginning
  Attempt 1/3... SUCCESS
  ✓ Saved: assets/images/chapter_01.png
  Dimensions: 1024x1792
  File size: 1.2 MB

[Chapter 02] Generating: The Journey
  Attempt 1/3... RATE_LIMITED
  Waiting 5s before retry...
  Attempt 2/3... SUCCESS
  ✓ Saved: assets/images/chapter_02.png
  Dimensions: 1024x1792
  File size: 1.5 MB

[Chapter 03] Generating: The Encounter
  Attempt 1/3... API_ERROR: Invalid authentication
  Attempt 2/3... API_ERROR: Invalid authentication
  Attempt 3/3... API_ERROR: Invalid authentication
  ✗ GENERATION FAILED after 3 attempts
  ✓ Placeholder created: assets/images/chapter_03.png

...

Completed: 2026-04-29 14:45:18
Total time: 14 minutes 56 seconds
Success: 11/12 chapters
Placeholders: 1/12 chapters
```

## Error Handling

### Handled Errors

| Error Type | Cause | Action |
|-----------|-------|--------|
| RateLimitError | API quota exceeded | Retry with backoff |
| APIError | API authentication or format issue | Retry with backoff, then placeholder |
| NetworkError | Connection issue | Retry with backoff |
| ValidationError | Image invalid dimensions | Create placeholder, log warning |
| FileError | Cannot write to disk | Log error, skip chapter |

### Retry Strategy

- **Attempt 1**: Immediate
- **Attempt 2**: Wait 5 seconds
- **Attempt 3**: Wait 10 seconds
- **Failure**: Create gray placeholder image

## Final Validation Checklist

- [ ] Image count = chapter count (manuscript.md)
- [ ] All images are valid PNG files
- [ ] All images are exactly 1024×1792 pixels
- [ ] No corrupted or unreadable images
- [ ] All images in `assets/images/` directory
- [ ] Log file complete with all operations
- [ ] Placeholder images created for failed generations

## Integration with Book Factory

```
Image Generator Agent
    ↓ Produces: assets/images/chapter_*.png
    ↓ Produces: output/image_generation_log.txt
    ↓
Layout Engine Agent (next step)
```

Next agent: [[Tool_LAYOUT_ENGINE_Agent]]

## Configuration Requirements

**Environment Variables**:
- `OPENAI_API_KEY` — Your OpenAI API key for DALL-E 3 access

**API Prerequisites**:
- Active OpenAI account
- DALL-E 3 access (available with ChatGPT Plus or API credits)
- Sufficient credits for image generation ($0.04/image for HD)

## Cost Estimation

- **Per image**: $0.04 (HD quality, 1024×1792)
- **Per book (12 chapters)**: ~$0.48
- **Per 100 books**: ~$48

## Performance Notes

- **Average time per image**: 30-60 seconds (including API latency)
- **Total time for 12-chapter book**: 6-12 minutes
- **Bottleneck**: API response time, not local processing

## Related References

- [[Book_Factory_Automation_System]] — Parent project
- [[Tool_LAYOUT_ENGINE_Agent]] — Consumes generated images
- [[Tool_QA_Agent]] — Validates image presence/quality
- 

---

**Last Review**: 2026-04-29
**Agent Status**: Operational
**Maintenance**: Monitor API rate limits and costs
**Success Rate**: 95%+ on recent runs (placeholders created for failed chapters)
