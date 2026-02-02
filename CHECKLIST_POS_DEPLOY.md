# ✅ CHECKLIST PÓS-DEPLOY - SITE WAYSERVICE

**Data:** 30 de Janeiro de 2026
**Status do Site:** ✅ Online no Squarespace
**DNS Google Workspace:** ✅ Configurado (MX Records)
**Última atualização:** Email comercial atualizado para <comercial@wayserviceltda.com>

---

## 🚨 AÇÕES CRÍTICAS - FAZER AGORA

### 1️⃣ Google Search Console (OBRIGATÓRIO)

**Status:** ✅ CONCLUÍDO
**Prioridade:** 🔴 CRÍTICA
**Tempo:** 15 minutos

**O que fazer:**

1. Acesse: <https://search.google.com/search-console>
2. Clique em "Adicionar propriedade"
3. Selecione "Prefixo do URL"
4. Digite: `https://wayserviceltda.com`
5. Escolha método de verificação: **Registro DNS** (mais fácil via Squarespace)
6. Copie o código TXT fornecido pelo Google
7. Adicione no Squarespace:
   - Domínios → DNS Settings
   - Add Record → Type: TXT
   - Host: @ (ou deixe em branco)
   - Value: cole o código do Google
8. Clique em "Verificar" no Google Search Console
9. **IMPORTANTE:** Envie o sitemap:
   - URL do sitemap: `https://wayserviceltda.com/sitemap.xml`
   - Clique em "Adicionar novo sitemap"

**Resultado esperado:** Indexação no Google em 24-72 horas

---

### 2️⃣ Google Analytics 4 (ALTA PRIORIDADE)

**Status:** ✅ CONCLUÍDO
**Prioridade:** 🔴 ALTA
**Tempo:** 10 minutos

**Situação atual:**

- ✅ Código GA4 instalado em todas as 19 páginas HTML

- ✅ ID real configurado: **G-WTC0G5M6C7**

- ✅ Commit e push realizados com sucesso

**O que fazer:**

1. Acesse: <https://analytics.google.com>
2. Clique em "Começar a medir"
3. Crie a conta:
   - Nome da conta: **WayService Engenharia**
   - Nome da propriedade: **Site WayService**
   - Fuso horário: **(GMT-03:00) Brasília**
   - Moeda: **Real Brasileiro (BRL)**
4. Configure o fluxo de dados:
   - Plataforma: **Web**
   - URL: `https://wayserviceltda.com`
   - Nome do fluxo: **Site Principal**
5. **COPIE o ID de medição** (formato: G-ABC1234567)
6. Execute no PowerShell (dentro da pasta do site):

```powershell
# SUBSTITUA "G-ABC1234567" pelo seu ID real do GA4
$idReal = "G-ABC1234567"

Get-ChildItem -Filter "*.html" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw -Encoding UTF8
    $content = $content -replace 'G-XXXXXXXXXX', $idReal
    $content | Set-Content $_.FullName -Encoding UTF8 -NoNewline
    Write-Host "✅ Atualizado: $($_.Name)" -ForegroundColor Green
}
```

1. Faça commit e push das alterações:

```powershell
git add .
git commit -m "Ativar Google Analytics 4 com ID real"
git push
```

**Testar:** Acesse GA4 → Relatórios → Tempo real (abra o site e veja sua visita)

---

### 3️⃣ Teste de Performance (PageSpeed Insights)

**Status:** ✅ CONCLUÍDO
**Prioridade:** 🟡 MÉDIA
**Tempo:** 5 minutos

**Resultados obtidos:**

- ✅ Mobile: **80 pontos** (Objetivo > 90) ⚠️ Pode melhorar

- ✅ Desktop: **92 pontos** (Objetivo > 95) 🎯 Excelente

- ✅ LCP (Largest Contentful Paint):
  - Mobile: 3,8s (meta: < 2.5s) ⚠️ Acima da meta
  - Desktop: 0,8s (meta: < 2.5s) ✅ Ótimo
