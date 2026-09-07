# Estratto CSS — 14-arma-outemail

Solo cio' che insegna qualcosa: variabili, movimenti, effetti, gradienti, curve,
caratteri e **i commenti dell'autore**. Il resto e' utility generata e non si legge.

Generato da `scripts/analizza_css.py`.

---

## `src/07-2bca9184-site.css` — 1243 KB

### Variabili — 1470

**Colore (333):**
```css
--course-item-nav-text-color: hsla(var(--white-hsl),1);
--tweak-blog-item-pagination-icon-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-summary-block-read-more-color-on-background: hsla(var(--accent-hsl),1);
--product-block-text-color-on-background: hsla(var(--accent-hsl),1);
--product-basic-item-add-ons-title-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-quote-block-source-color-on-background: hsla(var(--accent-hsl),1);
--paragraphSmallColor: hsla(var(--safeInverseAccent-hsl),1);
--list-section-simple-button-background-color: hsla(var(--safeInverseAccent-hsl),1);
--gradientHeaderBorderColor: hsla(var(--black-hsl),1);
--tweak-summary-block-header-text-color-on-background: hsla(var(--accent-hsl),1);
--solidHeaderDropShadowColor: hsla(var(--black-hsl),1);
--tweak-blog-alternating-side-by-side-list-read-more-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-summary-block-background-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-form-block-survey-title-color: hsla(var(--safeInverseAccent-hsl),1);
--list-section-carousel-card-description-color: hsla(var(--accent-hsl),1);
--scheduling-block-scheduler-background-color: hsla(var(--accent-hsl),1);
--image-block-card-inline-link-color: hsla(var(--safeInverseAccent-hsl),1);
--paragraphLargeColor: hsla(var(--safeInverseAccent-hsl),1);
--tweak-summary-block-primary-metadata-color-on-background: hsla(var(--accent-hsl),1);
--tweak-blog-item-comment-text-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-summary-block-read-more-color: hsla(var(--safeInverseAccent-hsl),1);
--list-section-banner-slideshow-card-description-link-color: hsla(var(--accent-hsl),1);
--image-block-stack-inline-link-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-menu-block-title-color: hsla(var(--safeInverseAccent-hsl),1);
--product-basic-item-discount-chip-text-color: hsla(var(--accent-hsl),1);
--list-section-carousel-card-button-text-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-paragraph-medium-color-on-background: hsla(var(--accent-hsl),1);
--portfolio-grid-overlay-title-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-accordion-block-icon-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-marquee-block-paragraph-color-on-background: hsla(var(--accent-hsl),1);
--tweak-product-quick-view-button-color: hsla(var(--black-hsl),1);
--product-detail-subscription-price-text-color: hsla(var(--safeInverseAccent-hsl),1);
--paragraphMediumColor: hsla(var(--safeInverseAccent-hsl),1);
--siteTitleColor: hsla(var(--safeInverseAccent-hsl),1);
--tweak-product-basic-item-title-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-quote-block-text-color-on-background: hsla(var(--accent-hsl),1);
--list-section-carousel-card-title-color: hsla(var(--accent-hsl),1);
--tweak-gallery-icon-color: hsla(var(--safeInverseAccent-hsl),1);
--stack-stroke-color: hsla(var(--black-hsl),1);
--image-block-overlap-image-title-bg-color: hsla(var(--accent-hsl),1);
--tweak-newsletter-block-title-color: hsla(var(--safeInverseAccent-hsl),1);
--image-block-collage-inline-link-color: hsla(var(--accent-hsl),1);
--tweak-newsletter-block-button-background-color-on-background: hsla(var(--accent-hsl),1);
--tweak-product-basic-item-breadcumb-nav-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-product-basic-item-description-color: hsla(var(--safeInverseAccent-hsl),1);
--tertiaryButtonBackgroundColor: hsla(var(--safeInverseAccent-hsl),1);
--tweak-video-item-pagination-title-color: hsla(var(--white-hsl),1);
--tweak-product-list-description-text-color: hsla(var(--safeInverseAccent-hsl),1);
--course-list-grid-layout-course-item-border-color: hsla(var(--darkAccent-hsl),1);
--portfolio-grid-basic-title-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-blog-alternating-side-by-side-list-title-color: hsla(var(--safeInverseAccent-hsl),1);
--menuOverlayNavigationLinkColor: hsla(var(--safeInverseAccent-hsl),1);
--product-detail-subscriptions-frequency-text-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-product-list-stroke-color: hsla(var(--darkAccent-hsl),1);
--tweak-quote-block-stroke-color: hsla(var(--darkAccent-hsl),1);
--tweak-portfolio-item-pagination-title-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-form-block-title-color-on-background: hsla(var(--accent-hsl),1);
--image-block-collage-image-overlay-color: hsla(var(--darkAccent-hsl),1);
--image-block-stack-image-button-text-color: hsla(var(--accent-hsl),1);
--tweak-text-block-stroke-color: hsla(var(--darkAccent-hsl),1);
--product-detail-subscriptions-button-text-color: hsla(var(--accent-hsl),1);
--tweak-paragraph-small-color-on-background: hsla(var(--accent-hsl),1);
--tweak-accordion-block-icon-color-on-background: hsla(var(--accent-hsl),1);
--announcement-bar-background-color: hsla(var(--safeInverseAccent-hsl),1);
--headingLinkColor: hsla(var(--safeInverseAccent-hsl),1);
--headerBorderColor: hsla(var(--black-hsl),1);
--course-item-nav-border-color: hsla(var(--white-hsl),.25);
--tweak-quote-block-background-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-summary-block-header-text-color: hsla(var(--safeInverseAccent-hsl),1);
--list-section-carousel-card-button-background-color: hsla(var(--accent-hsl),1);
--list-section-carousel-card-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-blog-masonry-list-read-more-color: hsla(var(--safeInverseAccent-hsl),1);
--course-list-grid-layout-course-item-background-color: hsla(var(--black-hsl),1);
--list-section-banner-slideshow-title-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-product-grid-text-below-list-category-nav-color: hsla(var(--safeInverseAccent-hsl),1);
--product-basic-item-restock-notification-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-accordion-block-background-color: hsla(var(--safeInverseAccent-hsl),1);
--tweak-menu-block-item-title-color: hsla(var(--safeInverseAccent-hsl),1);
--headingMediumColor: hsla(var(--safeInverseAccent-hsl),1);
--list-section-carousel-button-background-color: hsla(var(--safeInverseAccent-hsl),1);
```

