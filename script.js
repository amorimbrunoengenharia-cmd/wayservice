// Navegação - Efeito de scroll
const navbar = document.getElementById('navbar');
const navLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Menu Mobile Toggle
const menuToggle = document.getElementById('menuToggle');
const navMenu = document.getElementById('navMenu');

menuToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
});

// Fechar menu ao clicar em um link
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        
        // Atualizar link ativo
        navLinks.forEach(l => l.classList.remove('active'));
        link.classList.add('active');
    });
});

// Smooth Scroll e atualização do link ativo baseado na seção visível
const sections = document.querySelectorAll('section[id]');

function updateActiveLink() {
    const scrollY = window.pageYOffset;

    sections.forEach(section => {
        const sectionHeight = section.offsetHeight;
        const sectionTop = section.offsetTop - 100;
        const sectionId = section.getAttribute('id');
        
        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${sectionId}`) {
                    link.classList.add('active');
                }
            });
        }
    });
}

window.addEventListener('scroll', updateActiveLink);

// FAQ Accordion - Event Delegation (Solução Final)
function initFAQAccordion() {
    const faqContainer = document.querySelector('.faq-container');
    if (!faqContainer) return;
    
    // Um Único listener no container (event delegation)
    faqContainer.addEventListener('click', function(e) {
        // Encontrar o botão clicado
        const button = e.target.closest('.faq-question');
        if (!button) return;
        
        // Encontrar o item pai
        const clickedItem = button.closest('.faq-item');
        if (!clickedItem) return;
        
        // Verificar estado atual
        const isOpen = clickedItem.classList.contains('active');
        
        // Fechar todos os itens
        const allItems = faqContainer.querySelectorAll('.faq-item');
        allItems.forEach(item => item.classList.remove('active'));
        
        // Abrir o clicado se estava fechado
        if (!isOpen) {
            clickedItem.classList.add('active');
        }
    });
}

// Formulário de Contato
const contactForm = document.getElementById('contactForm');

if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // Pegar botão de submit
        const submitButton = contactForm.querySelector('button[type="submit"]');
        const originalButtonText = submitButton.innerHTML;
        
        // Desabilitar botão e mostrar loading
        submitButton.disabled = true;
        submitButton.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="spin">
                <circle cx="12" cy="12" r="10"></circle>
                <path d="M12 6v6l4 2"></path>
            </svg>
            Enviando...
        `;
        submitButton.style.opacity = '0.7';
        submitButton.style.cursor = 'not-allowed';
        
        // Coletar dados do formulário
        const formData = new FormData(contactForm);
        const nome = formData.get('nome');
        const empresa = formData.get('empresa');
        const telefone = formData.get('telefone');
        const email = formData.get('email');
        const mensagem = formData.get('mensagem');
        
        // Criar mensagem para WhatsApp
        const whatsappMessage = `
*Nova Solicitação de Orçamento*

*Nome:* ${nome}
*Empresa:* ${empresa}
*Telefone:* ${telefone}
*E-mail:* ${email || 'Não informado'}

*Mensagem:*
${mensagem}
        `.trim();
        
        // Codificar mensagem para URL
        const encodedMessage = encodeURIComponent(whatsappMessage);
        const whatsappNumber = '5518997421905';
        const whatsappURL = `https://wa.me/${whatsappNumber}?text=${encodedMessage}`;
        
        // Abrir WhatsApp em nova aba
        window.open(whatsappURL, '_blank');
        
        // Restaurar botão após pequeno delay
        setTimeout(() => {
            submitButton.disabled = false;
            submitButton.innerHTML = originalButtonText;
            submitButton.style.opacity = '1';
            submitButton.style.cursor = 'pointer';
        }, 2000);
        
        // Limpar formulário
        contactForm.reset();
        
        // Mostrar mensagem de sucesso (opcional)
        showNotification('Redirecionando para WhatsApp...', 'success');
    });
}

// Função para mostrar notificações
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        padding: 1rem 1.5rem;
        background: ${type === 'success' ? 'var(--primary-green)' : 'rgba(255, 255, 255, 0.1)'};
        color: ${type === 'success' ? 'var(--dark-bg)' : 'var(--text-white)'};
        border-radius: 12px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(16px);
        z-index: 10000;
        animation: slideIn 0.3s ease;
        font-weight: 600;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Animação de entrada para elementos
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observar cards e elementos que devem animar
const animatedElements = document.querySelectorAll('.card, .process-card, .feature-card, .section-header');
animatedElements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
});