- ✅ FID (First Input Delay):
  - Mobile: 10ms (meta: < 100ms) ✅ Excelente
  - Desktop: 210ms (meta: < 100ms) ⚠️ Acima da meta
- ✅ CLS (Cumulative Layout Shift):
  - Mobile: 0 (meta: < 0.1) ✅ Perfeito
  - Desktop: 0,006 (meta: < 0.1) ✅ Perfeito

**Outras métricas:**

- **Acessibilidade:** 96/100 ✅

- **Melhores práticas:** 100/100 ✅

- **SEO:** 100/100 ✅

**Análise:**

- ✅ Desktop está excelente (92 pontos)

- ⚠️ Mobile precisa melhorias no LCP (carregamento de imagens)

- ✅ SEO perfeito, site totalmente otimizado para busca

- ✅ Acessibilidade e práticas recomendadas implementadas

---

## 🔍 VALIDAÇÕES TÉCNICAS

### 4️⃣ Teste Mobile (Funcionalidades)

**Status:** ✅ CONCLUÍDO
**Prioridade:** 🟡 MÉDIA
**Tempo:** 10 minutos

**Testar no celular:**

- ✅ Botão de ligação funciona (abre discador)

- ✅ Botão WhatsApp funciona e abre com mensagem pré-preenchida

- ✅ Imagens carregam progressivamente (lazy loading)

- ✅ Ano no rodapé mostra 2026 (auto-update)

- ✅ Filtros de projetos funcionam corretamente

- ✅ Galeria de fotos abre e fecha suavemente

- ✅ Menu mobile responsivo funciona

- ✅ Formulários são fáceis de preencher no mobile

**Dispositivos testados:**

- ✅ iPhone/iOS

- ✅ Android

---

### 5️⃣ Testar Formulários

**Status:** ✅ CONCLUÍDO
**Prioridade:** 🟡 MÉDIA
**Tempo:** 5 minutos

**Formulários a testar:**

1. **Formulário de Contato** (contato.html)
   - ✅ Preencher todos os campos
   - ✅ Clicar em "Enviar"
   - ✅ Verificar se chegou no email: <comercial@wayserviceltda.com>

2. **Formulário de Orçamento** (orcamento.html)
   - ✅ Preencher todos os campos
   - ✅ Clicar em "Enviar Orçamento"
   - ✅ Verificar se chegou no email: <comercial@wayserviceltda.com>

3. **Canal de Denúncia** (canal-denuncia.html)
   - ✅ Preencher formulário
   - ✅ Verificar se é enviado corretamente

**Observação:** Se os formulários não estiverem chegando, verificar configuração do Squarespace Forms ou FormSubmit.

---

### 6️⃣ Links e Navegação

**Status:** ✅ CONCLUÍDO
**Prioridade:** 🟢 BAIXA
**Tempo:** 5 minutos

**Verificar:**

- ✅ Todos os links do menu funcionam

- ✅ Links para páginas de projetos funcionam

- ✅ Links de redes sociais funcionam (se houver)

- ✅ Email clicável abre cliente de email

- ✅ Telefone clicável funciona

- ✅ Não há links quebrados (erro 404)

---

### 7️⃣ SEO e Meta Tags

**Status:** ✅ IMPLEMENTADO
**Prioridade:** 🟢 BAIXA

**Verificar com ferramentas:**

1. **Rich Results Test**
   - Acesse: <https://search.google.com/test/rich-results>
   - URL: `https://wayserviceltda.com`
   - Verificar se Schema.org está correto

2. **Mobile-Friendly Test**
   - Acesse: <https://search.google.com/test/mobile-friendly>
   - URL: `https://wayserviceltda.com`
   - Deve mostrar "A página é compatível com dispositivos móveis"

---

## 📊 CONFIGURAÇÕES AVANÇADAS (OPCIONAL)

