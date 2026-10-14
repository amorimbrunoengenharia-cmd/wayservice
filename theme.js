(function () {
    const storageKey = 'wayservice-theme';
    const storedTheme = (() => {
        try {
            return localStorage.getItem(storageKey);
        } catch {
            return null;
        }
    })();
    const initialTheme = storedTheme || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    const button = document.createElement('button');
    button.id = 'themeToggle';
    button.className = 'theme-toggle';
    button.type = 'button';
    button.addEventListener('click', () => setTheme(document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark', true));

    function setTheme(theme, persist) {
        document.documentElement.dataset.theme = theme;
        button.innerHTML = theme === 'dark'
            ? '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2m0 16v2M4.93 4.93l1.42 1.42m11.3 11.3 1.42 1.42M2 12h2m16 0h2M4.93 19.07l1.42-1.42m11.3-11.3 1.42-1.42"></path></svg>'
            : '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.9 13A8.5 8.5 0 0 1 11 3.1 8.5 8.5 0 1 0 20.9 13Z"></path></svg>';
        const nextTheme = theme === 'dark' ? 'claro' : 'escuro';
        button.setAttribute('aria-label', `Ativar tema ${nextTheme}`);
        button.title = `Ativar tema ${nextTheme}`;
        document.querySelectorAll('meta[name="theme-color"]').forEach(meta => {
            meta.content = theme === 'dark' ? '#1E1F27' : '#F4F6F3';
        });

        if (persist) {
            try {
                localStorage.setItem(storageKey, theme);
            } catch {
                return;
            }
        }
    }

    const navContainer = document.querySelector('.nav-container');
    const pageNavigation = document.querySelector('.page-navigation');
    if (navContainer) {
        const menuToggle = navContainer.querySelector('.menu-toggle');
        document.querySelectorAll('.whatsapp-float, .phone-float').forEach(action => {
            navContainer.insertBefore(action, menuToggle);
        });
        navContainer.insertBefore(button, menuToggle);
    } else if (pageNavigation) {
        button.classList.add('theme-toggle-in-page-nav');
        const whatsappLink = document.querySelector('.whatsapp-float');
        if (whatsappLink) {
            whatsappLink.classList.add('whatsapp-nav-action');
            pageNavigation.appendChild(whatsappLink);
        }
        pageNavigation.appendChild(button);
    } else {
        document.querySelector('nav')?.appendChild(button);
    }

    setTheme(initialTheme, false);
})();