// Adicionar estilos de animação
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Prevenir envio padrão em links âncora
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const offsetTop = target.offsetTop - 80;
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// Validação de telefone (formato brasileiro)
const telefoneInput = document.querySelector('input[name="telefone"]');
if (telefoneInput) {
    telefoneInput.addEventListener('input', (e) => {
        let value = e.target.value.replace(/\D/g, '');
        
        if (value.length <= 11) {
            if (value.length <= 2) {
                e.target.value = value;
            } else if (value.length <= 6) {
                e.target.value = `(${value.slice(0, 2)}) ${value.slice(2)}`;
            } else if (value.length <= 10) {
                e.target.value = `(${value.slice(0, 2)}) ${value.slice(2, 6)}-${value.slice(6)}`;
            } else {
                e.target.value = `(${value.slice(0, 2)}) ${value.slice(2, 7)}-${value.slice(7, 11)}`;
            }
        }
    });
}

// Adicionar efeito de hover nos cards de serviço
const serviceCards = document.querySelectorAll('.service-card');
serviceCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.style.transform = 'translateY(-8px)';
    });
    
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'translateY(0)';
    });
});

// Filtros de Projetos
const filterButtons = document.querySelectorAll('.filter-btn');
const projectCards = document.querySelectorAll('.project-card');
const projectSearch = document.getElementById('projectSearch');
const projectsGrid = document.querySelector('.projects-grid');

if (filterButtons.length > 0) {
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remover active de todos
            filterButtons.forEach(btn => btn.classList.remove('active'));
            // Adicionar active ao clicado
            button.classList.add('active');
            
            const filter = button.getAttribute('data-filter');
            filterProjects(filter);
        });
    });
}

if (projectSearch) {
    projectSearch.addEventListener('input', (e) => {
        const searchTerm = e.target.value.toLowerCase();
        const activeFilter = document.querySelector('.filter-btn.active').getAttribute('data-filter');
        filterProjects(activeFilter, searchTerm);
    });
}

function filterProjects(category, searchTerm = '') {
    let visibleCount = 0;
    
    projectCards.forEach(card => {
        const cardCategory = card.getAttribute('data-category');
        const cardTitle = card.querySelector('h3').textContent.toLowerCase();
        const cardDescription = card.querySelector('.project-description').textContent.toLowerCase();
        
        const matchesCategory = category === 'all' || cardCategory === category;
        const matchesSearch = searchTerm === '' || 
                             cardTitle.includes(searchTerm) || 
                             cardDescription.includes(searchTerm);
        
        if (matchesCategory && matchesSearch) {
            card.style.display = 'flex';
            visibleCount++;
        } else {
            card.style.display = 'none';
        }
    });
    
    updateProjectCount(visibleCount);
}

function updateProjectCount(count) {
    let countElement = document.querySelector('.project-count');
    if (!countElement && projectsGrid) {
        countElement = document.createElement('div');
        countElement.className = 'project-count';
        projectsGrid.parentElement.insertBefore(countElement, projectsGrid);
    }
    if (countElement) {
        countElement.textContent = `${count} projeto${count !== 1 ? 's' : ''} encontrado${count !== 1 ? 's' : ''}`;
    }
}

// Formulário de Orçamento
const quoteForm = document.getElementById('quoteForm');

if (quoteForm) {
    quoteForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // Validar campos
        const formData = new FormData(quoteForm);
        const name = formData.get('name');
        const company = formData.get('company');
        const phone = formData.get('phone');
        const email = formData.get('email') || 'Não informado';
        const message = formData.get('message');
        const workType = formData.get('workType') || 'Não especificado';
        const deadline = formData.get('deadline') || 'Não especificado';
        const location = formData.get('location') || 'Não especificado';
        
        // Mostrar loading
        const submitBtn = quoteForm.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<svg class="spinner" width="20" height="20" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="3" fill="none" opacity="0.25"/><path fill="currentColor" d="M12 2a10 10 0 0 1 10 10h-3a7 7 0 0 0-7-7V2z"/></svg> Enviando...';
        submitBtn.disabled = true;
        
        // Criar mensagem para WhatsApp
        const whatsappMessage = `
*Nova Solicitação de Orçamento - Way Service*

*Nome:* ${name}
*Empresa/Órgão:* ${company}
*Telefone:* ${phone}
*E-mail:* ${email}
*Tipo de Obra:* ${workType}
*Prazo Desejado:* ${deadline}
*Localização:* ${location}

*Descrição da Necessidade:*
${message}
        `.trim();
        
        const encodedMessage = encodeURIComponent(whatsappMessage);
        const whatsappNumber = '5518997421905';
        const whatsappURL = `https://wa.me/${whatsappNumber}?text=${encodedMessage}`;
        
        // Simular delay de envio
        setTimeout(() => {
            window.open(whatsappURL, '_blank');
            
            // Resetar botão
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
            
            // Mostrar notificação de sucesso
            showNotification('Redirecionando para WhatsApp...', 'success');
            
            // Limpar formulário
            quoteForm.reset();
        }, 1000);
    });
}

