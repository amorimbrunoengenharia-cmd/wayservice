import json

# Template HTML para páginas de galeria
TEMPLATE = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo} | Way Service</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        /* Header Navigation Container */
        .page-navigation {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: rgba(30, 31, 39, 0.95);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(67, 228, 86, 0.2);
            padding: 1rem 2rem;
            z-index: 100;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        }}

        .back-button {{
            padding: 0.625rem 1.25rem;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(67, 228, 86, 0.3);
            color: #43e456;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.95rem;
            font-weight: 500;
        }}

        .back-button:hover {{
            background: #43e456;
            color: #1E1F27;
            transform: translateX(-5px);
            box-shadow: 0 0 24px rgba(67, 228, 86, 0.4);
        }}

        .header-badge {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.6rem 1rem;
            background: rgba(100, 120, 180, 0.2);
            border: 1px solid rgba(100, 120, 180, 0.4);
            color: rgba(150, 170, 220, 1);
            border-radius: 20px;
            font-size: 0.85rem;
        }}

        .gallery-page {{
            min-height: 100vh;
            background: linear-gradient(135deg, #1E1F27 0%, #0F1014 100%);
            padding-top: 6rem;
            padding-bottom: 2rem;
        }}

        .gallery-header {{
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem 1.5rem 3rem;
            text-align: center;
        }}

        .gallery-header h1 {{
            color: #43e456;
            font-size: 2.8rem;
            margin-bottom: 1.5rem;
            font-weight: 800;
            line-height: 1.2;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            letter-spacing: -0.02em;
        }}

        .gallery-info {{
            color: rgba(255, 255, 255, 0.85);
            font-size: 1.1rem;
            margin-bottom: 1.5rem;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
            line-height: 1.8;
            text-align: justify;
        }}

        .gallery-details {{
            display: flex;
            gap: 3rem;
            justify-content: center;
            margin-top: 2rem;
        }}

        .gallery-details span {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            color: rgba(255, 255, 255, 0.9);
            font-size: 1rem;
            font-weight: 500;
        }}

        .gallery-details svg {{
            color: #43e456;
            width: 20px;
            height: 20px;
        }}

        .gallery-grid {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 1.5rem;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 3rem;
        }}

        .gallery-item {{
            position: relative;
            aspect-ratio: 16/9;
            border-radius: 12px;
            overflow: hidden;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            background: rgba(255, 255, 255, 0.03);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        }}

        .gallery-item:hover {{
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(67, 228, 86, 0.3);
        }}

        .gallery-item::before {{
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, rgba(67, 228, 86, 0.1) 0%, transparent 100%);
            opacity: 0;
            transition: opacity 0.4s ease;
            z-index: 1;
            pointer-events: none;
        }}

        .gallery-item:hover::before {{
            opacity: 1;
        }}

        .gallery-item img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        .gallery-item:hover img {{
            transform: scale(1.05);
            filter: brightness(1.1);
        }}

        .lightbox {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.95);
            z-index: 9999;
        }}

        .lightbox.active {{
            display: flex;
        }}

        .lightbox-content {{
            display: flex;
            width: 100%;
            height: 100%;
            position: relative;
        }}

        .lightbox-image-wrapper {{
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 4rem 2rem;
        }}

        .lightbox-image {{
            max-width: 100%;
            max-height: 90vh;
            object-fit: contain;
        }}

        .lightbox-info {{
            width: 400px;
            background: rgba(26, 26, 46, 0.95);
            backdrop-filter: blur(10px);
            padding: 2rem;
            overflow-y: auto;
            border-left: 1px solid rgba(67, 228, 86, 0.2);
        }}

        .lightbox-info h3 {{
            color: #43e456;
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }}

        .lightbox-info .acervo-badge {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.6rem 1rem;
            background: rgba(100, 120, 180, 0.2);
            border: 1px solid rgba(100, 120, 180, 0.4);
            color: rgba(150, 170, 220, 1);
            border-radius: 20px;
            font-size: 0.85rem;
            margin-bottom: 2rem;
        }}

        .lightbox-info p {{
            color: rgba(255, 255, 255, 0.7);
            line-height: 1.6;
            margin-bottom: 1.5rem;
        }}

        .lightbox-details {{
            display: flex;
            flex-direction: column;
            gap: 0.8rem;
        }}

        .lightbox-details span {{
            color: rgba(255, 255, 255, 0.6);
            font-size: 0.95rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .lightbox-details svg {{
            color: #43e456;
            flex-shrink: 0;
        }}

        .lightbox-close, .lightbox-prev, .lightbox-next {{
            position: absolute;
            background: rgba(67, 228, 86, 0.2);
            border: 1px solid rgba(67, 228, 86, 0.4);
            color: #43e456;
            padding: 1rem;
            border-radius: 50%;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 1.5rem;
            width: 50px;
            height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .lightbox-close:hover, .lightbox-prev:hover, .lightbox-next:hover {{
            background: rgba(67, 228, 86, 0.4);
            transform: scale(1.1);
        }}

        .lightbox-close {{
            top: 2rem;
            right: 2rem;
        }}

        .lightbox-prev {{
            left: 2rem;
            top: 50%;
            transform: translateY(-50%);
        }}

        .lightbox-next {{
            right: 2rem;
            top: 50%;
            transform: translateY(-50%);
        }}

        .lightbox-counter {{
            position: absolute;
            bottom: 2rem;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0, 0, 0, 0.8);
            color: #43e456;
            padding: 0.6rem 1.2rem;
            border-radius: 20px;
            font-size: 0.95rem;
            font-weight: 600;
        }}

        /* Card do Engenheiro Responsável */
        .engineer-card {{
            max-width: 600px;
            margin: 0 auto 3rem;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid #333;
            border-radius: 16px;
            padding: 2rem;
            backdrop-filter: blur(10px);
            display: flex;
            align-items: center;
            gap: 1.5rem;
            transition: all 0.3s ease;
        }}

        .engineer-card:hover {{
            border-color: rgba(67, 228, 86, 0.5);
            transform: translateY(-2px);
            box-shadow: 0 8px 32px rgba(67, 228, 86, 0.15);
        }}

        .engineer-avatar {{
            width: 80px;
            height: 80px;
            border-radius: 50%;
            background: linear-gradient(135deg, rgba(67, 228, 86, 0.2), rgba(100, 120, 180, 0.2));
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            border: 2px solid rgba(67, 228, 86, 0.3);
        }}

        .engineer-avatar svg {{
            color: #43e456;
            width: 40px;
            height: 40px;
        }}

        .engineer-info {{
            flex: 1;
        }}

        .engineer-label {{
            color: rgba(255, 255, 255, 0.5);
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 0.3rem;
        }}

        .engineer-name {{
            color: #43e456;
            font-size: 1.4rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
        }}

        .engineer-role {{
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.95rem;
        }}

        @media (max-width: 768px) {{
            .page-navigation {{
                flex-direction: column;
                gap: 0.8rem;
                padding: 1rem;
            }}

            .gallery-page {{
                padding-top: 8rem;
            }}

            .gallery-header h1 {{
                font-size: 2rem;
            }}

            .gallery-details {{
                flex-direction: column;
                gap: 1rem;
            }}

            .gallery-grid {{
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                gap: 1rem;
            }}

            .lightbox-content {{
                flex-direction: column;
            }}

            .lightbox-info {{
                width: 100%;
                max-height: 40vh;
            }}

            .lightbox-image-wrapper {{
                padding: 2rem 1rem;
            }}

            .engineer-card {{
                flex-direction: column;
                text-align: center;
                padding: 1.5rem;
            }}
        }}
    </style>
</head>
<body>
    <nav class="page-navigation">
        <a href="projetos.html" class="back-button">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M19 12H5M12 19l-7-7 7-7"/>
            </svg>
            Voltar aos Projetos
        </a>
        {header_badge}
    </nav>

    <div class="gallery-page">
        <div class="gallery-header">
            <h1>{titulo}</h1>
            <p class="gallery-info">{descricao}</p>
            <div class="gallery-details">
                {detalhes}
            </div>
        </div>

        {engineer_card}

        <div class="gallery-grid" id="galleryGrid"></div>
    </div>

    <div id="lightbox" class="lightbox">
        <button class="lightbox-close" onclick="closeLightbox()">✕</button>
        <button class="lightbox-prev" onclick="changeImage(-1)">‹</button>
        <button class="lightbox-next" onclick="changeImage(1)">›</button>
        <div class="lightbox-content">
            <div class="lightbox-image-wrapper">
                <img id="lightboxImage" class="lightbox-image" src="" alt="">
                <div class="lightbox-counter">
                    <span id="currentIndex">1</span> / <span id="totalImages">{total_fotos}</span>
                </div>
            </div>
            <div class="lightbox-info">
                {lightbox_info}
            </div>
        </div>
    </div>

    <script>
        const totalImages = {total_fotos};
        const projectId = '{project_id}';
        let currentImageIndex = 0;

        const galleryGrid = document.getElementById('galleryGrid');
        for (let i = 1; i <= totalImages; i++) {{
            const item = document.createElement('div');
            item.className = 'gallery-item';
            item.innerHTML = `
                <img src="img/${{projectId}}/foto${{i}}.jpg" alt="Foto ${{i}}" loading="lazy">
            `;
            item.onclick = () => openLightbox(i - 1);
            galleryGrid.appendChild(item);
        }}

        function openLightbox(index) {{
            currentImageIndex = index;
            updateLightboxImage();
            document.getElementById('lightbox').classList.add('active');
            document.body.style.overflow = 'hidden';
        }}

        function closeLightbox() {{
            document.getElementById('lightbox').classList.remove('active');
            document.body.style.overflow = '';
        }}

        function changeImage(direction) {{
            currentImageIndex = (currentImageIndex + direction + totalImages) % totalImages;
            updateLightboxImage();
        }}

        function updateLightboxImage() {{
            const img = document.getElementById('lightboxImage');
            img.src = `img/${{projectId}}/foto${{currentImageIndex + 1}}.jpg`;
            document.getElementById('currentIndex').textContent = currentImageIndex + 1;
        }}

        document.addEventListener('keydown', (e) => {{
            if (document.getElementById('lightbox').classList.contains('active')) {{
                if (e.key === 'Escape') closeLightbox();
                if (e.key === 'ArrowLeft') changeImage(-1);
                if (e.key === 'ArrowRight') changeImage(1);
            }}
        }});
    </script>
</body>
</html>
'''

# Carregar JSON
with open('projetos.json', 'r', encoding='utf-8') as f:
    projetos = json.load(f)

# Gerar página para cada projeto
for projeto in projetos:
    project_id = projeto['id']
    titulo = projeto['titulo']
    descricao = projeto['descricao']
    total_fotos = len(projeto['galeria'])
    
    # Badge de acervo técnico para header
    header_badge = ''
    # Badge de acervo técnico para lightbox
    lightbox_acervo = ''
    if projeto.get('tipo_autoria') == 'acervo_pessoal':
        responsavel = projeto.get('responsavel_tecnico', 'Acervo Técnico')
        header_badge = f'''<div class="header-badge">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
                <circle cx="9" cy="7" r="4"></circle>
                <polyline points="16 11 18 13 22 9"></polyline>
            </svg>
            <span>Gestão de Execução: {responsavel}</span>
        </div>'''
        lightbox_acervo = f'''<div class="acervo-badge">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
                        <circle cx="9" cy="7" r="4"></circle>
                        <polyline points="16 11 18 13 22 9"></polyline>
                    </svg>
                    <span>Gestão de Execução: {responsavel}</span>
                </div>'''
    
    # Card do Engenheiro Responsável
    engineer_card = ''
    if projeto.get('responsavel_tecnico'):
        responsavel_nome = projeto.get('responsavel_tecnico')
        tipo_autoria = projeto.get('tipo_autoria')
        
        if tipo_autoria == 'acervo_pessoal':
            role_label = 'Engenheiro Responsável'
        else:
            role_label = 'Engenheiro Responsável pela Execução'
        
        engineer_card = f'''<div class="engineer-card">
            <div class="engineer-avatar">
                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                    <circle cx="12" cy="7" r="4"></circle>
                </svg>
            </div>
            <div class="engineer-info">
                <div class="engineer-label">Gestão de Execução</div>
                <div class="engineer-name">{responsavel_nome}</div>
                <div class="engineer-role">{role_label}</div>
            </div>
        </div>'''
    
    # Detalhes com ícones SVG modernos
    detalhes_list = []
    lightbox_detalhes_list = []
    if projeto.get('localizacao'):
        detalhes_list.append(f'''<span>
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                        <circle cx="12" cy="10" r="3"></circle>
                    </svg>
                    {projeto["localizacao"]}
                </span>''')
        lightbox_detalhes_list.append(f'''<span>
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                            <circle cx="12" cy="10" r="3"></circle>
                        </svg>
                        {projeto["localizacao"]}
                    </span>''')
    if projeto.get('area'):
        detalhes_list.append(f'''<span>
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="3" y1="9" x2="21" y2="9"></line>
                        <line x1="9" y1="21" x2="9" y2="9"></line>
                    </svg>
                    {projeto["area"]}
                </span>''')
        lightbox_detalhes_list.append(f'''<span>
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                            <line x1="3" y1="9" x2="21" y2="9"></line>
                            <line x1="9" y1="21" x2="9" y2="9"></line>
                        </svg>
                        {projeto["area"]}
                    </span>''')
    if projeto.get('ano'):
        detalhes_list.append(f'''<span>
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="16" y1="2" x2="16" y2="6"></line>
                        <line x1="8" y1="2" x2="8" y2="6"></line>
                        <line x1="3" y1="10" x2="21" y2="10"></line>
                    </svg>
                    {projeto["ano"]}
                </span>''')
        lightbox_detalhes_list.append(f'''<span>
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                            <line x1="16" y1="2" x2="16" y2="6"></line>
                            <line x1="8" y1="2" x2="8" y2="6"></line>
                            <line x1="3" y1="10" x2="21" y2="10"></line>
                        </svg>
                        {projeto["ano"]}
                    </span>''')
    
    # Adicionar contador de fotos com ícone
    detalhes_list.append(f'''<span>
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="18" height="18" rx="2"></rect>
                        <circle cx="9" cy="9" r="2"></circle>
                        <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
                    </svg>
                    {total_fotos} fotos
                </span>''')
    
    detalhes = '\n                '.join(detalhes_list)
    
    # Informações do lightbox (sem badge - já está no header)
    lightbox_detalhes = '\n                    '.join(lightbox_detalhes_list)
    lightbox_info = f'''<h3>{titulo}</h3>
                <p>{descricao}</p>
                <div class="lightbox-details">
                    {lightbox_detalhes}
                </div>'''
    
    # Gerar HTML
    html = TEMPLATE.format(
        titulo=titulo,
        descricao=descricao,
        total_fotos=total_fotos,
        project_id=project_id,
        header_badge=header_badge,
        engineer_card=engineer_card,
        detalhes=detalhes,
        lightbox_info=lightbox_info
    )
    
    # Salvar arquivo
    filename = f'projeto-{project_id}.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f'✓ Criado: {filename} ({total_fotos} fotos)')

print(f'\n✅ {len(projetos)} páginas de galeria criadas com sucesso!')