**Misura, curva, tempo, carattere (1137):**
```css
--white-hsl: 0,0%,98%;
--lightAccent-hsl: 49,21%,90%;
--accent-hsl: 0,0%,66%;
--darkAccent-hsl: 217,100%,50%;
--black-hsl: 240,3%,11%;
--safeLightAccent-hsl: 0,0%,66%;
--safeDarkAccent-hsl: 240,3%,11%;
--safeInverseAccent-hsl: 240,3%,11%;
--safeInverseLightAccent-hsl: 240,3%,11%;
--tweak-form-block-field-input-color-on-background-a: 1;
--tweak-form-block-field-border-color-a: 1;
--tweak-form-block-field-input-color-a: 1;
--tweak-form-block-field-fill-color-a: 1;
--tweak-form-block-field-accent-color-on-background-a: 1;
--tweak-form-block-field-accent-color-a: 1;
--tweak-form-block-field-fill-color-on-background-a: 1;
--tweak-form-block-field-border-color-on-background-a: 1;
--base-font-size: 16px;
--heading-font-font-family: "plus-jakarta-sans-o8l9cc";
--heading-font-font-style: normal;
--heading-font-font-weight: 700;
--heading-font-text-transform: none;
--heading-font-letter-spacing: 0em;
--heading-font-line-height: 1.2em;
--body-font-font-family: "elza-8u3n84";
--body-font-font-style: normal;
--body-font-font-weight: 300;
--body-font-text-transform: none;
--body-font-letter-spacing: 0em;
--body-font-line-height: 1.8em;
--meta-font-font-family: "elza-8u3n84";
--meta-font-font-style: normal;
--meta-font-font-weight: 400;
--meta-font-text-transform: none;
--meta-font-letter-spacing: 0em;
--meta-font-line-height: 1.2em;
--heading-1-size: 3.8rem;
--heading-1-size-value: 3.8;
--heading-2-size: 3rem;
--heading-2-size-value: 3;
--heading-3-size: 2.4rem;
--heading-3-size-value: 2.4;
--heading-4-size: 1.5rem;
--heading-4-size-value: 1.5;
--large-text-size: 1.25rem;
--large-text-size-value: 1.25;
--normal-text-size: 1rem;
--normal-text-size-value: 1;
--small-text-size: .8rem;
--small-text-size-value: .8;
--normal-meta-size: 1rem;
--normal-meta-size-value: 1;
--course-list-chapter-item-chapter-name-font-font-family: var(--heading-font-font-family);
--course-list-chapter-item-chapter-name-font-font-style: var(--heading-font-font-style);
--course-list-chapter-item-chapter-name-font-font-weight: var(--heading-font-font-weight);
--course-list-chapter-item-chapter-name-font-text-transform: var(--heading-font-text-transform);
--course-list-chapter-item-chapter-name-font-letter-spacing: var(--heading-font-letter-spacing);
--course-list-chapter-item-chapter-name-font-line-height: var(--heading-font-line-height);
--course-list-chapter-item-chapter-name-font-font-size: 2rem;
--course-list-chapter-item-chapter-name-font-font-size-value: 2;
--course-item-name-font-font-family: var(--heading-font-font-family);
--course-item-name-font-font-style: var(--heading-font-font-style);
--course-item-name-font-font-weight: var(--heading-font-font-weight);
--course-item-name-font-text-transform: var(--heading-font-text-transform);
--course-item-name-font-letter-spacing: var(--heading-font-letter-spacing);
--course-item-name-font-line-height: var(--heading-font-line-height);
--course-item-name-font-font-size: 2rem;
--course-item-name-font-font-size-value: 2;
--product-list-result-count-font-font-family: var(--body-font-font-family);
--product-list-result-count-font-font-style: var(--body-font-font-style);
--product-list-result-count-font-font-weight: var(--body-font-font-weight);
--product-list-result-count-font-text-transform: var(--body-font-text-transform);
--product-list-result-count-font-letter-spacing: var(--body-font-letter-spacing);
--product-list-result-count-font-line-height: var(--body-font-line-height);
--product-list-result-count-font-font-size: var(--normal-text-size);
--product-list-result-count-font-font-size-value: var(--normal-text-size-value);
--events-item-pagination-date-font-font-family: var(--meta-font-font-family);
--events-item-pagination-date-font-font-style: var(--meta-font-font-style);
--events-item-pagination-date-font-font-weight: var(--meta-font-font-weight);
--events-item-pagination-date-font-text-transform: var(--meta-font-text-transform);
```

### Movimenti — 33 @keyframes