// Máscara de telefone para formulário de orçamento
const phoneInputs = document.querySelectorAll('input[type="tel"]');
phoneInputs.forEach(input => {
    input.addEventListener('input', (e) => {
        let value = e.target.value.replace(/\D/g, '');
        
        if (value.length <= 11) {
            if (value.length <= 2) {
                e.target.value = value;
            } else if (value.length <= 6) {
                e.target.value = `(${value.slice(0, 2)}) ${value.slice(2)}`;
            } else if (value.length <= 10) {
                e.target.value = `(${value.slice(0, 2)}) ${value.slice(2, 6)}-${value.slice(6)}`;
            } else {
                e.target.value = `(${value.slice(0, 2)}) ${value.slice(2, 7)}-${value.slice(7, 11)}`;
            }
        }
    });
});

// Modal de Detalhes do Projeto
function openProjectModal(projectData) {
    const modal = document.getElementById('projectModal');
    if (!modal) return;
    
    document.getElementById('modalTitle').textContent = projectData.title;
    document.getElementById('modalCategory').textContent = projectData.category;
    document.getElementById('modalDescription').textContent = projectData.description;
    document.getElementById('modalLocation').textContent = projectData.location;
    document.getElementById('modalArea').textContent = projectData.area;
    document.getElementById('modalYear').textContent = projectData.year;
    
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
}

function closeProjectModal() {
    const modal = document.getElementById('projectModal');
    if (modal) {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
}

// Fechar modal clicando fora
window.addEventListener('click', (e) => {
    const modal = document.getElementById('projectModal');
    if (e.target === modal) {
        closeProjectModal();
    }
});

// Botão Voltar ao Topo
const backToTopBtn = document.getElementById('backToTop');

if (backToTopBtn) {
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            backToTopBtn.classList.add('visible');
        } else {
            backToTopBtn.classList.remove('visible');
        }
    });
    
    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// ========================================
// MELHORIAS VISUAIS AVANÇADAS - 2025
// ========================================

// Progress Bar no Topo
function initScrollProgress() {
    const progressBar = document.createElement('div');
    progressBar.className = 'scroll-progress';
    document.body.appendChild(progressBar);

    window.addEventListener('scroll', () => {
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        progressBar.style.width = scrolled + '%';
    });
}

// Scroll Reveal Animation
function initScrollReveal() {
    const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale, .reveal-rotate');
    if (revealElements.length === 0) return;
    
    const revealOnScroll = () => {
        revealElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const elementVisible = 150;
            
            if (elementTop < window.innerHeight - elementVisible) {
                element.classList.add('active');
            }
        });
    };

    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll(); // Trigger inicial
}

// Typing Effect - DISABLED FOR IMMEDIATE READABILITY
function initTypingEffect() {
    // Função desabilitada para melhor UX
    // Texto aparece imediatamente sem animação
    return;
}

// Partículas Animadas
function initParticles() {
    const heroSections = document.querySelectorAll('.hero');
    if (heroSections.length === 0) return;
    
    heroSections.forEach(hero => {
        const container = document.createElement('div');
        container.className = 'particles-container';
        hero.appendChild(container);

        for (let i = 0; i < 20; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 15 + 's';
            particle.style.animationDuration = (Math.random() * 10 + 10) + 's';
            container.appendChild(particle);
        }
    });
}

