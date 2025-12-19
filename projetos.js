/**
 * Sistema de Galeria Dinâmica de Projetos
 * Gerencia renderização de cards e lightbox com navegação de imagens
 */

// Configuração de gradientes para as categorias
const categoryGradients = {
    'obras_publicas': 'linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)',
    'varejo': 'linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)',
    'industrial': 'linear-gradient(135deg, #30cfd0 0%, #330867 100%)',
    'comercial': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    'infraestrutura': 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
    'manutencao': 'linear-gradient(135deg, #c471f5 0%, #fa71cd 100%)'
};

// Labels amigáveis para categorias
const categoryLabels = {
    'obras_publicas': 'Obras Públicas',
    'varejo': 'Varejo',
    'industrial': 'Industrial',
    'comercial': 'Comercial',
    'infraestrutura': 'Infraestrutura',
    'manutencao': 'Manutenção'
};

// Tags CSS customizadas por categoria
const categoryTagClasses = {
    'obras_publicas': 'publico-tag',
    'varejo': 'varejo-tag',
    'industrial': 'industrial-tag',
    'comercial': '',
    'infraestrutura': '',
    'manutencao': 'manutencao-tag'
};

// Ícones SVG por categoria
const categoryIcons = {
    'obras_publicas': `<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M3 9h18v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9Z"></path>
        <path d="M3 9V7a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v2"></path>
        <line x1="9" x2="9" y1="13" y2="17"></line>
        <line x1="15" x2="15" y1="13" y2="17"></line>
    </svg>`,
    'varejo': `<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="m2 7 4.41-4.41A2 2 0 0 1 7.83 2h8.34a2 2 0 0 1 1.42.59L22 7"></path>
        <path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"></path>
        <path d="M15 22v-4a2 2 0 0 0-2-2h-2a2 2 0 0 0-2 2v4"></path>
        <path d="M2 7h20"></path>
    </svg>`,
    'industrial': `<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <rect width="7" height="7" x="3" y="3" rx="1"></rect>
        <rect width="7" height="7" x="14" y="3" rx="1"></rect>
        <rect width="7" height="7" x="14" y="14" rx="1"></rect>
        <rect width="7" height="7" x="3" y="14" rx="1"></rect>
    </svg>`,
    'comercial': `<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
        <polyline points="9 22 9 12 15 12 15 22"></polyline>
    </svg>`,
    'infraestrutura': `<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"></path>
        <path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"></path>
        <path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"></path>
    </svg>`,
    'manutencao': `<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
    </svg>`
};

// Estado global
let allProjects = [];
let currentProject = null;
let currentImageIndex = 0;

/**
 * Carrega os projetos do arquivo JSON
 */
async function loadProjects() {
    console.log('🔄 Iniciando carregamento de projetos...');
    try {
        const response = await fetch('projetos.json');
        console.log('📡 Response status:', response.status);
        if (!response.ok) {
            throw new Error('Erro ao carregar projetos');
        }
        allProjects = await response.json();
        console.log('✅ Projetos carregados:', allProjects.length);
        console.log('📋 Projetos:', allProjects);
        renderProjects(allProjects);
        updateProjectCount(allProjects.length);
    } catch (error) {
        console.error('❌ Erro ao carregar projetos:', error);
        showError();
    }
}

/**
 * Renderiza os cards de projetos na grid
 */
function renderProjects(projects) {
    console.log('🎨 Renderizando projetos...');
    const grid = document.getElementById('projectsGrid');
    console.log('📦 Grid element:', grid);
    if (!grid) {
        console.error('❌ Elemento projectsGrid não encontrado!');
        return;
    }

    grid.innerHTML = '';
    console.log('🔄 Limpando grid e adicionando', projects.length, 'projetos');

    projects.forEach((project, index) => {
        console.log(`➕ Adicionando projeto ${index + 1}:`, project.titulo);
        const card = createProjectCard(project, index);
        grid.appendChild(card);
        
        // Ativa animação reveal após adicionar ao DOM
        setTimeout(() => {
            card.classList.add('active');
        }, 50 + (index * 100));
    });
    
    console.log('✅ Renderização concluída!');
}

/**
 * Cria o HTML de um card de projeto
 */