```css
@keyframes bounceIn {0%{opacity:0;transform:scale(.3)}50%{opacity:1;transform:scale(1.05)}70%{transform:scale(.9)}100%{transform:scale(1)}}
@keyframes bounceOut {0%{transform:scale(1)}25%{transform:scale(.95)}50%{opacity:1;transform:scale(1.1)}100%{opacity:0;transform:scale(.3)}}
@keyframes sqs-spin {0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
@keyframes show-confirmation {from{opacity:0;transform:scale(.96)}to{opacity:1;transform:scale(1)}}
@keyframes show-confirmation-mobile {from{transform:translatey(-50%)}to{transform:translatey(0)}}
@keyframes bounceIn {0%{opacity:0;transform:scale(.3)}50%{opacity:1;transform:scale(1.05)}70%{transform:scale(.9)}100%{transform:scale(1)}}
@keyframes bounceOut {0%{transform:scale(1)}25%{transform:scale(.95)}50%{opacity:1;transform:scale(1.1)}100%{opacity:0;transform:scale(.3)}}
@keyframes loading-indicator-rotate-spinner {100%{transform:rotate(360deg)}}
@keyframes loading-indicator-dash {0%{stroke-dasharray:1,200;stroke-dashoffset:0}50%{stroke-dasharray:89,200;stroke-dashoffset:-35}100%{stroke-dasharray:89,200;stroke-dashoffset:-124}}
@keyframes underlineSlideOut {from{background-position:0% bottom,100% bottom}to{background-position:200% bottom,300% bottom}}
@keyframes underlineSlideIn {from{background-position:-200% bottom,-100% bottom}to{background-position:0% bottom,100% bottom}}
@keyframes tmpl-anim-fade-up {from,to{animation-timing-function:cubic-bezier(.4,0,.2,1);transform-origin:center center}from{opacity:0;transform:matrix(1,0,0,1,0,25)}to{opacity:1;transform:matrix(1,0,0,1,0,0)}}
@keyframes tmpl-anim-fade-scale-up {from,to{animation-timing-function:cubic-bezier(.4,0,.2,1);transform-origin:center center}from{opacity:0;transform:matrix(.92,0,0,.92,0,0)}to{opacity:1;transform:matrix(1,0,0,1,0,0)}}
@keyframes tmpl-anim-fade-stretch-up {from,to{animation-timing-function:cubic-bezier(.4,0,.2,1);transform-origin:center 0}from{opacity:0;transform:matrix(.9,0,0,1.3,0,25)}to{opacity:1;transform:matrix(1,0,0,1,0,0)}}
@keyframes tmpl-anim-clip-vertical-up {from,to{animation-timing-function:cubic-bezier(.4,0,.2,1)}from{-webkit-clip-path:polygon(50% 0%,100% 0%,100% 0%,50% 0%,50% 100%,0% 100%,0% 100%,50% 100%,50% 100%,50% 100%);clip-path:polygon(50% 0%,100% 0%,100% 0%,50% 0%,50% 100%,0% 100%,0% 100%,50% 100%,50% 100%,50% 100%)}to{-webkit-clip-path:polygon(50% 0%,100% 0%,100% 100%,50% 100%,50% 100%,0% 100%,0% 0%,50% 0%,50% 100%,50% 100%);clip-path:polygon(50% 0%,100% 0%,1
@keyframes tmpl-anim-clip-horizontal-left {from,to{animation-timing-function:cubic-bezier(.4,0,.2,1)}from{-webkit-clip-path:polygon(0% 50%,0% 100%,0% 100%,0% 50%,100% 50%,100% 0%,100% 0%,100% 50%,100% 50%,100% 50%);clip-path:polygon(0% 50%,0% 100%,0% 100%,0% 50%,100% 50%,100% 0%,100% 0%,100% 50%,100% 50%,100% 50%)}to{-webkit-clip-path:polygon(0% 50%,0% 100%,100% 100%,100% 50%,100% 50%,100% 0%,0% 0%,0% 50%,100% 50%,100% 50%);clip-path:polygon(0% 50%,0% 100%,1
@keyframes portfolio-index-background-image-mask--mask-down-in {from{transform:translate3d(0,-100%,0)}to{transform:translate3d(0,0,0)}}
@keyframes portfolio-index-background-image-mask--mask-down-out {from{transform:translate3d(0,0,0)}to{transform:translate3d(0,100%,0)}}
@keyframes portfolio-index-background-image-mask--mask-up-in {from{transform:translate3d(0,100%,0)}to{transform:translate3d(0,0,0)}}
@keyframes portfolio-index-background-image-mask--mask-up-out {from{transform:translate3d(0,0,0)}to{transform:translate3d(0,-100%,0)}}
@keyframes portfolio-index-background-image-mask--mask-left-in {from{transform:translate3d(-100%,0,0)}to{transform:translate3d(0,0,0)}}
@keyframes portfolio-index-background-image-mask--mask-left-out {from{transform:translate3d(0,0,0)}to{transform:translate3d(100%,0,0)}}
@keyframes portfolio-index-background-image-mask--mask-right-in {from{transform:translate3d(100%,0,0)}to{transform:translate3d(0,0,0)}}
@keyframes portfolio-index-background-image-mask--mask-right-out {from{transform:translate3d(0,0,0)}to{transform:translate3d(-100%,0,0)}}
@keyframes no-image-fade-in {from{opacity:0;transform:translatey(-15px)}to{opacity:1;transform:translatey(0)}}
@keyframes lightbox-open {from{opacity:0}to{opacity:1}}
```

### filtri — 9 valori distinti
```
alpha(opacity=70)
blur(15px)
blur(1px)
blur(1px) brightness(.3)
blur(20px)
blur(2px) brightness(.3)
blur(4px) brightness(.3)
blur(6px)
drop-shadow(2px 2px 1px rgba(0,0,0,.3))
```

### blend — 2 valori distinti
```
hard-light
var(--blend)
```

### clip/mask — 16 valori distinti
```
inset(0 0 50% 0)
inset(50% 0 0 0)
linear-gradient(to right,transparent 0%,#000 15%,#000 85%,transparent 100%)
polygon(0 0,100% 0,100% 100%,0% 100%)
polygon(0% 0%,0% 0%,0% 100%,0% 100%)
polygon(0% 0%,100% 0%,100% 100%,0% 100%)
polygon(0% 0,0 0%,-50% 100%,0% 100%)
polygon(0% 0,0 0%,0% 100%,0% 100%)
polygon(0% 100%,100% 100%,100% 100%,0% 100%)
polygon(0% 50%,0% 100%,0% 100%,0% 50%,100% 50%,100% 0%,100% 0%,100% 50%,100% 50%,100% 50%)
polygon(0% 50%,0% 100%,100% 100%,100% 50%,100% 50%,100% 0%,0% 0%,0% 50%,100% 50%,100% 50%)
polygon(100% 0%,100% 0%,100% 100%,100% 100%)
polygon(100% 0,100% 0,100% 100%,100% 100%)
polygon(100% 0,100% 0,100% 100%,150% 100%)
polygon(50% 0%,100% 0%,100% 0%,50% 0%,50% 100%,0% 100%,0% 100%,50% 100%,50% 100%,50% 100%)
polygon(50% 0%,100% 0%,100% 100%,50% 100%,50% 100%,0% 100%,0% 0%,50% 0%,50% 100%,50% 100%)
```

### ombre-testo — 1 valori distinti
```
0 0 4px rgba(0,0,0,.8)
```

### prospettiva — 1 valori distinti
```
hidden
```

