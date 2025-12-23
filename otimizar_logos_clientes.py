#!/usr/bin/env python3
"""
Script para otimizar logos de clientes
Redimensiona imagens para as dimensões apropriadas (210px largura)
"""

from PIL import Image
import os

# Diretório dos logos
logos_dir = "logo/clientes"

# Dimensões desejadas (largura fixa de 210px, altura proporcional)
target_width = 210

# Lista de logos para otimizar
logos = {
    "raizen.png": 87,        # Altura proporcional para 210px largura
    "governo_sp.png": 79,
    "petrobras.png": 42,
    "cocamar.png": 48,
    "belagricola.png": 86,
    "jbs.png": 90
}

def otimizar_logo(filename, target_height):
    """Redimensiona e otimiza um logo"""
    filepath = os.path.join(logos_dir, filename)
    
    if not os.path.exists(filepath):
        print(f"❌ Arquivo não encontrado: {filepath}")
        return
    
    try:
        # Abrir imagem
        img = Image.open(filepath)
        original_size = img.size
        original_file_size = os.path.getsize(filepath) / 1024  # KB
        
        # Redimensionar mantendo proporção
        img_resized = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
        
        # Salvar otimizado (substituir original)
        # PNG com otimização
        img_resized.save(filepath, "PNG", optimize=True, quality=85)
        
        new_file_size = os.path.getsize(filepath) / 1024  # KB
        reduction = ((original_file_size - new_file_size) / original_file_size) * 100
        
        print(f"✅ {filename}")
        print(f"   Antes: {original_size[0]}x{original_size[1]} ({original_file_size:.1f} KB)")
        print(f"   Depois: {target_width}x{target_height} ({new_file_size:.1f} KB)")
        print(f"   Economia: {reduction:.1f}%\n")
        
    except Exception as e:
        print(f"❌ Erro ao processar {filename}: {e}\n")

def main():
    """Função principal"""
    print("🖼️  OTIMIZADOR DE LOGOS DE CLIENTES")
    print("=" * 50)
    print(f"Dimensão alvo: {target_width}px de largura\n")
    
    total_before = 0
    total_after = 0
    
    for filename, height in logos.items():
        filepath = os.path.join(logos_dir, filename)
        if os.path.exists(filepath):
            total_before += os.path.getsize(filepath) / 1024
        
        otimizar_logo(filename, height)
        
        if os.path.exists(filepath):
            total_after += os.path.getsize(filepath) / 1024
    
    print("=" * 50)
    print(f"📊 RESUMO")
    print(f"Tamanho total antes: {total_before:.1f} KB")
    print(f"Tamanho total depois: {total_after:.1f} KB")
    print(f"Economia total: {total_before - total_after:.1f} KB ({((total_before - total_after) / total_before * 100):.1f}%)")
    print("\n✅ Otimização concluída!")
    print("\n⚠️  IMPORTANTE: Faça commit das imagens otimizadas:")
    print("   git add logo/clientes/*.png")
    print("   git commit -m 'Optimize: Redimensionar logos de clientes para 210px'")

if __name__ == "__main__":
    main()