function createProjectCard(project, index) {
    const card = document.createElement('div');
    card.className = 'project-card card glassmorphism card-shine reveal reveal-scale';
    card.setAttribute('data-category', project.categoria);
    
    // Adiciona delays de animação alternados
    if (index % 4 !== 0) {
        card.classList.add(`reveal-delay-${index % 4}`);
    }

    const gradient = categoryGradients[project.categoria] || categoryGradients['comercial'];
    const icon = categoryIcons[project.categoria] || categoryIcons['comercial'];
    const label = categoryLabels[project.categoria] || project.categoria;
    const tagClass = categoryTagClasses[project.categoria] || '';

    // Detalhes opcionais
    const detailsHTML = generateDetailsHTML(project);

    // Badge de Acervo Técnico (se aplicável)
    const acervoHTML = generateAcervoBadge(project);

    card.innerHTML = `
        <div class="project-image" style="background-image: url('${project.imagemCapa}'); background-size: cover; background-position: center;">
            <div class="project-badge">${project.badge || 'Concluído'}</div>
            ${acervoHTML}
            <div class="project-image-icon">
                ${icon}
            </div>
        </div>
        <div class="project-content">
            <div class="project-header">
                <h3>${project.titulo}</h3>
                <span class="project-tag ${tagClass}">${label}</span>
            </div>
            <p class="project-description">${project.descricao}</p>
            ${detailsHTML}
            <div class="project-actions">
                <a href="projeto-${project.id}.html" class="btn-primary btn-view-gallery">
                    Ver Álbum
                </a>
                <a href="index.html#orcamento" class="btn-secondary">Solicitar Similar</a>
            </div>
        </div>
    `;

    return card;
}

/**
 * Gera o badge de acervo técnico (se aplicável)
 */
function generateAcervoBadge(project) {
    // Se não for acervo pessoal, não exibe nada
    if (!project.tipo_autoria || project.tipo_autoria !== 'acervo_pessoal') {
        return '';
    }

    const responsavel = project.responsavel_tecnico || 'Acervo Técnico';

    return `
        <div class="acervo-badge">
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
                <circle cx="9" cy="7" r="4"></circle>
                <polyline points="16 11 18 13 22 9"></polyline>
            </svg>
            <span>Gestão de Execução: ${responsavel}</span>
        </div>
    `;
}

/**
 * Gera o HTML dos detalhes do projeto (localização, área, ano)
 */
function generateDetailsHTML(project) {
    const details = [];

    if (project.localizacao) {
        details.push(`
            <div class="detail-item">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"></path>
                    <circle cx="12" cy="10" r="3"></circle>
                </svg>
                ${project.localizacao}
            </div>
        `);
    }

    if (project.area) {
        details.push(`
            <div class="detail-item">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect width="18" height="18" x="3" y="3" rx="2"></rect>
                </svg>
                ${project.area}
            </div>
        `);
    }

    if (project.ano) {
        details.push(`
            <div class="detail-item">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M8 2v4"></path>
                    <path d="M16 2v4"></path>
                    <rect width="18" height="18" x="3" y="4" rx="2"></rect>
                    <path d="M3 10h18"></path>
                </svg>
                ${project.ano}
            </div>
        `);
    }

    if (details.length === 0) return '';

    return `<div class="project-details">${details.join('')}</div>`;
}

/**
 * Abre a galeria de fotos no lightbox
 */
function openGallery(project) {
    console.log('🖼️ Abrindo galeria para:', project.titulo);
    console.log('📸 Total de fotos:', project.galeria.length);
    
    currentProject = project;
    currentImageIndex = 0;

    const lightbox = document.getElementById('lightbox');
    const lightboxImage = document.getElementById('lightboxImage');
    const lightboxTitle = document.getElementById('lightboxTitle');
    const lightboxDescription = document.getElementById('lightboxDescription');
    const lightboxDetails = document.getElementById('lightboxDetails');

    console.log('🎯 Elementos do lightbox:', { lightbox, lightboxImage, lightboxTitle });

    // Atualiza informações do projeto
    lightboxTitle.textContent = project.titulo;
    lightboxDescription.textContent = project.descricao;
    
    // Gera detalhes incluindo badge de acervo (se aplicável)
    let detailsContent = generateDetailsHTML(project);
    
    // Adiciona badge de acervo técnico no lightbox (se aplicável)
    if (project.tipo_autoria === 'acervo_pessoal' && project.responsavel_tecnico) {
        const acervoBadge = `
            <div class="lightbox-acervo-badge">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
                    <circle cx="9" cy="7" r="4"></circle>
                    <polyline points="16 11 18 13 22 9"></polyline>
                </svg>
                <span>Gestão de Execução: ${project.responsavel_tecnico}</span>
            </div>
        `;
        detailsContent = acervoBadge + detailsContent;
    }
    
    lightboxDetails.innerHTML = detailsContent;

    // Carrega primeira imagem
    showImage(0);

    // Exibe lightbox
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
}

/**
 * Exibe uma imagem específica da galeria
 */
