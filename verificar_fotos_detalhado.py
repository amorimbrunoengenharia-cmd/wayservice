#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script avançado para verificar fotos dos projetos
- Verifica se imagens são válidas (não corrompidas)
- Detecta duplicatas por conteúdo (hash MD5)
- Remove fotos inexistentes
- Lista fotos no disco que não estão no JSON
"""

import json
import os
import hashlib
from pathlib import Path
from PIL import Image

def calcular_hash(caminho_arquivo):
    """Calcula hash MD5 do arquivo para detectar duplicatas"""
    try:
        with open(caminho_arquivo, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except Exception as e:
        return None

def verificar_imagem_valida(caminho_arquivo):
    """Verifica se a imagem pode ser aberta e não está corrompida"""
    try:
        with Image.open(caminho_arquivo) as img:
            img.verify()
        # Reabrir para verificar se realmente funciona
        with Image.open(caminho_arquivo) as img:
            img.load()
        return True
    except Exception:
        return False

def listar_fotos_no_disco(pasta_projeto):
    """Lista todas as fotos JPG/JPEG na pasta do projeto"""
    fotos = []
    if os.path.exists(pasta_projeto):
        for arquivo in os.listdir(pasta_projeto):
            if arquivo.lower().endswith(('.jpg', '.jpeg')):
                fotos.append(os.path.join(pasta_projeto, arquivo))
    return sorted(fotos)

def verificar_e_atualizar_projetos():
    """Verifica fotos com análise profunda e atualiza projetos.json"""
    
    # Carregar projetos.json
    with open('projetos.json', 'r', encoding='utf-8') as f:
        projetos = json.load(f)
    
    print("=" * 80)
    print("ANÁLISE DETALHADA DE FOTOS DOS PROJETOS")
    print("=" * 80)
    
    total_projetos = len(projetos)
    total_fotos_antes = 0
    total_fotos_depois = 0
    total_removidas_inexistentes = 0
    total_removidas_corrompidas = 0
    total_removidas_duplicadas = 0
    
    for projeto in projetos:
        projeto_id = projeto['id']
        titulo = projeto['titulo']
        galeria_antes = projeto.get('galeria', [])
        total_fotos_antes += len(galeria_antes)
        
        print(f"\n{'─' * 80}")
        print(f"📁 Projeto: {titulo}")
        print(f"   ID: {projeto_id}")
        print(f"   Fotos listadas no JSON: {len(galeria_antes)}")
        
        # Verificar cada foto
        fotos_validas = []
        fotos_inexistentes = []
        fotos_corrompidas = []
        hashes_vistos = {}
        fotos_duplicadas_hash = []
        
        for foto_path in galeria_antes:
            # Verificar se existe
            if not os.path.exists(foto_path):
                fotos_inexistentes.append(foto_path)
                continue
            
            # Verificar se é válida
            if not verificar_imagem_valida(foto_path):
                fotos_corrompidas.append(foto_path)
                continue
            
            # Calcular hash para detectar duplicatas
            hash_foto = calcular_hash(foto_path)
            if hash_foto:
                if hash_foto in hashes_vistos:
                    fotos_duplicadas_hash.append({
                        'duplicata': foto_path,
                        'original': hashes_vistos[hash_foto]
                    })
                    continue
                hashes_vistos[hash_foto] = foto_path
            
            fotos_validas.append(foto_path)
        
        # Verificar fotos no disco que não estão no JSON
        pasta_img = f"img/{projeto_id}"
        fotos_no_disco = listar_fotos_no_disco(pasta_img)
        fotos_nao_listadas = [f for f in fotos_no_disco if f not in galeria_antes and f != f"img/{projeto_id}/capa.jpg"]
        
        # Contabilizar removidas
        num_inexistentes = len(fotos_inexistentes)
        num_corrompidas = len(fotos_corrompidas)
        num_duplicadas = len(fotos_duplicadas_hash)
        
        total_removidas_inexistentes += num_inexistentes
        total_removidas_corrompidas += num_corrompidas
        total_removidas_duplicadas += num_duplicadas
        
        # Atualizar galeria do projeto
        projeto['galeria'] = fotos_validas
        total_fotos_depois += len(fotos_validas)
        
        # Exibir resultados
        print(f"   ✅ Fotos válidas mantidas: {len(fotos_validas)}")
        
        if fotos_inexistentes:
            print(f"   ❌ Fotos NÃO ENCONTRADAS no disco: {num_inexistentes}")
            for foto in fotos_inexistentes[:5]:  # Mostrar apenas as 5 primeiras
                print(f"      - {foto}")
            if len(fotos_inexistentes) > 5:
                print(f"      ... e mais {len(fotos_inexistentes) - 5} fotos")
        
        if fotos_corrompidas:
            print(f"   ⚠️  Fotos CORROMPIDAS (não podem ser abertas): {num_corrompidas}")
            for foto in fotos_corrompidas:
                print(f"      - {foto}")
        
        if fotos_duplicadas_hash:
            print(f"   🔄 Fotos DUPLICADAS (mesmo conteúdo): {num_duplicadas}")
            for dup in fotos_duplicadas_hash[:5]:  # Mostrar apenas as 5 primeiras
                print(f"      - {dup['duplicata']}")
                print(f"        (idêntica a {dup['original']})")
            if len(fotos_duplicadas_hash) > 5:
                print(f"      ... e mais {len(fotos_duplicadas_hash) - 5} duplicatas")
        
        if fotos_nao_listadas:
            print(f"   ℹ️  Fotos NO DISCO mas NÃO no JSON: {len(fotos_nao_listadas)}")
            for foto in fotos_nao_listadas[:5]:  # Mostrar apenas as 5 primeiras
                print(f"      - {foto}")
            if len(fotos_nao_listadas) > 5:
                print(f"      ... e mais {len(fotos_nao_listadas) - 5} fotos")
        
        print(f"   📊 Total após limpeza: {len(fotos_validas)} fotos")
        
        if num_inexistentes + num_corrompidas + num_duplicadas > 0:
            print(f"   ⚙️  Removidas: {num_inexistentes + num_corrompidas + num_duplicadas} fotos")
    
    # Salvar projetos.json atualizado
    with open('projetos.json', 'w', encoding='utf-8') as f:
        json.dump(projetos, f, ensure_ascii=False, indent=2)
    
    # Resumo final
    print(f"\n{'=' * 80}")
    print("RESUMO DA ANÁLISE DETALHADA")
    print("=" * 80)
    print(f"Total de projetos analisados: {total_projetos}")
    print(f"Total de fotos antes: {total_fotos_antes}")
    print(f"Total de fotos depois: {total_fotos_depois}")
    print(f"\nFotos removidas por categoria:")
    print(f"  - Inexistentes no disco: {total_removidas_inexistentes}")
    print(f"  - Corrompidas/inválidas: {total_removidas_corrompidas}")
    print(f"  - Duplicadas (mesmo conteúdo): {total_removidas_duplicadas}")
    print(f"  TOTAL REMOVIDO: {total_removidas_inexistentes + total_removidas_corrompidas + total_removidas_duplicadas}")
    
    if total_fotos_antes != total_fotos_depois:
        print(f"\n✅ Arquivo projetos.json ATUALIZADO com sucesso!")
    else:
        print(f"\n✅ Nenhuma alteração necessária - todos os álbuns estão corretos!")
    print("=" * 80)

if __name__ == '__main__':
    try:
        verificar_e_atualizar_projetos()
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        import traceback
        traceback.print_exc()
