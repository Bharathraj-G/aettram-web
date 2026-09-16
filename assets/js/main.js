(function () {
  "use strict";

  document.documentElement.classList.add("page-fade");

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var finePointer = window.matchMedia("(pointer: fine)").matches;

  if (window.AOS) {
    AOS.init({
      duration: reduce ? 0 : 700,
      easing: "ease-out-cubic",
      once: true,
      offset: 80,
    });
  }

  if (window.Lenis && !reduce && !document.body.classList.contains("roi-page")) {
    var lenis = new Lenis({ lerp: 0.1 });
    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);
    if (window.gsap && window.ScrollTrigger) {
      gsap.registerPlugin(ScrollTrigger);
      lenis.on("scroll", ScrollTrigger.update);
    }
  } else if (window.gsap && window.ScrollTrigger) {
    gsap.registerPlugin(ScrollTrigger);
  }

  var header = document.querySelector(".site-header");
  function onScroll() {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 24);
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  var toggle = document.querySelector(".nav-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = document.body.classList.toggle("menu-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  document.querySelectorAll(".mobile-panel a").forEach(function (a) {
    a.addEventListener("click", function () {
      document.body.classList.remove("menu-open");
    });
  });

  if (window.Splitting && window.gsap && document.querySelector("[data-splitting]")) {
    Splitting();
    if (!reduce) {
      gsap.from("[data-splitting] .char", {
        y: 40,
        opacity: 0,
        duration: 0.7,
        stagger: 0.02,
        ease: "power3.out",
        delay: 0.15,
      });
    }
  }

  if (window.gsap && window.ScrollTrigger && !reduce) {
    gsap.utils.toArray("[data-hero-media]").forEach(function (el) {
      gsap.to(el, {
        yPercent: 12,
        ease: "none",
        scrollTrigger: { trigger: el.parentElement, start: "top top", end: "bottom top", scrub: true },
      });
    });

    gsap.utils.toArray(".card, .work-item, .pillar").forEach(function (el, i) {
      gsap.from(el, {
        y: 28,
        opacity: 0,
        duration: 0.7,
        delay: (i % 3) * 0.08,
        scrollTrigger: { trigger: el, start: "top 88%" },
      });
    });
  }

  document.querySelectorAll("[data-count]").forEach(function (el) {
    var target = parseInt(el.getAttribute("data-count"), 10);
    var started = false;
    function run() {
      if (started) return;
      started = true;
      var start = 0;
      var dur = 1200;
      var t0 = performance.now();
      function tick(now) {
        var p = Math.min(1, (now - t0) / dur);
        el.textContent = Math.round(start + (target - start) * p);
        if (p < 1) requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    }
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) run();
        });
      });
      io.observe(el);
    } else run();
  });

  if (window.Swiper) {
    document.querySelectorAll("[data-swiper]").forEach(function (root) {
      new Swiper(root, {
        slidesPerView: 1.15,
        spaceBetween: 16,
        grabCursor: true,
        breakpoints: {
          768: { slidesPerView: 2.2 },
          1024: { slidesPerView: 3.1 },
        },
      });
    });
    document.querySelectorAll("[data-logo-swiper]").forEach(function (root) {
      new Swiper(root, {
        slidesPerView: 2.4,
        spaceBetween: 24,
        loop: true,
        autoplay: reduce ? false : { delay: 2200 },
        breakpoints: { 768: { slidesPerView: 4 }, 1024: { slidesPerView: 6 } },
      });
    });
  }

  if (window.GLightbox) {
    GLightbox({ selector: ".glightbox", touchNavigation: true, loop: true });
  }

  var filterBtns = document.querySelectorAll(".filter-btn");
  var items = document.querySelectorAll(".work-item");
  filterBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      filterBtns.forEach(function (b) {
        b.classList.remove("is-active");
        b.setAttribute("aria-pressed", "false");
      });
      btn.classList.add("is-active");
      btn.setAttribute("aria-pressed", "true");
      var key = btn.getAttribute("data-filter");
      items.forEach(function (item) {
        var show = key === "all" || item.getAttribute("data-cat") === key;
        item.classList.toggle("is-hidden", !show);
      });
    });
  });

  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      var val = btn.getAttribute("data-copy");
      if (navigator.clipboard) navigator.clipboard.writeText(val);
      btn.classList.add("show-tip");
      setTimeout(function () {
        btn.classList.remove("show-tip");
      }, 1400);
      if (btn.tagName === "BUTTON") e.preventDefault();
    });
  });

  if (finePointer && !reduce) {
    document.body.classList.add("has-custom-cursor");
    var dot = document.createElement("div");
    var ring = document.createElement("div");
    dot.className = "cursor-dot";
    ring.className = "cursor-ring";
    document.body.appendChild(dot);
    document.body.appendChild(ring);
    var x = 0,
      y = 0,
      rx = 0,
      ry = 0;
    window.addEventListener(
      "mousemove",
      function (e) {
        x = e.clientX;
        y = e.clientY;
        dot.style.left = x + "px";
        dot.style.top = y + "px";
      },
      { passive: true }
    );
    function follow() {
      rx += (x - rx) * 0.18;
      ry += (y - ry) * 0.18;
      ring.style.left = rx + "px";
      ring.style.top = ry + "px";
      requestAnimationFrame(follow);
    }
    follow();
    document.querySelectorAll("a, button").forEach(function (el) {
      el.addEventListener("mouseenter", function () {
        document.body.classList.add("is-hovering");
      });
      el.addEventListener("mouseleave", function () {
        document.body.classList.remove("is-hovering");
      });
    });
  }

  window.addEventListener("pageshow", function () {
    document.documentElement.style.opacity = "";
    document.documentElement.style.transition = "";
    document.body.classList.remove("menu-open");
  });
})();