### Gradienti non banali — 13
```css
linear-gradient(-45deg,rgba(35,40,47,.6) 25%,transparent 25%,transparent 50%,rgba(35,40,47,.6)
linear-gradient(0deg,rgba(0,0,0,.9) 0%,rgba(0,0,0,.4) 33%,rgba(0,0,0,0)
linear-gradient(0deg,rgba(0,0,0,.9),rgba(0,0,0,.4) 50%,rgba(0,0,0,0)
linear-gradient(180deg,rgba(0,0,0,.15) 0%,rgba(0,0,0,0) 100%)
linear-gradient(currentColor,currentColor),linear-gradient(currentColor,currentColor)
linear-gradient(to bottom,rgba(0,0,0,0) 0%,rgba(30,30,30,.3)
linear-gradient(to right,currentColor 100%,currentColor 0)
linear-gradient(to right,currentColor var(--value,0%),transparent var(--value,0%)
linear-gradient(to right,transparent 0%,#000 15%,#000 85%,transparent 100%)
linear-gradient(var(--backgroundOverlayColor),150px,transparent)
linear-gradient(var(--gradientHeaderBackgroundColor), transparent)
radial-gradient(circle at 50% 25%,rgba(0,0,0,.75),#000)}.sqs-lightbox-overlay.light{background:rgba(246,246,246,.98)
radial-gradient(circle at 50% 25%,rgba(255,255,255,.96),#fff)
```

### Curve — 7
```
cubic-bezier(.19,1,.22,1)
cubic-bezier(.2,.6,.3,1)
cubic-bezier(.25,.46,.45,.94)
cubic-bezier(.25,1,.6,1)
cubic-bezier(.33,1,.68,1)
cubic-bezier(.4,0,.2,1)
cubic-bezier(0,0,.2,1)
```

### @font-face — 3
```css
@font-face { font-family:'squarespace-ui-font';src:url(/assets/mirror/asset/d4cb48f1-squarespace-ui-font.eot);src:url(/assets/mirror/asset/fba0e315-squarespace-ui-font.eot) format('embedded-opentype'),url(/assets/mirror/asset/f3a35a01-squarespace-ui-font.svg) format('svg') }
@font-face { font-family:'squarespace-ui-font';src:url(/assets/mirror/asset/d4cb48f1-squarespace-ui-font.eot);src:url(/assets/mirror/asset/fba0e315-squarespace-ui-font.eot) format('embedded-opentype'),url(/assets/mirror/asset/f3a35a01-squarespace-ui-font.svg) format('svg') }
@font-face { font-family:'social-icon-font';src:url(/assets/mirror/asset/c46567b5-social-icon-font.eot);src:url(/assets/mirror/asset/c2119f0b-social-icon-font.eot) format('embedded-opentype'),url(/assets/mirror/asset/c882fd5d-social-icon-font.woff) format('woff'),url(/asse }
```

### Commenti dell'autore — 1 (**lo strato 4**)

- fonte: https://armageddon.bsns.it/assets/mirror/2bca9184-site.css

---

## `src/19-d59d72b2-static.css` — 470 KB

### Movimenti — 27 @keyframes

```css
@keyframes animation-form-field-fx-highlight-trace {0%{left:50%;transform:translate3d(-50%,-50%,0) scaleY(1) scaleX(3) rotate(0deg)}25%{left:min(50%,2.5em);transform:translate3d(-50%,-50%,0) scaleY(1.5) scaleX(1) rotate(90deg)}50%{transform:translate3d(-50%,-50%,0) scaleY(1) scaleX(3) rotate(180deg)}75%{left:calc(100% - min(2.5em,50%));transform:translate3d(-50%,-50%,0) scaleY(1.5) scaleX(1) rotate(270deg)}to{left:50%;transform:translate3d(-50%,-50%,0) scaleY(1) scal
@keyframes animation-form-field-fx-highlight-double-trace {0%{left:50%;transform:translate3d(-50%,-50%,0) scaleY(1) scaleX(3) rotate(0deg)}25%{left:min(50%,2.5em);transform:translate3d(-50%,-50%,0) scaleY(1.5) scaleX(1) rotate(90deg)}50%{transform:translate3d(-50%,-50%,0) scaleY(1) scaleX(3) rotate(180deg)}75%{left:calc(100% - min(2.5em,50%));transform:translate3d(-50%,-50%,0) scaleY(1.5) scaleX(1) rotate(270deg)}to{left:50%;transform:translate3d(-50%,-50%,0) scaleY(1) scal
@keyframes animation-form-field-fx-highlight-trace-bottom {0%{left:calc(100% + 2.5em);transform:translate3d(-50%,-50%,0) scaleY(1) scaleX(3) rotate(0deg)}to{left:-2.5em;transform:translate3d(-50%,-50%,0) scaleY(1) scaleX(3) rotate(0deg)}}
@keyframes animation-form-field-fx-highlight-double-trace-bottom {0%{left:calc(100% + 2.5em);transform:translate3d(-50%,-50%,0) scaleY(1) scaleX(3) rotate(0deg)}to{left:-2.5em;transform:translate3d(-50%,-50%,0) scaleY(1) scaleX(3) rotate(0deg)}}
@keyframes animation-form-field-fx-highlight-glow {0%,to{opacity:.1}50%{opacity:1}}
@keyframes shake-three {0%,to{transform:translate3d(0,0,0)}16.666%,50%,83.333%{transform:translate3d(.333rem,0,0)}33.333%,66.666%{transform:translate3d(-.333rem,0,0)}}
@keyframes keyframes-spinner {0%{transform:rotate(0deg)}to{transform:rotate(360deg)}}
@keyframes keyframes-spinner-check {0%{transform:translate3d(-100%,0,0)}to{transform:translate3d(0,0,0)}}
@keyframes keyframes-circle {0%,to{animation-timing-function:cubic-bezier(.5,0,1,.5)}0%{transform:rotateY(0deg)}to{transform:rotateY(1440deg)}}
@keyframes keyframes-circle-check {0%{transform:translate3d(0,0,0)}to{transform:translate3d(100%,0,0)}}
@keyframes keyframes-check {0%{transform:translate3d(-100%,0,0)}to{transform:translate3d(0,0,0)}}
@keyframes keyframes-bar {0%{transform:translate3d(-200%,0,0)}to{transform:translate3d(100%,0,0)}}
@keyframes keyframes-ellipsis-grow {0%{transform:scale(0)}to{transform:scale(1)}}
@keyframes keyframes-ellipsis-shrink {0%{transform:scale(1)}to{transform:scale(0)}}
@keyframes keyframes-ellipsis-shift {0%{transform:translate(0,0)}to{transform:translate(calc(.35em*2),0)}}
@keyframes anim-form-post-submit {0%{opacity:0;transform:translate3d(0,.5rem,0)}to{opacity:1;transform:translate3d(0,0,0)}}
@keyframes hideContent {0%,99%{opacity:0}}
@keyframes clipAnimation {0%{-webkit-clip-path:polygon(0 0,10%0,0 100%,0 100%);clip-path:polygon(0 0,10%0,0 100%,0 100%)}to{-webkit-clip-path:polygon(0 0,100%0,100% 100%,0 100%);clip-path:polygon(0 0,100%0,100% 100%,0 100%)}}
@keyframes spin {0%{transform:rotate(0deg)}to{transform:rotate(360deg)}}
@keyframes loading-dot-2 {0%{opacity:0}25%{opacity:1}}
@keyframes loading-dot-3 {0%{opacity:0}50%{opacity:1}}
@keyframes cart-loader-spin {0%{transform:rotate(0deg)}to{transform:rotate(360deg)}}
@keyframes gallery-image-enter-from-right {0%{transform:translateX(101%)}to{transform:translateX(0)}}
@keyframes gallery-image-exit-to-left {0%{transform:translateX(0)}to{transform:translateX(-101%)}}
@keyframes gallery-image-enter-from-left {0%{transform:translateX(-101%)}to{transform:translateX(0)}}
@keyframes gallery-image-exit-to-right {0%{transform:translateX(0)}to{transform:translateX(101%)}}
```

