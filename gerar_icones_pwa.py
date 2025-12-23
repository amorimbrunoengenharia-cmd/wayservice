#!/usr/bin/env python3
"""
Script para criar ícones PWA em múltiplos tamanhos
Gera 192x192 e 512x512 a partir do logo Ativo 2.png
"""

from PIL import Image, ImageDraw
import os

# Configurações
logo_path = "logo/Ativo 2.png"
output_dir = "logo/pwa"
sizes = [192, 512]

# Criar diretório de saída
os.makedirs(output_dir, exist_ok=True)

def create_pwa_icon(size):
    """Cria ícone PWA com fundo e logo centralizado"""
    # Criar canvas com fundo
    icon = Image.new('RGB', (size, size), color='#1E1F27')
    
    # Abrir logo original
    logo = Image.open(logo_path)
    
    # Calcular tamanho do logo (70% do ícone)
    logo_size = int(size * 0.7)
    
    # Redimensionar logo mantendo proporção
    logo.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)
    
    # Calcular posição para centralizar
    x = (size - logo.width) // 2
    y = (size - logo.height) // 2
    
    # Colar logo no canvas (com transparência se houver)
    if logo.mode == 'RGBA':
        icon.paste(logo, (x, y), logo)
    else:
        icon.paste(logo, (x, y))
    
    # Salvar
    output_path = os.path.join(output_dir, f"icon-{size}x{size}.png")
    icon.save(output_path, "PNG", optimize=True)
    
    print(f"✅ Criado: {output_path}")
    return output_path

def create_maskable_icon(size):
    """Cria ícone maskable com safe zone"""
    # Canvas maior para safe zone
    canvas_size = int(size * 1.2)
    icon = Image.new('RGB', (canvas_size, canvas_size), color='#43E456')
    
    # Círculo de fundo verde
    draw = ImageDraw.Draw(icon)
    draw.ellipse([0, 0, canvas_size, canvas_size], fill='#43E456')
    
    # Abrir logo
    logo = Image.open(logo_path)
    
    # Logo menor para safe zone (50% do canvas)
    logo_size = int(canvas_size * 0.5)
    logo.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)
    
    # Centralizar logo
    x = (canvas_size - logo.width) // 2
    y = (canvas_size - logo.height) // 2
    
    # Colar logo
    if logo.mode == 'RGBA':
        icon.paste(logo, (x, y), logo)
    else:
        icon.paste(logo, (x, y))
    
    # Redimensionar para tamanho final
    icon = icon.resize((size, size), Image.Resampling.LANCZOS)
    
    # Salvar
    output_path = os.path.join(output_dir, f"icon-maskable-{size}x{size}.png")
    icon.save(output_path, "PNG", optimize=True)
    
    print(f"✅ Criado: {output_path} (maskable)")
    return output_path

def main():
    """Função principal"""
    print("🎨 GERADOR DE ÍCONES PWA")
    print("=" * 50)
    
    if not os.path.exists(logo_path):
        print(f"❌ Logo não encontrado: {logo_path}")
        return
    
    print(f"Logo: {logo_path}\n")
    
    for size in sizes:
        create_pwa_icon(size)
        create_maskable_icon(size)
    
    print("\n" + "=" * 50)
    print("✅ Ícones PWA criados com sucesso!")
    print(f"\n📁 Diretório: {output_dir}/")
    print("\n⚠️  Atualizar manifest.json com os novos ícones:")
    print('   "icons": [')
    for size in sizes:
        print(f'     {{ "src": "logo/pwa/icon-{size}x{size}.png", "sizes": "{size}x{size}", "type": "image/png" }},')
        print(f'     {{ "src": "logo/pwa/icon-maskable-{size}x{size}.png", "sizes": "{size}x{size}", "type": "image/png", "purpose": "maskable" }},')
    print('   ]')

if __name__ == "__main__":
    main()
