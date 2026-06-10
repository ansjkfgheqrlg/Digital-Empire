/* ============================================
   CCM STRATEGIC CALL — Interactions v3.0
   Scroll Reveal (multi-variant), Accordion,
   Sticky CTA, Parallax, Count-Up
============================================ */

(function () {
  'use strict';

  /* ===========================
     1. SCROLL REVEAL (multi-variant)
  =========================== */
  function initScrollReveal() {
    var selectors = '.reveal, .reveal-left, .reveal-right, .reveal-scale, .reveal-fade';
    var els = document.querySelectorAll(selectors);
    if (!els.length) return;

    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('revealed');
            observer.unobserve(entry.target);
          }
        });
      }, {
        threshold: 0.08,
        rootMargin: '0px 0px -60px 0px'
      });

      els.forEach(function (el) { observer.observe(el); });
    } else {
      els.forEach(function (el) { el.classList.add('revealed'); });
    }
  }


  /* ===========================
     2. ACCORDION
  =========================== */
  function initAccordion() {
    var headers = document.querySelectorAll('.accordion-header');

    headers.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var item = this.closest('.accordion-item');
        var isActive = item.classList.contains('active');

        // Close all others
        document.querySelectorAll('.accordion-item.active').forEach(function (openItem) {
          if (openItem !== item) {
            openItem.classList.remove('active');
            var otherBtn = openItem.querySelector('.accordion-header');
            if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
          }
        });

        // Toggle current
        item.classList.toggle('active', !isActive);
        this.setAttribute('aria-expanded', String(!isActive));
      });

      // Keyboard accessibility
      btn.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          this.click();
        }
      });
    });
  }


  /* ===========================
     3. STICKY CTA BAR
  =========================== */
  function initStickyCTA() {
    var stickyBar = document.querySelector('.sticky-cta');
    if (!stickyBar) return;

    var triggerPoint = window.innerHeight * 0.6;
    var ticking = false;

    function updateSticky() {
      var scrollY = window.pageYOffset || document.documentElement.scrollTop;

      if (scrollY > triggerPoint) {
        stickyBar.classList.add('visible');
      } else {
        stickyBar.classList.remove('visible');
      }

      ticking = false;
    }

    window.addEventListener('scroll', function () {
      if (!ticking) {
        requestAnimationFrame(updateSticky);
        ticking = true;
      }
    }, { passive: true });
  }


  /* ===========================
     4. SMOOTH SCROLL for anchors
  =========================== */
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
      anchor.addEventListener('click', function (e) {
        var targetId = this.getAttribute('href');
        if (targetId === '#') return;

        var target = document.querySelector(targetId);
        if (target) {
          e.preventDefault();
          var offset = 80;
          var top = target.getBoundingClientRect().top + window.pageYOffset - offset;

          window.scrollTo({
            top: top,
            behavior: 'smooth'
          });
        }
      });
    });
  }


  /* ===========================
     5. COUNT-UP ANIMATION for stats
  =========================== */
  function initCountUp() {
    var statNums = document.querySelectorAll('.stat-num[data-target]');
    if (!statNums.length) return;

    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            animateCount(entry.target);
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.5 });

      statNums.forEach(function (el) { observer.observe(el); });
    }
  }

  function animateCount(el) {
    var target = el.getAttribute('data-target');
    var suffix = el.getAttribute('data-suffix') || '';
    var prefix = el.getAttribute('data-prefix') || '';
    var numTarget = parseFloat(target);
    var duration = 1800;
    var startTime = null;

    function step(timestamp) {
      if (!startTime) startTime = timestamp;
      var progress = Math.min((timestamp - startTime) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      var current = Math.round(eased * numTarget);

      el.textContent = prefix + current + suffix;

      if (progress < 1) {
        requestAnimationFrame(step);
      }
    }

    requestAnimationFrame(step);
  }


  /* ===========================
     6. HERO PARALLAX (subtle)
  =========================== */
  function initParallax() {
    var parallaxBg = document.querySelector('.hero-parallax-bg');
    if (!parallaxBg) return;

    // Respect reduced motion
    var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReduced) return;

    var ticking = false;

    function updateParallax() {
      var scrollY = window.pageYOffset || document.documentElement.scrollTop;
      // Subtle shift: move at 30% of scroll speed, cap effect to hero area
      var maxScroll = window.innerHeight * 1.5;
      if (scrollY < maxScroll) {
        var yOffset = scrollY * 0.3;
        parallaxBg.style.transform = 'translateY(' + yOffset + 'px)';
      }
      ticking = false;
    }

    window.addEventListener('scroll', function () {
      if (!ticking) {
        requestAnimationFrame(updateParallax);
        ticking = true;
      }
    }, { passive: true });
  }


  /* ===========================
     INIT
  =========================== */
  document.addEventListener('DOMContentLoaded', function () {
    initScrollReveal();
    initAccordion();
    initStickyCTA();
    initSmoothScroll();
    initCountUp();
    initParallax();
  });

})();