### clip/mask — 26 valori distinti
```
-100%0
0 0
100%
200% 100%
ellipse(0 100%at 0 0)
exclude
inset(50%)
linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0)
linear-gradient(90deg,transparent 0 50%,#fff 50%)
linear-gradient(to right,transparent 40%,var(--fx-highlight-input-color),transparent 60%)
polygon(-1%0,.1%0,-25% 100%,0 100%)
polygon(-2% -2%,102% -2%,102% 102%,-2% 102%)
polygon(-2% 102%,102% 102%,102% 102%,-2% 102%)
polygon(0 0,10%0,0 100%,0 100%)
polygon(0 0,100%0,100% 100%,0 100%)
polygon(0 0,101%0,101% 101%,0 101%)
polygon(0 100%,100% 100%,100% 100%,0 100%)
polygon(0 50%,0 100%,0 100%,0 50%,100% 50%,100%0,100%0,100% 50%,100% 50%,100% 50%)
polygon(0 50%,0 100%,100% 100%,100% 50%,100% 50%,100%0,0 0,0 50%,100% 50%,100% 50%)
polygon(0% calc(100% - var(--fx-highlight-input-border-width)),100% calc(100% - var(--fx-highlight-input-border-width)),100% 100%,0% 100%)
polygon(101%0,99.9%0,101% 100%,calc(100% + 25%) 100%)
polygon(50%0,100%0,100% 100%,50% 100%,50% 100%,0 100%,0 0,50%0,50% 100%,50% 100%)
```

### prospettiva — 2 valori distinti
```
80px
preserve-3d
```

### Gradienti non banali — 6
```css
conic-gradient(from .25turn,transparent,currentcolor 75%)
conic-gradient(from 0deg at 50% 50%,transparent 40%,var(--fx-highlight-input-color)
linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0)
linear-gradient(to bottom,rgba(255,255,255,0) 0%,var(--siteBackgroundColor)
linear-gradient(to right,transparent 40%,var(--fx-highlight-input-color)
radial-gradient(closest-side,transparent 0% calc(100% - var(--thickness)
```

### Curve — 9
```
cubic-bezier(.19,1,.22,1)
cubic-bezier(.25,.1,.25,1)
cubic-bezier(.37,0,.63,1)
cubic-bezier(.4,0,.2,1)
cubic-bezier(.5,0,1,.5)
cubic-bezier(.61,1,.88,1)
cubic-bezier(.66,0,.34,1)
cubic-bezier(0,.2,.8,1)
cubic-bezier(0.33, 1, 0.68, 1)
```

### Commenti dell'autore — 1 (**lo strato 4**)

- fonte: https://armageddon.bsns.it/assets/mirror/d59d72b2-static.css

---

## `src/23-player.css` — 232 KB

### Movimenti — 31 @keyframes

```css
@keyframes buffer {100%{transform:translateX(-10px)}}
@keyframes throb {0%,100%{background-color:#555}50%{background-color:#444}}
@keyframes wiggle {0%{transform:translateY(10px)}20%{transform:translateY(0)}40%,80%{transform:translateX(8px)}60%{transform:translateX(-8px)}100%{transform:translateX(0)}}
@keyframes pulse {50%{transform:scale(.9)}}
@keyframes dash {0%{stroke-dasharray:1,200;stroke-dashoffset:0}50%{stroke-dasharray:89,200;stroke-dashoffset:-35px}100%{stroke-dasharray:89,200;stroke-dashoffset:-135px}}
@keyframes rotate {100%{transform:rotate(360deg)}}
@keyframes scaleAnimation {0%{transform:scale(.9,.9)}100%{transform:scale(1,1)}}
@keyframes LikeButton_module_heartbeat__3908feee {0%{transform:scale(1)}10%{transform:scale(1)}20%{transform:scale(1.3)}30%{transform:scale(1.1)}40%{transform:scale(1.3)}100%{transform:scale(1)}}
@keyframes ShareButton_module_takeoff__26260904 {0%{transform:translate(0,0)}20%{transform:translate(-3px,3px)}40%{transform:translate(2px,-2px)}60%{transform:translate(-1px,1px)}80%{transform:translate(.5px,-.5px)}100%{transform:translate(0,0)}}
@keyframes EmbedButton_module_embedPop__dece8678 {0%{transform:scale(1)}40%{transform:scale(1.15)}100%{transform:scale(1)}}
@keyframes WatchLaterButton_module_pop__238c6c3b {0%{transform:scale(1)}10%{transform:scale(1.15)}100%{transform:scale(1)}}
@keyframes TinyProgressBar_module_buffer__c04d36b1 {100%{transform:translateX(-10px)}}
@keyframes ShareSheet_module_backdropFadeIn__5ab8a323 {from{opacity:0}to{opacity:1}}
@keyframes ShareSheet_module_backdropFadeOut__5ab8a323 {from{opacity:1}to{opacity:0}}
@keyframes ShareSheet_module_modalSlideIn__5ab8a323 {from{opacity:0;transform:translateY(12px) scale(.97)}to{opacity:1;transform:translateY(0) scale(1)}}
@keyframes ShareSheet_module_modalSlideOut__5ab8a323 {from{opacity:1;transform:translateY(0) scale(1)}to{opacity:0;transform:translateY(12px) scale(.97)}}
@keyframes AiCreditsEnrollmentModal_module_backdropFadeIn__6d3d95f8 {from{opacity:0}to{opacity:1}}
@keyframes AiCreditsEnrollmentModal_module_backdropFadeOut__6d3d95f8 {from{opacity:1}to{opacity:0}}
@keyframes AiCreditsEnrollmentModal_module_modalSlideIn__6d3d95f8 {from{opacity:0;transform:translateY(12px) scale(.97)}to{opacity:1;transform:translateY(0) scale(1)}}
@keyframes AiCreditsEnrollmentModal_module_modalSlideOut__6d3d95f8 {from{opacity:1;transform:translateY(0) scale(1)}to{opacity:0;transform:translateY(12px) scale(.97)}}
@keyframes OutroContentWrapper_module_fadeIn__06afa88b {0%{opacity:0}100%{opacity:1}}
@keyframes LinkOutro_module_slideDown__0f1c39e6 {to{transform:translate(0,0);opacity:1}}
@keyframes Spinner_module_buffer__795e5e53 {100%{transform:translateX(-10px)}}
@keyframes Spinner_module_throb__795e5e53 {0%,100%{background-color:#555}50%{background-color:#444}}
@keyframes Spinner_module_wiggle__795e5e53 {0%{transform:translateY(10px)}20%{transform:translateY(0)}40%,80%{transform:translateX(8px)}60%{transform:translateX(-8px)}100%{transform:translateX(0)}}
@keyframes Spinner_module_pulse__795e5e53 {50%{transform:scale(.9)}}
```