// Ripple Effect em Botões
function initRippleEffect() {
    const buttons = document.querySelectorAll('.btn-primary, .btn-secondary, .btn-ripple');
    if (buttons.length === 0) return;
    
    buttons.forEach(button => {
        button.classList.add('btn-ripple');
        
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            ripple.className = 'ripple';
            
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            
            this.appendChild(ripple);
            
            setTimeout(() => ripple.remove(), 600);
        });
    });
}

// Toast Notification
function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    
    const icon = type === 'success' 
        ? '<svg class="toast-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>'
        : '<svg class="toast-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" x2="9" y1="9" y2="15"/><line x1="9" x2="15" y1="9" y2="15"/></svg>';
    
    toast.innerHTML = `${icon}<div class="toast-message">${message}</div>`;
    document.body.appendChild(toast);
    
    setTimeout(() => toast.classList.add('show'), 100);
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 400);
    }, 3000);
}

// Loading Spinner
function showSpinner() {
    let spinner = document.querySelector('.spinner-overlay');
    if (!spinner) {
        spinner = document.createElement('div');
        spinner.className = 'spinner-overlay';
        spinner.innerHTML = '<div class="spinner"></div>';
        document.body.appendChild(spinner);
    }
    setTimeout(() => spinner.classList.add('active'), 10);
    return spinner;
}

function hideSpinner() {
    const spinner = document.querySelector('.spinner-overlay');
    if (spinner) {
        spinner.classList.remove('active');
    }
}

// Lightbox para Galeria
function initLightbox() {
    const lightbox = document.getElementById('lightbox');
    if (!lightbox) return;

    const projectCards = document.querySelectorAll('.project-card');
    const lightboxImage = document.getElementById('lightboxImage');
    const lightboxTitle = document.getElementById('lightboxTitle');
    const lightboxDescription = document.getElementById('lightboxDescription');
    const lightboxDetails = document.getElementById('lightboxDetails');
    const closeBtn = lightbox.querySelector('.lightbox-close');
    const prevBtn = lightbox.querySelector('.lightbox-prev');
    const nextBtn = lightbox.querySelector('.lightbox-next');
    
    let currentIndex = 0;
    let projectsArray = [];

    // Coletar informações de todos os projetos
    projectCards.forEach((card, index) => {
        const projectImage = card.querySelector('.project-image');
        const title = card.querySelector('.project-header h3').textContent;
        const description = card.querySelector('.project-description').textContent;
        const detailItems = card.querySelectorAll('.detail-item');
        const gradient = window.getComputedStyle(projectImage).background;
        
        projectsArray.push({
            gradient: gradient,
            title: title,
            description: description,
            details: Array.from(detailItems).map(item => item.innerHTML)
        });

        // Adicionar click no card inteiro
        projectImage.style.cursor = 'pointer';
        projectImage.addEventListener('click', () => {
            currentIndex = index;
            openLightbox();
        });
    });

    function openLightbox() {
        const project = projectsArray[currentIndex];
        
        // Atualizar imagem (gradient como placeholder)
        lightboxImage.style.background = project.gradient;
        lightboxImage.style.width = '100%';
        lightboxImage.style.height = '500px';
        lightboxImage.style.borderRadius = '12px';
        
        // Atualizar informações
        lightboxTitle.textContent = project.title;
        lightboxDescription.textContent = project.description;
        
        // Atualizar detalhes
        lightboxDetails.innerHTML = project.details.map(detail => 
            `<div class="detail-item">${detail}</div>`
        ).join('');
        
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeLightbox() {
        lightbox.classList.remove('active');
        document.body.style.overflow = '';
    }

    function showNext() {
        currentIndex = (currentIndex + 1) % projectsArray.length;
        openLightbox();
    }

    function showPrev() {
        currentIndex = (currentIndex - 1 + projectsArray.length) % projectsArray.length;
        openLightbox();
    }

    // Event listeners
    closeBtn.addEventListener('click', closeLightbox);
    nextBtn.addEventListener('click', showNext);
    prevBtn.addEventListener('click', showPrev);
    
    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) closeLightbox();
    });

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (!lightbox.classList.contains('active')) return;
        if (e.key === 'Escape') closeLightbox();
        if (e.key === 'ArrowRight') showNext();
        if (e.key === 'ArrowLeft') showPrev();
    });
}

