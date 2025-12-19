#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para verificar fotos dos projetos e atualizar projetos.json
Remove fotos inexistentes e duplicadas, atualiza contagem
"""

import json
import os
from pathlib import Path
from collections import Counter

def verificar_e_atualizar_projetos():
    """Verifica fotos e atualiza projetos.json"""
    
    # Carregar projetos.json
    with open('projetos.json', 'r', encoding='utf-8') as f:
        projetos = json.load(f)
    
    print("=" * 80)
    print("VERIFICAÇÃO DE FOTOS DOS PROJETOS")
    print("=" * 80)
    
    total_projetos = len(projetos)
    total_fotos_antes = 0
    total_fotos_depois = 0
    total_removidas = 0
    total_duplicadas = 0
    
    for projeto in projetos:
        projeto_id = projeto['id']
        titulo = projeto['titulo']
        galeria_antes = projeto.get('galeria', [])
        total_fotos_antes += len(galeria_antes)
        
        print(f"\n{'─' * 80}")
        print(f"📁 Projeto: {titulo}")
        print(f"   ID: {projeto_id}")
        print(f"   Fotos no JSON: {len(galeria_antes)}")
        
        # Verificar quais fotos realmente existem
        fotos_validas = []
        fotos_inexistentes = []
        
        for foto_path in galeria_antes:
            if os.path.exists(foto_path):
                fotos_validas.append(foto_path)
            else:
                fotos_inexistentes.append(foto_path)
        
        # Detectar duplicatas
        contador = Counter(galeria_antes)
        duplicadas = [foto for foto, count in contador.items() if count > 1]
        
        # Remover duplicatas mantendo ordem
        fotos_sem_duplicatas = []
        seen = set()
        for foto in fotos_validas:
            if foto not in seen:
                fotos_sem_duplicatas.append(foto)
                seen.add(foto)
        
        # Contar fotos removidas
        num_duplicadas = len(fotos_validas) - len(fotos_sem_duplicatas)
        num_inexistentes = len(fotos_inexistentes)
        
        total_removidas += num_inexistentes
        total_duplicadas += num_duplicadas
        
        # Atualizar galeria do projeto
        projeto['galeria'] = fotos_sem_duplicatas
        total_fotos_depois += len(fotos_sem_duplicatas)
        
        # Exibir resultados
        print(f"   ✅ Fotos válidas: {len(fotos_validas)}")
        
        if fotos_inexistentes:
            print(f"   ❌ Fotos não encontradas: {num_inexistentes}")
            for foto in fotos_inexistentes:
                print(f"      - {foto}")
        
        if duplicadas:
            print(f"   🔄 Fotos duplicadas: {num_duplicadas}")
            for foto in duplicadas:
                print(f"      - {foto} (aparece {contador[foto]}x)")
        
        print(f"   📊 Total após limpeza: {len(fotos_sem_duplicatas)} fotos")
    
    # Salvar projetos.json atualizado
    with open('projetos.json', 'w', encoding='utf-8') as f:
        json.dump(projetos, f, ensure_ascii=False, indent=2)
    
    # Resumo final
    print(f"\n{'=' * 80}")
    print("RESUMO DA VERIFICAÇÃO")
    print("=" * 80)
    print(f"Total de projetos verificados: {total_projetos}")
    print(f"Total de fotos antes: {total_fotos_antes}")
    print(f"Total de fotos depois: {total_fotos_depois}")
    print(f"Fotos inexistentes removidas: {total_removidas}")
    print(f"Fotos duplicadas removidas: {total_duplicadas}")
    print(f"Total removido: {total_removidas + total_duplicadas}")
    print(f"\n✅ Arquivo projetos.json atualizado com sucesso!")
    print("=" * 80)

if __name__ == '__main__':
    verificar_e_atualizar_projetos()