function showImage(index) {
    if (!currentProject || !currentProject.galeria) return;

    const gallery = currentProject.galeria;
    
    // Garante que o índice está dentro dos limites
    currentImageIndex = ((index % gallery.length) + gallery.length) % gallery.length;

    const lightboxImage = document.getElementById('lightboxImage');
    const currentIndexSpan = document.getElementById('currentImageIndex');
    const totalImagesSpan = document.getElementById('totalImages');

    // Atualiza imagem
    lightboxImage.src = gallery[currentImageIndex];
    lightboxImage.alt = `${currentProject.titulo} - Foto ${currentImageIndex + 1}`;

    // Atualiza contador
    if (currentIndexSpan && totalImagesSpan) {
        currentIndexSpan.textContent = currentImageIndex + 1;
        totalImagesSpan.textContent = gallery.length;
    }

    // Mostra/oculta botões de navegação se houver apenas uma imagem
    const prevBtn = document.querySelector('.lightbox-prev');
    const nextBtn = document.querySelector('.lightbox-next');
    
    if (gallery.length <= 1) {
        if (prevBtn) prevBtn.style.display = 'none';
        if (nextBtn) nextBtn.style.display = 'none';
    } else {
        if (prevBtn) prevBtn.style.display = '';
        if (nextBtn) nextBtn.style.display = '';
    }
}

/**
 * Fecha o lightbox
 */
function closeLightbox() {
    const lightbox = document.getElementById('lightbox');
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
    currentProject = null;
    currentImageIndex = 0;
}

/**
 * Navega para a próxima imagem
 */
function nextImage() {
    if (!currentProject) return;
    showImage(currentImageIndex + 1);
}

/**
 * Navega para a imagem anterior
 */
function prevImage() {
    if (!currentProject) return;
    showImage(currentImageIndex - 1);
}

/**
 * Atualiza o contador de projetos no hero
 */
function updateProjectCount(count) {
    const counter = document.querySelector('.counter');
    if (counter) {
        // Anima o contador
        animateCounter(counter, 0, count, 1500);
    }
}

/**
 * Anima o contador de projetos
 */
function animateCounter(element, start, end, duration) {
    const range = end - start;
    const increment = range / (duration / 16);
    let current = start;

    const timer = setInterval(() => {
        current += increment;
        if (current >= end) {
            element.textContent = end;
            clearInterval(timer);
        } else {
            element.textContent = Math.floor(current);
        }
    }, 16);
}

/**
 * Mostra mensagem de erro
 */
function showError() {
    const grid = document.getElementById('projectsGrid');
    if (!grid) return;

    grid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 3rem;">
            <p style="color: var(--text-secondary); font-size: 1.1rem;">
                Erro ao carregar projetos. Por favor, tente novamente mais tarde.
            </p>
        </div>
    `;
}

/**
 * Filtra projetos por categoria
 */
function filterProjects(category) {
    if (category === 'all' || category === 'todos') {
        renderProjects(allProjects);
        updateProjectCount(allProjects.length);
    } else {
        const filtered = allProjects.filter(p => p.categoria === category);
        renderProjects(filtered);
        updateProjectCount(filtered.length);
    }
}

/**
 * Busca projetos por texto
 */
function searchProjects(query) {
    const lowerQuery = query.toLowerCase();
    const filtered = allProjects.filter(project => 
        project.titulo.toLowerCase().includes(lowerQuery) ||
        project.descricao.toLowerCase().includes(lowerQuery) ||
        (project.localizacao && project.localizacao.toLowerCase().includes(lowerQuery))
    );
    renderProjects(filtered);
}

/**
 * Inicialização quando o DOM estiver pronto
 */
document.addEventListener('DOMContentLoaded', () => {
    // Carrega projetos
    loadProjects();

    // Event listeners do lightbox
    const lightboxClose = document.querySelector('.lightbox-close');
    const lightboxPrev = document.querySelector('.lightbox-prev');
    const lightboxNext = document.querySelector('.lightbox-next');
    const lightbox = document.getElementById('lightbox');

    if (lightboxClose) {
        lightboxClose.addEventListener('click', closeLightbox);
    }

    if (lightboxPrev) {
        lightboxPrev.addEventListener('click', prevImage);
    }

    if (lightboxNext) {
        lightboxNext.addEventListener('click', nextImage);
    }

    // Fechar ao clicar fora do conteúdo
    if (lightbox) {
        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) {
                closeLightbox();
            }
        });
    }

    // Navegação por teclado
    document.addEventListener('keydown', (e) => {
        if (!currentProject) return;

        if (e.key === 'Escape') {
            closeLightbox();
        } else if (e.key === 'ArrowLeft') {
            prevImage();
        } else if (e.key === 'ArrowRight') {
            nextImage();
        }
    });

    // Event listeners para filtros (se existirem)
    const filterButtons = document.querySelectorAll('[data-filter]');
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            const category = button.getAttribute('data-filter');
            filterProjects(category);

            // Atualiza estado ativo
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
        });
    });

    // Event listener para busca (se existir)
    const searchInput = document.querySelector('.search-input');
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            searchProjects(e.target.value);
        });
    }
});