// Wizard Multi-Step Form
function initWizardForm() {
    const wizardContainer = document.querySelector('.wizard-container');
    if (!wizardContainer) return;

    const steps = wizardContainer.querySelectorAll('.wizard-step');
    const panels = wizardContainer.querySelectorAll('.wizard-panel');
    const nextBtns = wizardContainer.querySelectorAll('.wizard-next');
    const prevBtns = wizardContainer.querySelectorAll('.wizard-prev');
    let currentStep = 0;

    function showStep(stepIndex) {
        // Update steps
        steps.forEach((step, index) => {
            step.classList.remove('active');
            if (index < stepIndex) {
                step.classList.add('completed');
            } else {
                step.classList.remove('completed');
            }
            if (index === stepIndex) {
                step.classList.add('active');
            }
        });

        // Update panels
        panels.forEach((panel, index) => {
            panel.classList.remove('active');
            if (index === stepIndex) {
                panel.classList.add('active');
            }
        });

        currentStep = stepIndex;
        updateProgress();
    }

    function updateProgress() {
        const progress = ((currentStep + 1) / steps.length) * 100;
        const progressBar = document.querySelector('.form-progress-bar');
        if (progressBar) {
            progressBar.style.width = progress + '%';
        }
    }

    nextBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            if (validateStep(currentStep)) {
                if (currentStep < steps.length - 1) {
                    showStep(currentStep + 1);
                }
            }
        });
    });

    prevBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            if (currentStep > 0) {
                showStep(currentStep - 1);
            }
        });
    });

    function validateStep(stepIndex) {
        const panel = panels[stepIndex];
        const inputs = panel.querySelectorAll('input[required], select[required], textarea[required]');
        let isValid = true;

        inputs.forEach(input => {
            if (!input.value.trim()) {
                input.parentElement.classList.add('invalid');
                isValid = false;
            } else {
                input.parentElement.classList.remove('invalid');
                input.parentElement.classList.add('valid');
            }
        });

        return isValid;
    }

    showStep(0);
}

// Validação em Tempo Real
function initRealTimeValidation() {
    const inputs = document.querySelectorAll('input[required], select[required], textarea[required]');
    if (inputs.length === 0) return;
    
    inputs.forEach(input => {
        // Adicionar ícones de validação
        if (!input.parentElement.querySelector('.validation-icon')) {
            const checkIcon = document.createElement('span');
            checkIcon.className = 'validation-icon check';
            checkIcon.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>';
            checkIcon.style.color = 'var(--primary-green)';
            
            const errorIcon = document.createElement('span');
            errorIcon.className = 'validation-icon error';
            errorIcon.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" x2="9" y1="9" y2="15"/><line x1="9" x2="15" y1="9" y2="15"/></svg>';
            errorIcon.style.color = '#ff4757';
            
            input.parentElement.appendChild(checkIcon);
            input.parentElement.appendChild(errorIcon);
        }

        input.addEventListener('blur', () => validateInput(input));
        input.addEventListener('input', () => {
            if (input.parentElement.classList.contains('invalid')) {
                validateInput(input);
            }
        });
    });

    function validateInput(input) {
        const formGroup = input.parentElement;
        
        if (input.type === 'email') {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(input.value) && input.value) {
                formGroup.classList.add('invalid');
                formGroup.classList.remove('valid');
                return false;
            }
        }
        
        if (input.value.trim() === '' && input.hasAttribute('required')) {
            formGroup.classList.add('invalid');
            formGroup.classList.remove('valid');
            return false;
        } else if (input.value.trim() !== '') {
            formGroup.classList.remove('invalid');
            formGroup.classList.add('valid');
            return true;
        }
        
        formGroup.classList.remove('invalid', 'valid');
        return true;
    }
}