### filtri — 11 valori distinti
```
blur(10px)
blur(40px)
blur(8px)
brightness(.9) contrast(1.5) grayscale(0) hue-rotate(0) saturate(1) sepia(0)
brightness(0)
brightness(1) contrast(.9) grayscale(0) hue-rotate(0) saturate(1) sepia(.2)
brightness(1) contrast(1.1) grayscale(0) hue-rotate(0) saturate(1.1) sepia(0)
brightness(1) contrast(2) grayscale(0) hue-rotate(0) saturate(1) sepia(0)
brightness(1.1) contrast(1.1) grayscale(1) hue-rotate(0) saturate(1) sepia(0)
brightness(1.2) contrast(.9) grayscale(0) hue-rotate(-20deg) saturate(.85) sepia(0)
brightness(1.2) contrast(.9) grayscale(0) hue-rotate(0) saturate(1.1) sepia(0)
```

### blend — 4 valori distinti
```
darken
multiply
overlay
screen
```

### clip/mask — 3 valori distinti
```
inset(50%)
linear-gradient(to right,transparent 0%,#000 16px,#000 calc(100% - 16px),transparent 100%)
no-clip
```

### container — 1 valori distinti
```
scroll-state
```

### Gradienti non banali — 10
```css
linear-gradient(45deg,#414141 25%,transparent 25%),linear-gradient(-45deg,#414141 25%,transparent 25%)
linear-gradient(45deg,transparent 75%,#414141 75%),linear-gradient(-45deg,transparent 75%,#414141 75%)
linear-gradient(to right,rgba(66,10,14,.2),transparent),radial-gradient(circle,transparent,transparent)
linear-gradient(to right,transparent 0%,#000 16px,#000 calc(100% - 16px)
linear-gradient(to right,transparent,transparent),radial-gradient(circle at 40% 40%,rgba(255,255,255,.8)
linear-gradient(to right,transparent,transparent),radial-gradient(circle,#804e0f,#3b003b)
linear-gradient(to right,transparent,transparent),radial-gradient(circle,#a6b1ff 50%,#342134)
linear-gradient(to right,transparent,transparent),radial-gradient(circle,#d0ba8e 20%,#360309 85%,#1d0210 100%)
linear-gradient(to right,transparent,transparent),radial-gradient(circle,transparent,transparent)
radial-gradient(#82ffeb 0,#17d5ff 30%,#0ba1ff 45%,#9e00ff 75%,rgba(157,0,255,0)
```

### Curve — 9
```
cubic-bezier(.08, .82, .17, 1)
cubic-bezier(.17, .88, .32, 1.28)
cubic-bezier(.18, .89, .32, 1.2)
cubic-bezier(.18, 0, .07, 1)
cubic-bezier(.34,1.2,.64,1)
cubic-bezier(0.17,0,0.2,1)
cubic-bezier(0.18,0.89,0.32,1.2)
cubic-bezier(0.2,0.9,1,1)
cubic-bezier(0.5,0,0.83,1)
```

### Commenti dell'autore — 2 (**lo strato 4**)

- fonte: https://f.vimeocdn.com/p/4.46.106/css/player.css
- VimeoPlayer - v4.46.106 - 2026-09-04

---

## `src/16-aff6ea18-all.min.css` — 100 KB

### Variabili — 2

**Misura, curva, tempo, carattere (2):**
```css
--fa-style-family-brands: "Font Awesome 6 Brands";
--fa-style-family-classic: "Font Awesome 6 Free";
```

### Movimenti — 14 @keyframes

