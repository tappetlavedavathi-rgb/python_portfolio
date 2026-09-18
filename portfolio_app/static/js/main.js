(() => {
    const root = document.documentElement;
    const nav = document.getElementById("site-nav");
    const toggle = document.querySelector("[data-nav-toggle]");
    const themeToggle = document.querySelector("[data-theme-toggle]");
    const toTop = document.querySelector(".to-top");
    const header = document.querySelector("[data-header]");
    const storedTheme = localStorage.getItem("portfolio-theme");
    const preferred = window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark";

    root.setAttribute("data-theme", storedTheme || preferred);

    themeToggle?.addEventListener("click", () => {
        const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
        root.setAttribute("data-theme", next);
        localStorage.setItem("portfolio-theme", next);
    });

    const closeNav = () => {
        nav?.classList.remove("is-open");
        toggle?.setAttribute("aria-expanded", "false");
        document.body.classList.remove("nav-open");
    };

    toggle?.addEventListener("click", () => {
        const open = nav?.classList.toggle("is-open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
        document.body.classList.toggle("nav-open", Boolean(open));
    });

    nav?.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", closeNav);
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            closeNav();
        }
    });

    const sections = [...document.querySelectorAll("section[id]")];
    const navLinks = [...document.querySelectorAll(".nav-links a")];

    const setActive = () => {
        const offset = (header?.offsetHeight || 76) + 24;
        let current = sections[0];
        sections.forEach((section) => {
            if (window.scrollY + offset >= section.offsetTop) {
                current = section;
            }
        });
        navLinks.forEach((link) => {
            const href = link.getAttribute("href");
            link.classList.toggle("active", current && href === `#${current.id}`);
        });
        if (toTop) {
            toTop.hidden = window.scrollY < 500;
        }
    };

    window.addEventListener("scroll", setActive, { passive: true });
    setActive();

    toTop?.addEventListener("click", () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });
})();