### 8️⃣ Google Business Profile

**Status:** ⏳ AGUARDANDO BARRACÃO
**Prioridade:** 🟡 RECOMENDADO
**Tempo:** 15 minutos

**Observação:** Aguardando construção do barracão para configurar endereço físico no Google Business.

**Benefícios:**

- Aparecer no Google Maps

- Reviews de clientes

- Informações de contato no Google

**O que fazer:**

1. Acesse: <https://business.google.com>
2. Clique em "Gerenciar agora"
3. Adicione a empresa:
   - Nome: **WayService Engenharia Ltda**
   - Categoria: **Construtora** / **Engenharia Civil**
   - Endereço: (seu endereço comercial)
   - Telefone: (18) 9 9742-1905
   - Site: <https://wayserviceltda.com>
4. Verificar a empresa (Google envia código por carta/telefone)

---

### 9️⃣ Backup Automático

**Status:** ✅ CONCLUÍDO
**Prioridade:** 🟢 RECOMENDADO

**Configurar backup do código:**

- ✅ GitHub já configurado (repositório: amorimbrunoengenharia-cmd/wayservice)

- ✅ Configurar backup no Squarespace (se disponível)

- ✅ Documentar processo de restauração

---

### 🔟 Certificado SSL

**Status:** ✅ CONCLUÍDO
**Prioridade:** 🔴 CRÍTICA

**Resultado:**

- ✅ Site acessível via HTTPS

- ✅ Cadeado 🔒 aparece no navegador

- ✅ Certificado SSL ativo e válido

**SSL ATIVO para:**

- ✅ Google indexar corretamente

- ✅ Formulários funcionarem

- ✅ Confiança dos visitantes

---

## 📈 MONITORAMENTO CONTÍNUO

### Semanalmente

- [ ] Verificar Google Search Console (erros de rastreamento)

- [ ] Verificar Google Analytics (tráfego, conversões)

- [ ] Testar formulários (envio de teste)

### Mensalmente

- [ ] Executar PageSpeed Insights

- [ ] Revisar palavras-chave posicionadas

- [ ] Atualizar projetos (adicionar novos)

- [ ] Backup completo do site

---

## 🎯 METAS DE SUCESSO

### 30 dias após deploy

- [ ] Site indexado no Google (aparecer na busca "wayservice")

- [ ] Google Analytics mostrando dados

- [ ] Pelo menos 1 conversão via formulário

- [ ] PageSpeed > 90 no mobile

### 90 dias após deploy

- [ ] Aparecer na 1ª página para "construtora obras públicas [cidade]"

- [ ] 50+ visitantes/mês

- [ ] 5+ conversões via formulário

- [ ] 10+ reviews no Google Business (se configurado)

---

## 📞 CONTATOS DE SUPORTE

**Site:** <https://wayserviceltda.com>
**Email:** <comercial@wayserviceltda.com>
**Telefone:** (18) 9 9742-1905
**Repositório GitHub:** <https://github.com/amorimbrunoengenharia-cmd/wayservice>

---

## ✅ PROGRESSO GERAL

**Concluído:** 9/10 itens (90%)
**Pendente:** 1/10 itens
**Próxima ação:** Google Business Profile (aguardando construção do barracão)

**Itens concluídos:**

- ✅ Google Search Console configurado e sitemap enviado

- ✅ Google Analytics 4 ativado (ID: G-WTC0G5M6C7)

- ✅ Teste de Performance realizado (Desktop 92, Mobile 80)

- ✅ Teste Mobile realizado em iPhone e Android

- ✅ Formulários testados e funcionando

- ✅ Links e navegação verificados

- ✅ SEO e Meta Tags implementados (100/100)

- ✅ Backup automático configurado

- ✅ Certificado SSL ativo

**Itens pendentes:**

- ⏳ Google Business Profile (aguardando construção do barracão)

---

**Última atualização:** 30/01/2026
**Responsável:** Bruno Amorim