```css
@keyframes fa-beat {0%,90%{-webkit-transform:scale(1);transform:scale(1)}45%{-webkit-transform:scale(var(--fa-beat-scale,1.25));transform:scale(var(--fa-beat-scale,1.25))}}
@keyframes fa-beat {0%,90%{-webkit-transform:scale(1);transform:scale(1)}45%{-webkit-transform:scale(var(--fa-beat-scale,1.25));transform:scale(var(--fa-beat-scale,1.25))}}
@keyframes fa-bounce {0%{-webkit-transform:scale(1) translateY(0);transform:scale(1) translateY(0)}10%{-webkit-transform:scale(var(--fa-bounce-start-scale-x,1.1),var(--fa-bounce-start-scale-y,.9)) translateY(0);transform:scale(var(--fa-bounce-start-scale-x,1.1),var(--fa-bounce-start-scale-y,.9)) translateY(0)}30%{-webkit-transform:scale(var(--fa-bounce-jump-scale-x,.9),var(--fa-bounce-jump-scale-y,1.1)) translateY(var(--fa-bounce-height,
@keyframes fa-bounce {0%{-webkit-transform:scale(1) translateY(0);transform:scale(1) translateY(0)}10%{-webkit-transform:scale(var(--fa-bounce-start-scale-x,1.1),var(--fa-bounce-start-scale-y,.9)) translateY(0);transform:scale(var(--fa-bounce-start-scale-x,1.1),var(--fa-bounce-start-scale-y,.9)) translateY(0)}30%{-webkit-transform:scale(var(--fa-bounce-jump-scale-x,.9),var(--fa-bounce-jump-scale-y,1.1)) translateY(var(--fa-bounce-height,
@keyframes fa-fade {50%{opacity:var(--fa-fade-opacity,.4)}}
@keyframes fa-fade {50%{opacity:var(--fa-fade-opacity,.4)}}
@keyframes fa-beat-fade {0%,to{opacity:var(--fa-beat-fade-opacity,.4);-webkit-transform:scale(1);transform:scale(1)}50%{opacity:1;-webkit-transform:scale(var(--fa-beat-fade-scale,1.125));transform:scale(var(--fa-beat-fade-scale,1.125))}}
@keyframes fa-beat-fade {0%,to{opacity:var(--fa-beat-fade-opacity,.4);-webkit-transform:scale(1);transform:scale(1)}50%{opacity:1;-webkit-transform:scale(var(--fa-beat-fade-scale,1.125));transform:scale(var(--fa-beat-fade-scale,1.125))}}
@keyframes fa-flip {50%{-webkit-transform:rotate3d(var(--fa-flip-x,0),var(--fa-flip-y,1),var(--fa-flip-z,0),var(--fa-flip-angle,-180deg));transform:rotate3d(var(--fa-flip-x,0),var(--fa-flip-y,1),var(--fa-flip-z,0),var(--fa-flip-angle,-180deg))}}
@keyframes fa-flip {50%{-webkit-transform:rotate3d(var(--fa-flip-x,0),var(--fa-flip-y,1),var(--fa-flip-z,0),var(--fa-flip-angle,-180deg));transform:rotate3d(var(--fa-flip-x,0),var(--fa-flip-y,1),var(--fa-flip-z,0),var(--fa-flip-angle,-180deg))}}
@keyframes fa-shake {0%{-webkit-transform:rotate(-15deg);transform:rotate(-15deg)}4%{-webkit-transform:rotate(15deg);transform:rotate(15deg)}8%,24%{-webkit-transform:rotate(-18deg);transform:rotate(-18deg)}12%,28%{-webkit-transform:rotate(18deg);transform:rotate(18deg)}16%{-webkit-transform:rotate(-22deg);transform:rotate(-22deg)}20%{-webkit-transform:rotate(22deg);transform:rotate(22deg)}32%{-webkit-transform:rotate(-12deg);transform:r
@keyframes fa-shake {0%{-webkit-transform:rotate(-15deg);transform:rotate(-15deg)}4%{-webkit-transform:rotate(15deg);transform:rotate(15deg)}8%,24%{-webkit-transform:rotate(-18deg);transform:rotate(-18deg)}12%,28%{-webkit-transform:rotate(18deg);transform:rotate(18deg)}16%{-webkit-transform:rotate(-22deg);transform:rotate(-22deg)}20%{-webkit-transform:rotate(22deg);transform:rotate(22deg)}32%{-webkit-transform:rotate(-12deg);transform:r
@keyframes fa-spin {0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}to{-webkit-transform:rotate(1turn);transform:rotate(1turn)}}
@keyframes fa-spin {0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}to{-webkit-transform:rotate(1turn);transform:rotate(1turn)}}
```

### Curve — 2
```
cubic-bezier(.28,.84,.42,1)
cubic-bezier(.4,0,.6,1)
```

### @font-face — 10
```css
@font-face { font-family:"Font Awesome 6 Brands";font-style:normal;font-weight:400;font-display:block;src:url(/assets/mirror/asset/8490a865-fa-brands-400.woff2) format("woff2"),url(/assets/mirror/asset/c933d91e-fa-brands-400.ttf) format("truetype") }
@font-face { font-family:"Font Awesome 6 Free";font-style:normal;font-weight:400;font-display:block;src:url(/assets/mirror/asset/4632c063-fa-regular-400.woff2) format("woff2"),url(/assets/mirror/asset/3294bae1-fa-regular-400.ttf) format("truetype") }
@font-face { font-family:"Font Awesome 6 Free";font-style:normal;font-weight:900;font-display:block;src:url(/assets/mirror/asset/7fa6b210-fa-solid-900.woff2) format("woff2"),url(/assets/mirror/asset/45f5e302-fa-solid-900.ttf) format("truetype") }
@font-face { font-family:"Font Awesome 5 Brands";font-display:block;font-weight:400;src:url(/assets/mirror/asset/8490a865-fa-brands-400.woff2) format("woff2"),url(/assets/mirror/asset/c933d91e-fa-brands-400.ttf) format("truetype") }
@font-face { font-family:"Font Awesome 5 Free";font-display:block;font-weight:900;src:url(/assets/mirror/asset/7fa6b210-fa-solid-900.woff2) format("woff2"),url(/assets/mirror/asset/45f5e302-fa-solid-900.ttf) format("truetype") }
@font-face { font-family:"Font Awesome 5 Free";font-display:block;font-weight:400;src:url(/assets/mirror/asset/4632c063-fa-regular-400.woff2) format("woff2"),url(/assets/mirror/asset/3294bae1-fa-regular-400.ttf) format("truetype") }
@font-face { font-family:"FontAwesome";font-display:block;src:url(/assets/mirror/asset/7fa6b210-fa-solid-900.woff2) format("woff2"),url(/assets/mirror/asset/45f5e302-fa-solid-900.ttf) format("truetype") }
@font-face { font-family:"FontAwesome";font-display:block;src:url(/assets/mirror/asset/8490a865-fa-brands-400.woff2) format("woff2"),url(/assets/mirror/asset/c933d91e-fa-brands-400.ttf) format("truetype") }
@font-face { font-family:"FontAwesome";font-display:block;src:url(/assets/mirror/asset/4632c063-fa-regular-400.woff2) format("woff2"),url(/assets/mirror/asset/3294bae1-fa-regular-400.ttf) format("truetype");unicode-range:u+f003,u+f006,u+f014,u+f016-f017,u+f01a-f01b,u+f01d, }
@font-face { font-family:"FontAwesome";font-display:block;src:url(/assets/mirror/asset/225098f6-fa-v4compatibility.woff2) format("woff2"),url(/assets/mirror/asset/a722f60f-fa-v4compatibility.ttf) format("truetype");unicode-range:u+f041,u+f047,u+f065-f066,u+f07d-f07e,u+f080 }
```

