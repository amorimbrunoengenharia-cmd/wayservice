#!/usr/bin/env python3
"""
Gera favicon.ico multi-tamanho a partir do Ativo 2.png
Cria ícones de 16x16, 32x32, 48x48 para compatibilidade máxima
"""
from PIL import Image
import os

def gerar_favicon():
    """Gera favicon.ico com múltiplos tamanhos"""
    input_path = "logo/Ativo 2.png"
    output_path = "favicon.ico"
    
    if not os.path.exists(input_path):
        print(f"❌ Erro: {input_path} não encontrado")
        return
    
    # Abrir imagem original
    img = Image.open(input_path)
    
    # Converter para RGBA se necessário
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Criar ícones em múltiplos tamanhos
    tamanhos = [(16, 16), (32, 32), (48, 48)]
    icones = []
    
    for tamanho in tamanhos:
        icone = img.resize(tamanho, Image.Resampling.LANCZOS)
        icones.append(icone)
    
    # Salvar como .ico multi-tamanho
    icones[0].save(
        output_path,
        format='ICO',
        sizes=tamanhos,
        append_images=icones[1:]
    )
    
    print(f"✅ Favicon criado: {output_path}")
    print(f"   Tamanhos: 16x16, 32x32, 48x48")
    
    # Verificar tamanho do arquivo
    tamanho_kb = os.path.getsize(output_path) / 1024
    print(f"   Tamanho: {tamanho_kb:.2f} KB")

if __name__ == "__main__":
    gerar_favicon()