// Upload de Arquivos com Drag & Drop
function initFileUpload() {
    const uploadAreas = document.querySelectorAll('.file-upload-area');
    if (uploadAreas.length === 0) return;
    
    uploadAreas.forEach(area => {
        const input = area.querySelector('input[type="file"]') || createFileInput(area);
        const preview = area.nextElementSibling?.classList.contains('file-preview') 
            ? area.nextElementSibling 
            : createPreviewArea(area);

        area.addEventListener('click', () => input.click());
        
        area.addEventListener('dragover', (e) => {
            e.preventDefault();
            area.classList.add('drag-over');
        });
        
        area.addEventListener('dragleave', () => {
            area.classList.remove('drag-over');
        });
        
        area.addEventListener('drop', (e) => {
            e.preventDefault();
            area.classList.remove('drag-over');
            const files = e.dataTransfer.files;
            handleFiles(files, preview);
        });
        
        input.addEventListener('change', (e) => {
            handleFiles(e.target.files, preview);
        });
    });

    function createFileInput(area) {
        const input = document.createElement('input');
        input.type = 'file';
        input.multiple = true;
        input.accept = 'image/*,.pdf';
        input.style.display = 'none';
        area.appendChild(input);
        return input;
    }

    function createPreviewArea(area) {
        const preview = document.createElement('div');
        preview.className = 'file-preview';
        area.after(preview);
        return preview;
    }

    function handleFiles(files, preview) {
        Array.from(files).forEach(file => {
            if (file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    const item = document.createElement('div');
                    item.className = 'file-preview-item';
                    item.innerHTML = `
                        <img class="file-preview-image" src="${e.target.result}" alt="${file.name}">
                        <button class="file-preview-remove">&times;</button>
                    `;
                    
                    item.querySelector('.file-preview-remove').addEventListener('click', () => {
                        item.remove();
                    });
                    
                    preview.appendChild(item);
                };
                reader.readAsDataURL(file);
            }
        });
    }
}

// Timer de Urgência
function initUrgencyTimer() {
    const timers = document.querySelectorAll('.urgency-timer');
    if (timers.length === 0) return;
    
    timers.forEach(timer => {
        // Definir tempo inicial (exemplo: 48 horas)
        const endTime = new Date().getTime() + (48 * 60 * 60 * 1000);
        
        function updateTimer() {
            const now = new Date().getTime();
            const distance = endTime - now;
            
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);
            
            const hoursEl = timer.querySelector('.timer-hours');
            const minutesEl = timer.querySelector('.timer-minutes');
            const secondsEl = timer.querySelector('.timer-seconds');
            
            if (hoursEl) hoursEl.textContent = hours.toString().padStart(2, '0');
            if (minutesEl) minutesEl.textContent = minutes.toString().padStart(2, '0');
            if (secondsEl) secondsEl.textContent = seconds.toString().padStart(2, '0');
            
            if (distance < 0) {
                clearInterval(interval);
                timer.textContent = 'Prazo expirado';
            }
        }
        
        updateTimer();
        const interval = setInterval(updateTimer, 1000);
    });
}

// Contador Animado
function initCounterAnimation() {
    const counters = document.querySelectorAll('.counter');
    if (counters.length === 0) return;
    
    const animateCounter = (counter) => {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;
        
        const updateCounter = () => {
            current += increment;
            if (current < target) {
                counter.textContent = Math.floor(current);
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target;
            }
        };
        
        updateCounter();
    };
    
    counters.forEach(counter => animateCounter(counter));
}

// Filtro de Projetos
function initProjectFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');
    const searchInput = document.getElementById('projectSearch');
    const sortSelect = document.getElementById('projectSort');
    
    if (filterButtons.length === 0) return;

    let currentFilter = 'all';
    let currentSearchTerm = '';

    // Filtrar por categoria
    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Atualizar botão ativo
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            currentFilter = btn.getAttribute('data-filter');
            applyFilters();
        });
    });

    // Busca por texto
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            currentSearchTerm = e.target.value.toLowerCase();
            applyFilters();
        });
    }

    // Ordenação
    if (sortSelect) {
        sortSelect.addEventListener('change', (e) => {
            const sortType = e.target.value;
            sortProjects(sortType);
        });
    }

    function applyFilters() {
        projectCards.forEach(card => {
            const category = card.getAttribute('data-category');
            const title = card.querySelector('.project-header h3').textContent.toLowerCase();
            const description = card.querySelector('.project-description').textContent.toLowerCase();
            
            const matchesFilter = currentFilter === 'all' || category === currentFilter;
            const matchesSearch = currentSearchTerm === '' || 
                                 title.includes(currentSearchTerm) || 
                                 description.includes(currentSearchTerm);
            
            if (matchesFilter && matchesSearch) {
                card.style.display = '';
                setTimeout(() => card.classList.add('reveal'), 50);
            } else {
                card.style.display = 'none';
                card.classList.remove('reveal');
            }
        });

        // Atualizar contagem
        const visibleCards = Array.from(projectCards).filter(card => card.style.display !== 'none');
        console.log(`${visibleCards.length} projetos visíveis`);
    }

    function sortProjects(sortType) {
        const projectsGrid = document.querySelector('.projects-grid');
        if (!projectsGrid) return;

        const cardsArray = Array.from(projectCards);
        
        switch(sortType) {
            case 'recent':
                cardsArray.sort((a, b) => {
                    const yearA = parseInt(a.querySelector('.detail-item:last-child')?.textContent) || 0;
                    const yearB = parseInt(b.querySelector('.detail-item:last-child')?.textContent) || 0;
                    return yearB - yearA;
                });
                break;
            case 'area':
                cardsArray.sort((a, b) => {
                    const areaA = parseInt(a.querySelector('.detail-item:nth-child(2)')?.textContent.replace(/\D/g, '')) || 0;
                    const areaB = parseInt(b.querySelector('.detail-item:nth-child(2)')?.textContent.replace(/\D/g, '')) || 0;
                    return areaB - areaA;
                });
                break;
            case 'name':
                cardsArray.sort((a, b) => {
                    const nameA = a.querySelector('.project-header h3').textContent;
                    const nameB = b.querySelector('.project-header h3').textContent;
                    return nameA.localeCompare(nameB);
                });
                break;
        }

        // Reorganizar DOM
        cardsArray.forEach(card => projectsGrid.appendChild(card));
    }
}