### Commenti dell'autore — 1 (**lo strato 4**)

- fonte: https://armageddon.bsns.it/assets/mirror/aff6ea18-all.min.css

---

## `src/10-37b3991b-35ebb88013744865-min.it-IT.css` — 25 KB

### Variabili — 1

**Misura, curva, tempo, carattere (1):**
```css
--commerce-mini-cart-image-size: 60px;
```

### Movimenti — 10 @keyframes

```css
@keyframes commerce-mini-cart-slide-in-right {0%{opacity:0;-webkit-filter:blur(2px);filter:blur(2px);transform:translate(500px)scale(1)}to{opacity:1;-webkit-filter:blur();filter:blur();transform:translate(0)scale(1)}}
@keyframes commerce-mini-cart-slide-out-right {0%{opacity:1;-webkit-filter:blur();filter:blur();transform:translate(0)scale(1)}to{opacity:0;-webkit-filter:blur(4px);filter:blur(4px);transform:translate(500px)scale(1)}}
@keyframes commerce-mini-cart-slide-in-bottom {0%{opacity:0;-webkit-filter:blur(2px);filter:blur(2px);transform:translateY(200px)scale(1)}to{opacity:1;-webkit-filter:blur();filter:blur();transform:translateY(0)scale(1)}}
@keyframes commerce-mini-cart-slide-out-bottom {0%{opacity:1;-webkit-filter:blur();filter:blur();transform:translateY(0)scale(1)}to{opacity:0;-webkit-filter:blur(4px);filter:blur(4px);transform:translateY(200px)scale(1)}}
@keyframes commerce-mini-cart-overlay-fade {0%{opacity:.4}to{opacity:0}}
@keyframes spin {0%{transform:rotate(0)}to{transform:rotate(360deg)}}
@keyframes commerce-reserved-cart-slide-in-right {0%{opacity:0;-webkit-filter:blur(2px);filter:blur(2px);transform:translate(500px)scale(1)}to{opacity:1;-webkit-filter:blur();filter:blur();transform:translate(0)scale(1)}}
@keyframes commerce-reserved-cart-slide-out-right {0%{opacity:1;-webkit-filter:blur();filter:blur();transform:translate(0)scale(1)}to{opacity:0;-webkit-filter:blur(4px);filter:blur(4px);transform:translate(500px)scale(1)}}
@keyframes commerce-reserved-cart-slide-in-top {0%{opacity:0;-webkit-filter:blur(2px);filter:blur(2px);transform:translateY(-200px)scale(1)}to{opacity:1;-webkit-filter:blur();filter:blur();transform:translateY(0)scale(1)}}
@keyframes commerce-reserved-cart-slide-out-top {0%{opacity:1;-webkit-filter:blur();filter:blur();transform:translateY(0)scale(1)}to{opacity:0;-webkit-filter:blur(4px);filter:blur(4px);transform:translateY(-200px)scale(1)}}
```

### filtri — 3 valori distinti
```
blur()
blur(2px)
blur(4px)
```

### clip/mask — 2 valori distinti
```
contain
no-repeat
```

### Curve — 1
```
cubic-bezier(.23,1,.32,1)
```

### Commenti dell'autore — 1 (**lo strato 4**)

- fonte: https://armageddon.bsns.it/assets/mirror/37b3991b-35ebb88013744865-min.it-IT.css

---

## `src/27-css2.css` — 15 KB

### @font-face — 24
```css
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmS-HY6EQ.woff2) format('woff2'); unicode-range: U+0460-052F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F }
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmb-HY6EQ.woff2) format('woff2'); unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116; }
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xnj-HY6EQ.woff2) format('woff2'); unicode-range: U+0302-0303, U+0305, U+0307-0308, U+0310, U+0312, U+0315, U+031A, U+032 }
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xnx-HY6EQ.woff2) format('woff2'); unicode-range: U+0001-000C, U+000E-001F, U+007F-009F, U+20DD-20E0, U+20E2-20E4, U+2150 }
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmQ-HY6EQ.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF }
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmR-HY6EQ.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304 }
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmf-HY.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0 }
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 500; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmS-HY6EQ.woff2) format('woff2'); unicode-range: U+0460-052F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F }
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 500; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmb-HY6EQ.woff2) format('woff2'); unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116; }
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 500; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xnj-HY6EQ.woff2) format('woff2'); unicode-range: U+0302-0303, U+0305, U+0307-0308, U+0310, U+0312, U+0315, U+031A, U+032 }
```

### Commenti dell'autore — 11 (**lo strato 4**)

- fonte: https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600&family=Space+Grotesk:wght@600&display=swap
- cyrillic-ext */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmS-HY6EQ.woff2) format('woff2'); unicode-range: U+0460-052F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F; } /* cyrillic
- vietnamese */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmQ-HY6EQ.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; } /* latin-ext
- latin */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmf-HY.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; } /* cyrillic-ext
- cyrillic */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 500; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmb-HY6EQ.woff2) format('woff2'); unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116; } /* math
- vietnamese */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 500; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmQ-HY6EQ.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; } /* latin-ext
- latin */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 500; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmf-HY.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; } /* cyrillic-ext
- cyrillic */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 600; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmb-HY6EQ.woff2) format('woff2'); unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116; } /* math
- vietnamese */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 600; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmQ-HY6EQ.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; } /* latin-ext
- latin */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 600; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmf-HY.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; } /* vietnamese
- latin-ext */ @font-face { font-family: 'Space Grotesk'; font-style: normal; font-weight: 600; font-display: swap; src: url(https://fonts.gstatic.com/s/spacegrotesk/v22/V8mQoQDjQSkFtoMM3T6r8E7mF71Q-gOoraIAEj42VnsqPMBTTA.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0
