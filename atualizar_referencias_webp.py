"""
Atualizador Automático de Referências para WebP
Atualiza todos os arquivos HTML e CSS substituindo .jpg/.png por .webp
"""

import os
import re
from pathlib import Path

def atualizar_arquivo(caminho_arquivo):
    """
    Atualiza as referências de imagens em um arquivo
    """
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        conteudo_original = conteudo
        
        # Substitui extensões de imagem por .webp
        # Padrões: .jpg, .jpeg, .png (case insensitive)
        conteudo = re.sub(r'\.(jpg|jpeg|png)', '.webp', conteudo, flags=re.IGNORECASE)
        
        # Conta quantas substituições foram feitas
        if conteudo != conteudo_original:
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                f.write(conteudo)
            
            mudancas = len(re.findall(r'\.webp', conteudo)) - len(re.findall(r'\.webp', conteudo_original))
            return True, mudancas
        
        return False, 0
        
    except Exception as e:
        print(f"❌ Erro ao processar {caminho_arquivo}: {e}")
        return False, 0

def processar_workspace(diretorio_base):
    """
    Processa todos os arquivos HTML e CSS do workspace
    """
    extensoes_alvo = ['.html', '.css', '.js', '.json']
    
    print("=" * 80)
    print("🔄 ATUALIZADOR DE REFERÊNCIAS PARA WEBP")
    print("=" * 80)
    print(f"📁 Diretório: {diretorio_base}")
    print("🎯 Arquivos alvo: HTML, CSS, JS, JSON")
    print("=" * 80)
    print()
    
    arquivos_atualizados = 0
    total_mudancas = 0
    
    # Processa arquivos no diretório raiz
    for arquivo in os.listdir(diretorio_base):
        if any(arquivo.endswith(ext) for ext in extensoes_alvo):
            caminho_completo = os.path.join(diretorio_base, arquivo)
            
            if os.path.isfile(caminho_completo):
                sucesso, mudancas = atualizar_arquivo(caminho_completo)
                
                if sucesso:
                    print(f"✅ {arquivo}")
                    print(f"   → {mudancas} referência(s) atualizada(s)")
                    arquivos_atualizados += 1
                    total_mudancas += mudancas
    
    # Resumo
    print("\n" + "=" * 80)
    print("📊 RESUMO DA ATUALIZAÇÃO")
    print("=" * 80)
    print(f"✅ Arquivos atualizados: {arquivos_atualizados}")
    print(f"🔄 Total de referências mudadas: {total_mudancas}")
    print("\n💡 PRÓXIMOS PASSOS:")
    print("   1. Teste o site localmente (abra index.html no navegador)")
    print("   2. Verifique se todas as imagens estão carregando corretamente")
    print("   3. Faça commit: git add . && git commit -m 'Otimização: imagens convertidas para WebP'")
    print("   4. Deploy: git push")
    print("   5. Teste no Google PageSpeed Insights (https://pagespeed.web.dev/)")
    print("=" * 80)

if __name__ == "__main__":
    diretorio_atual = Path(__file__).parent
    processar_workspace(diretorio_atual)
    
    print("\n✅ Atualização concluída!")
