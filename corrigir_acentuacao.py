#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para corrigir acentuação em projetos.json e index.html
"""

import json
import re

def corrigir_texto(texto):
    """Aplica todas as correções de acentuação"""
    
    # Dicionário de correções
    correcoes = {
        # Forum -> Fórum
        'Forum': 'Fórum',
        
        # Palavras terminadas em -cao -> -ção
        'Execucao': 'Execução',
        'execucao': 'execução',
        'Resistencia': 'Resistência',
        'resistencia': 'resistência',
        'fabrica': 'fábrica',
        'adequacao': 'adequação',
        'seguranca': 'segurança',
        'protecao': 'proteção',
        'area': 'área',
        'atraves': 'através',
        'aplicacao': 'aplicação',
        'instalacao': 'instalação',
        'compartimentacao': 'compartimentação',
        'prevencao': 'prevenção',
        'incendios': 'incêndios',
        'Incendio': 'Incêndio',
        'Protecao': 'Proteção',
        'construcao': 'construção',
        'Operacao': 'Operação',
        'Manutencao': 'Manutenção',
        'instalacoes': 'instalações',
        'eletricas': 'elétricas',
        'Tensao': 'Tensão',
        'obtencao': 'obtenção',
        'concessionaria': 'concessionária',
        'gestao': 'gestão',
        'Renovaveis': 'Renováveis',
        'Adelia': 'Adélia',
        'Impermeabilizacao': 'Impermeabilização',
        'instalacao': 'instalação',
        'infiltracoes': 'infiltrações',
        'Servicos': 'Serviços',
        'tecnica': 'técnica',
        'termico': 'térmico',
        'termico': 'térmico',
        'acustico': 'acústico',
        'Edificacao': 'Edificação',
        'Publica': 'Pública',
        'aguas': 'águas',
        'minima': 'mínima',
        'interferencia': 'interferência',
        'modernizacao': 'modernização',
        'sanitarios': 'sanitários',
        'impermeabilizacao': 'impermeabilização',
        'reservatorio': 'reservatório',
        'arvores': 'árvores',
        'automacao': 'automação',
        'portoes': 'portões',
        'funcionalidade': 'funcionalidade',
        'Servico': 'Serviço',
        'ceramico': 'cerâmico',
        'precisao': 'precisão',
        'tecnica': 'técnica',
        'durabilidade': 'durabilidade',
        'execucao': 'execução',
        'Itapolis': 'Itápolis',
        'Aracatuba': 'Araçatuba',
        'Concluido': 'Concluído',
        
        # Palavras específicas
        'inicio': 'início',
        'DUVIDAS': 'DÚVIDAS',
        'Sao': 'São',
        'Jose': 'José',
        'Sergio': 'Sérgio'
    }
    
    for erro, correto in correcoes.items():
        texto = texto.replace(erro, correto)
    
    return texto

# Corrigir projetos.json
print("📝 Corrigindo projetos.json...")
with open('projetos.json', 'r', encoding='utf-8') as f:
    conteudo = f.read()

conteudo_corrigido = corrigir_texto(conteudo)

with open('projetos.json', 'w', encoding='utf-8') as f:
    f.write(conteudo_corrigido)

print("✅ projetos.json corrigido!")

# Corrigir index.html
print("\n📝 Corrigindo index.html...")
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    html_corrigido = corrigir_texto(html)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_corrigido)
    
    print("✅ index.html corrigido!")
except Exception as e:
    print(f"⚠️ Erro ao corrigir index.html: {e}")

print("\n🎉 Correções concluídas!")
