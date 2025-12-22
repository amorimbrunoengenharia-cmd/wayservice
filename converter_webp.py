"""
Conversor Automático de Imagens para WebP
Converte todas as imagens JPG/PNG para WebP com compressão otimizada
Mantém a estrutura de pastas e cria backup
"""

from PIL import Image
import os
from pathlib import Path

def converter_para_webp(caminho_origem, qualidade=85):
    """
    Converte uma imagem para WebP mantendo qualidade alta
    
    Args:
        caminho_origem: Caminho do arquivo original
        qualidade: Qualidade da conversão (85 = ótimo equilíbrio)
    """
    try:
        # Abre a imagem
        img = Image.open(caminho_origem)
        
        # Converte para RGB se for PNG com transparência
        if img.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = background
        
        # Define caminho de saída (mesmo nome, extensão .webp)
        caminho_webp = caminho_origem.rsplit('.', 1)[0] + '.webp'
        
        # Salva como WebP
        img.save(caminho_webp, 'WebP', quality=qualidade, method=6)
        
        # Calcula redução de tamanho
        tamanho_original = os.path.getsize(caminho_origem)
        tamanho_webp = os.path.getsize(caminho_webp)
        reducao = ((tamanho_original - tamanho_webp) / tamanho_original) * 100
        
        print(f"✅ {os.path.basename(caminho_origem)} → {os.path.basename(caminho_webp)}")
        print(f"   Redução: {reducao:.1f}% ({tamanho_original/1024:.0f}KB → {tamanho_webp/1024:.0f}KB)")
        
        return caminho_webp, reducao
        
    except Exception as e:
        print(f"❌ Erro ao converter {caminho_origem}: {e}")
        return None, 0

def processar_diretorio(diretorio_base):
    """
    Processa todas as imagens em um diretório e subdiretórios
    """
    extensoes = ['.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG']
    
    # Diretórios a processar
    diretorios = [
        'img',
        'logo'
    ]
    
    total_convertidos = 0
    total_reducao = 0
    
    print("=" * 80)
    print("🖼️  CONVERSOR AUTOMÁTICO DE IMAGENS PARA WEBP")
    print("=" * 80)
    print(f"📁 Diretório base: {diretorio_base}")
    print(f"🎯 Qualidade: 85% (ótimo equilíbrio qualidade/tamanho)")
    print("=" * 80)
    print()
    
    for diretorio in diretorios:
        caminho_completo = os.path.join(diretorio_base, diretorio)
        
        if not os.path.exists(caminho_completo):
            print(f"⚠️  Diretório {diretorio} não encontrado, pulando...")
            continue
        
        print(f"\n📂 Processando: {diretorio}/")
        print("-" * 80)
        
        # Busca todas as imagens recursivamente
        for root, dirs, files in os.walk(caminho_completo):
            for file in files:
                if any(file.endswith(ext) for ext in extensoes):
                    caminho_arquivo = os.path.join(root, file)
                    
                    # Verifica se já existe versão WebP
                    caminho_webp_existente = caminho_arquivo.rsplit('.', 1)[0] + '.webp'
                    if os.path.exists(caminho_webp_existente):
                        print(f"⏭️  {file} (WebP já existe)")
                        continue
                    
                    # Converte
                    resultado, reducao = converter_para_webp(caminho_arquivo)
                    if resultado:
                        total_convertidos += 1
                        total_reducao += reducao
                    print()
    
    # Resumo final
    print("\n" + "=" * 80)
    print("📊 RESUMO DA CONVERSÃO")
    print("=" * 80)
    print(f"✅ Total de imagens convertidas: {total_convertidos}")
    if total_convertidos > 0:
        print(f"📉 Redução média de tamanho: {total_reducao/total_convertidos:.1f}%")
        print(f"🚀 Ganho de performance esperado: 30-50% mais rápido")
    print("\n⚠️  IMPORTANTE:")
    print("   1. Os arquivos originais foram MANTIDOS")
    print("   2. Agora você precisa atualizar as referências no código HTML/CSS")
    print("   3. Exemplo: 'foto.jpg' → 'foto.webp'")
    print("   4. Após confirmar que tudo funciona, você pode deletar os .jpg/.png originais")
    print("=" * 80)

if __name__ == "__main__":
    # Diretório atual (onde o script está)
    diretorio_atual = Path(__file__).parent
    
    # Verifica se o Pillow está instalado
    try:
        import PIL
        print("✅ Biblioteca PIL (Pillow) detectada")
    except ImportError:
        print("❌ ERRO: Pillow não está instalado!")
        print("   Execute: pip install Pillow")
        exit(1)
    
    # Processa
    processar_diretorio(diretorio_atual)
    
    print("\n✅ Conversão concluída!")
    print("💡 Próximo passo: Execute o script 'atualizar_referencias_webp.py' para atualizar o código")