// Inicializar animação de contadores
function initCounterAnimation() {
    const counters = document.querySelectorAll('.counter');
    if (counters.length === 0) return;
    
    const animateCounter = (counter) => {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;
        
        const updateCounter = () => {
            current += increment;
            if (current < target) {
                counter.textContent = Math.floor(current);
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target;
            }
        };
        
        updateCounter();
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    counters.forEach(counter => observer.observe(counter));
}

// FAQ com Busca
function initFAQSearch() {
    const searchInput = document.querySelector('.faq-search input');
    if (!searchInput) return;
    
    const faqItems = document.querySelectorAll('.faq-item');
    
    searchInput.addEventListener('input', (e) => {
        const searchTerm = e.target.value.toLowerCase();
        
        faqItems.forEach(item => {
            const question = item.querySelector('.faq-question').textContent.toLowerCase();
            const answer = item.querySelector('.faq-answer').textContent.toLowerCase();
            
            if (question.includes(searchTerm) || answer.includes(searchTerm)) {
                item.classList.remove('hidden');
            } else {
                item.classList.add('hidden');
            }
        });
    });
}

// Timeline Scroll Animation
function initTimeline() {
    const timelineItems = document.querySelectorAll('.timeline-item');
    if (timelineItems.length === 0) return;
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, { threshold: 0.3 });
    
    timelineItems.forEach(item => observer.observe(item));
}

// Testimonial Slider
function initTestimonialSlider() {
    const slider = document.querySelector('.testimonial-slider');
    if (!slider) return;
    
    const track = slider.querySelector('.testimonial-track');
    const items = slider.querySelectorAll('.testimonial-item');
    const dotsContainer = slider.querySelector('.testimonial-dots');
    let currentIndex = 0;
    
    // Criar dots
    items.forEach((_, index) => {
        const dot = document.createElement('div');
        dot.className = 'testimonial-dot';
        if (index === 0) dot.classList.add('active');
        dot.addEventListener('click', () => goToSlide(index));
        dotsContainer.appendChild(dot);
    });
    
    function goToSlide(index) {
        currentIndex = index;
        track.style.transform = `translateX(-${index * 100}%)`;
        updateDots();
    }
    
    function updateDots() {
        const dots = dotsContainer.querySelectorAll('.testimonial-dot');
        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === currentIndex);
        });
    }
    
    // Auto-play
    setInterval(() => {
        currentIndex = (currentIndex + 1) % items.length;
        goToSlide(currentIndex);
    }, 5000);
}

// Inicializar todas as melhorias ao carregar
document.addEventListener('DOMContentLoaded', () => {
    initScrollProgress();
    initScrollReveal();
    initTypingEffect();
    initParticles();
    initRippleEffect();
    initLightbox();
    initWizardForm();
    initRealTimeValidation();
    initFileUpload();
    initUrgencyTimer();
    initCounterAnimation();
    initProjectFilters();
    initFAQAccordion();
    initFAQSearch();
    initTimeline();
    initTestimonialSlider();
});

// Log de inicialização
console.log('Way Service Website - Carregado com sucesso! ✓');
console.log('Melhorias visuais 2025 - Ativadas! ✨');
