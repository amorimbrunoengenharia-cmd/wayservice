"""
Script para otimizar imagens do site, reduzindo tamanho dos arquivos
mantendo qualidade visual aceitável
"""
from PIL import Image
import os
from pathlib import Path

# Configurações
MAX_WIDTH = 1920  # Largura máxima em pixels
MAX_HEIGHT = 1920  # Altura máxima em pixels
QUALITY = 75  # Qualidade JPEG (0-100, recomendado 70-85)

def otimizar_imagem(caminho_original):
    """Otimiza uma imagem JPEG reduzindo tamanho e qualidade"""
    try:
        # Abrir imagem
        img = Image.open(caminho_original)
        
        # Converter para RGB se necessário (remove transparência)
        if img.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
            img = background
        
        # Redimensionar se necessário
        if img.width > MAX_WIDTH or img.height > MAX_HEIGHT:
            img.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.Resampling.LANCZOS)
        
        # Salvar com compressão otimizada
        img.save(caminho_original, 'JPEG', quality=QUALITY, optimize=True, progressive=True)
        
        return True
    except Exception as e:
        print(f"  ⚠ Erro ao otimizar {os.path.basename(caminho_original)}: {e}")
        return False

def otimizar_pasta(pasta):
    """Otimiza todas as imagens JPG em uma pasta"""
    pasta_path = Path(pasta)
    if not pasta_path.exists():
        print(f"⚠ Pasta não encontrada: {pasta}")
        return
    
    # Buscar todas as imagens .jpg
    imagens = list(pasta_path.glob("*.jpg")) + list(pasta_path.glob("*.JPG"))
    
    if not imagens:
        print(f"⚠ Nenhuma imagem encontrada em: {pasta}")
        return
    
    print(f"\n📁 Processando: {pasta_path.name}")
    print(f"   {len(imagens)} imagens encontradas")
    
    # Calcular tamanho total antes
    tamanho_antes = sum(img.stat().st_size for img in imagens)
    
    # Otimizar cada imagem
    sucesso = 0
    for i, imagem in enumerate(imagens, 1):
        if otimizar_imagem(str(imagem)):
            sucesso += 1
        
        # Mostrar progresso a cada 50 imagens
        if i % 50 == 0 or i == len(imagens):
            print(f"   Processadas: {i}/{len(imagens)}")
    
    # Calcular tamanho total depois
    tamanho_depois = sum(img.stat().st_size for img in imagens)
    
    # Mostrar resultados
    economia = tamanho_antes - tamanho_depois
    percentual = (economia / tamanho_antes * 100) if tamanho_antes > 0 else 0
    
    print(f"   ✓ {sucesso} imagens otimizadas")
    print(f"   📉 Antes: {tamanho_antes / (1024*1024):.2f} MB")
    print(f"   📉 Depois: {tamanho_depois / (1024*1024):.2f} MB")
    print(f"   💾 Economia: {economia / (1024*1024):.2f} MB ({percentual:.1f}%)")

def main():
    """Função principal"""
    print("=" * 60)
    print("🖼️  OTIMIZADOR DE IMAGENS")
    print("=" * 60)
    print(f"Configurações:")
    print(f"  - Dimensão máxima: {MAX_WIDTH}x{MAX_HEIGHT}px")
    print(f"  - Qualidade JPEG: {QUALITY}%")
    print("=" * 60)
    
    # Diretório base das imagens
    base_dir = Path(__file__).parent / "img"
    
    # Lista de pastas de projetos
    pastas = [
        "forum-andradina",
        "forum-aracatuba",
        "forum-auriflama",
        "forum-jales",
        "forum-lins",
        "lojas-americanas",
        "monsanto-bayer-itai",
        "petrobras-refinaria",
        "transpetro-aracaju",
        "ufv-pedro-canario",
        "ufv-santa-adelia",
        "ufv-sao-mateus"
    ]
    
    # Processar cada pasta
    tamanho_total_antes = 0
    tamanho_total_depois = 0
    
    for pasta in pastas:
        caminho_pasta = base_dir / pasta
        
        if caminho_pasta.exists():
            # Calcular tamanhos
            imagens = list(caminho_pasta.glob("*.jpg")) + list(caminho_pasta.glob("*.JPG"))
            tamanho_antes = sum(img.stat().st_size for img in imagens)
            tamanho_total_antes += tamanho_antes
            
            # Otimizar
            otimizar_pasta(str(caminho_pasta))
            
            # Calcular tamanho depois
            imagens = list(caminho_pasta.glob("*.jpg")) + list(caminho_pasta.glob("*.JPG"))
            tamanho_depois = sum(img.stat().st_size for img in imagens)
            tamanho_total_depois += tamanho_depois
    
    # Resumo final
    print("\n" + "=" * 60)
    print("📊 RESUMO GERAL")
    print("=" * 60)
    print(f"Tamanho total antes: {tamanho_total_antes / (1024*1024):.2f} MB")
    print(f"Tamanho total depois: {tamanho_total_depois / (1024*1024):.2f} MB")
    economia_total = tamanho_total_antes - tamanho_total_depois
    percentual_total = (economia_total / tamanho_total_antes * 100) if tamanho_total_antes > 0 else 0
    print(f"💾 Economia total: {economia_total / (1024*1024):.2f} MB ({percentual_total:.1f}%)")
    print("=" * 60)
    print("✅ Otimização concluída!")

if __name__ == "__main__":
    main()
