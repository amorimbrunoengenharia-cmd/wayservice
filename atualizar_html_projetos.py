#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para atualizar os arquivos HTML dos projetos com as fotos corretas do projetos.json
Remove o sistema de contador simples e usa a lista exata de fotos
"""

import json
import re
from pathlib import Path

def atualizar_html_projeto(projeto):
    """Atualiza o arquivo HTML de um projeto com a lista correta de fotos"""
    
    projeto_id = projeto['id']
    html_file = f"projeto-{projeto_id}.html"
    
    if not Path(html_file).exists():
        print(f"⚠️  Arquivo {html_file} não existe - pulando")
        return False
    
    # Ler o arquivo HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Extrair lista de fotos do projeto
    fotos = projeto.get('galeria', [])
    num_fotos = len(fotos)
    
    # Criar lista de fotos em formato JavaScript
    fotos_js_list = ',\n            '.join([f'"{foto}"' for foto in fotos])
    
    # Novo script JavaScript
    novo_script = f'''    <script>
        const images = [
            {fotos_js_list}
        ];
        
        const totalImages = images.length;
        const projectId = '{projeto_id}';
        let currentImageIndex = 0;

        const galleryGrid = document.getElementById('galleryGrid');
        images.forEach((imagePath, index) => {{
            const item = document.createElement('div');
            item.className = 'gallery-item';
            item.innerHTML = `
                <img src="${{imagePath}}" alt="Foto ${{index + 1}}" loading="lazy" onerror="this.parentElement.style.display='none'">
            `;
            item.onclick = () => openLightbox(index);
            galleryGrid.appendChild(item);
        }});

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
            img.src = images[currentImageIndex];
            document.getElementById('currentIndex').textContent = currentImageIndex + 1;
        }}

        document.addEventListener('keydown', (e) => {{
            if (document.getElementById('lightbox').classList.contains('active')) {{
                if (e.key === 'Escape') closeLightbox();
                if (e.key === 'ArrowLeft') changeImage(-1);
                if (e.key === 'ArrowRight') changeImage(1);
            }}
        }});
    </script>'''
    
    # Atualizar o totalImages no contador do lightbox
    html_content = re.sub(
        r'<span id="totalImages">\d+</span>',
        f'<span id="totalImages">{num_fotos}</span>',
        html_content
    )
    
    # Substituir o script antigo pelo novo
    # Procurar pelo padrão do script com totalImages e projectId
    pattern = r'<script>\s*const totalImages = \d+;.*?</script>'
    
    if re.search(pattern, html_content, re.DOTALL):
        html_content = re.sub(pattern, novo_script, html_content, flags=re.DOTALL)
        
        # Salvar o arquivo atualizado
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return True
    else:
        print(f"⚠️  Padrão de script não encontrado em {html_file}")
        return False

def atualizar_todos_projetos():
    """Atualiza todos os arquivos HTML dos projetos"""
    
    # Carregar projetos.json
    with open('projetos.json', 'r', encoding='utf-8') as f:
        projetos = json.load(f)
    
    print("=" * 80)
    print("ATUALIZANDO ARQUIVOS HTML DOS PROJETOS")
    print("=" * 80)
    
    total_atualizados = 0
    total_projetos = len(projetos)
    
    for projeto in projetos:
        projeto_id = projeto['id']
        titulo = projeto['titulo']
        num_fotos = len(projeto.get('galeria', []))
        
        print(f"\n📄 Atualizando: {titulo}")
        print(f"   ID: {projeto_id}")
        print(f"   Fotos: {num_fotos}")
        
        if atualizar_html_projeto(projeto):
            print(f"   ✅ Atualizado com sucesso!")
            total_atualizados += 1
        else:
            print(f"   ❌ Falha na atualização")
    
    print(f"\n{'=' * 80}")
    print(f"RESUMO")
    print("=" * 80)
    print(f"Total de projetos: {total_projetos}")
    print(f"Arquivos HTML atualizados: {total_atualizados}")
    print(f"✅ Concluído!")
    print("=" * 80)

if __name__ == '__main__':
    try:
        atualizar_todos_projetos()
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        import traceback
        traceback.print_exc()
