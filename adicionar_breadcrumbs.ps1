# Script para adicionar breadcrumbs em todas as páginas de projetos
# Define os projetos com seus nomes e IDs
$projetos = @(
    @{arquivo='projeto-forum-aracatuba.html'; nome='Fórum de Araçatuba'},
    @{arquivo='projeto-forum-jales.html'; nome='Fórum de Jales'},
    @{arquivo='projeto-escola-barra-bonita.html'; nome='Escola EE Laurindo Battaiola'},
    @{arquivo='projeto-escola-itapolis.html'; nome='Escola EE Dr Moraes Barros'},
    @{arquivo='projeto-lojas-americanas.html'; nome='Lojas Americanas - Reforma Varejo'},
    @{arquivo='projeto-monsanto-bayer-itai.html'; nome='Monsanto/Bayer Itaí - Sistema TRRF'},
    @{arquivo='projeto-petrobras-refinaria.html'; nome='Petrobras - Refinaria Paulínia'},
    @{arquivo='projeto-transpetro-aracaju.html'; nome='Transpetro Aracaju'},
    @{arquivo='projeto-ufv-pedro-canario.html'; nome='UFV Pedro Canário'},
    @{arquivo='projeto-ufv-santa-adelia.html'; nome='UFV Santa Adélia'},
    @{arquivo='projeto-ufv-sao-mateus.html'; nome='UFV São Mateus'}
)

foreach ($projeto in $projetos) {
    $arquivo = $projeto.arquivo
    $nomeProjeto = $projeto.nome
    
    Write-Host "Processando $arquivo..." -ForegroundColor Cyan
    
    # Lê o conteúdo do arquivo
    $content = Get-Content $arquivo -Raw -Encoding UTF8
    
    # 1. Adiciona o BreadcrumbList JSON-LD (se não existir)
    if ($content -notmatch 'BreadcrumbList') {
        $breadcrumbSchema = @"

    <!-- Schema.org BreadcrumbList Structured Data -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Início",
          "item": "https://wayservice.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Projetos",
          "item": "https://wayservice.com/projetos.html"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "$nomeProjeto",
          "item": "https://wayservice.com/$arquivo"
        }
      ]
    }
    </script>

    <style>
"@
        $content = $content -replace '    </script>\r?\n\r?\n    <style>', $breadcrumbSchema
        Write-Host "  ✓ Schema BreadcrumbList adicionado" -ForegroundColor Green
    }
    
    # 2. Adiciona o CSS do breadcrumb (se não existir)
    if ($content -notmatch '\/\* Breadcrumb Styling \*\/') {
        $breadcrumbCSS = @"
    <style>
        /* Breadcrumb Styling */
        .breadcrumb {
            background: rgba(30, 31, 39, 0.5);
            padding: 5.5rem 2rem 1rem;
            margin-top: -1rem;
        }

        .breadcrumb-container {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.9rem;
        }

        .breadcrumb-link {
            color: rgba(255, 255, 255, 0.6);
            text-decoration: none;
            transition: color 0.3s ease;
            display: flex;
            align-items: center;
            gap: 0.3rem;
        }

        .breadcrumb-link:hover {
            color: #43e456;
        }

        .breadcrumb-separator {
            color: rgba(255, 255, 255, 0.3);
            margin: 0 0.3rem;
        }

        .breadcrumb-current {
            color: #43e456;
            font-weight: 500;
        }

        @media (max-width: 768px) {
            .breadcrumb {
                padding: 5rem 1rem 0.8rem;
            }
            .breadcrumb-container {
                font-size: 0.8rem;
            }
        }

        /* Header Navigation Container */
"@
        $content = $content -replace '    <style>\r?\n        \/\* Header Navigation Container \*\/', $breadcrumbCSS
        Write-Host "  ✓ CSS do breadcrumb adicionado" -ForegroundColor Green
    }
    
    # 3. Adiciona o HTML do breadcrumb (se não existir)
    if ($content -notmatch '<div class="breadcrumb">') {
        $breadcrumbHTML = @"
        </div>
    </nav>

    <!-- Breadcrumb Navigation -->
    <div class="breadcrumb">
        <div class="breadcrumb-container">
            <a href="index.html" class="breadcrumb-link">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                </svg>
                Início
            </a>
            <span class="breadcrumb-separator">/</span>
            <a href="projetos.html" class="breadcrumb-link">Projetos</a>
            <span class="breadcrumb-separator">/</span>
            <span class="breadcrumb-current">$nomeProjeto</span>
        </div>
    </div>

    <div class="gallery-page">
"@
        $content = $content -replace '        </div>\r?\n    </nav>\r?\n\r?\n    <div class="gallery-page">', $breadcrumbHTML
        Write-Host "  ✓ HTML do breadcrumb adicionado" -ForegroundColor Green
    }
    
    # Salva as alterações
    $content | Set-Content $arquivo -Encoding UTF8 -NoNewline
    Write-Host "✅ $arquivo atualizado com sucesso!`n" -ForegroundColor Green
}

Write-Host "`n🎉 Todos os breadcrumbs foram adicionados com sucesso!" -ForegroundColor Green
