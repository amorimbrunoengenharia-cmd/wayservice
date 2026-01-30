# ✅ CHECKLIST PÓS-DEPLOY - SITE WAYSERVICE

**Data:** 30 de Janeiro de 2026  
**Status do Site:** ✅ Online no Squarespace  
**DNS Google Workspace:** ✅ Configurado (MX Records)  
**Última atualização:** Email comercial atualizado para comercial@wayserviceltda.com

---

## 🚨 AÇÕES CRÍTICAS - FAZER AGORA

### 1️⃣ Google Search Console (OBRIGATÓRIO)
**Status:** ⚠️ PENDENTE  
**Prioridade:** 🔴 CRÍTICA  
**Tempo:** 15 minutos

**O que fazer:**
1. Acesse: https://search.google.com/search-console
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
**Status:** ⚠️ CÓDIGO INSTALADO, FALTA ATIVAR  
**Prioridade:** 🔴 ALTA  
**Tempo:** 10 minutos

**Situação atual:**
- ✅ Código GA4 já está em todas as 17 páginas HTML
- ⚠️ Usando placeholder `G-XXXXXXXXXX`
- ❌ Precisa criar conta GA4 e substituir pelo ID real

**O que fazer:**
1. Acesse: https://analytics.google.com
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

7. Faça commit e push das alterações:
```powershell
git add .
git commit -m "Ativar Google Analytics 4 com ID real"
git push
```

**Testar:** Acesse GA4 → Relatórios → Tempo real (abra o site e veja sua visita)

---

### 3️⃣ Teste de Performance (PageSpeed Insights)
**Status:** ⚠️ PENDENTE  
**Prioridade:** 🟡 MÉDIA  
**Tempo:** 5 minutos

**O que fazer:**
1. Acesse: https://pagespeed.web.dev/
2. Digite: `https://wayserviceltda.com`
3. Clique em "Analisar"
4. Verifique as pontuações:
   - **Mobile:** Objetivo > 90
   - **Desktop:** Objetivo > 95
5. Anote os resultados abaixo:

**Resultados obtidos:**
- [ ] Mobile: _____ pontos
- [ ] Desktop: _____ pontos
- [ ] LCP (Largest Contentful Paint): _____ segundos (meta: < 2.5s)
- [ ] FID (First Input Delay): _____ ms (meta: < 100ms)
- [ ] CLS (Cumulative Layout Shift): _____ (meta: < 0.1)

---

## 🔍 VALIDAÇÕES TÉCNICAS

### 4️⃣ Teste Mobile (Funcionalidades)
**Status:** ⚠️ PENDENTE  
**Prioridade:** 🟡 MÉDIA  
**Tempo:** 10 minutos

**Testar no celular:**
- [ ] Botão de ligação funciona (abre discador)
- [ ] Botão WhatsApp funciona e abre com mensagem pré-preenchida
- [ ] Imagens carregam progressivamente (lazy loading)
- [ ] Ano no rodapé mostra 2026 (auto-update)
- [ ] Filtros de projetos funcionam corretamente
- [ ] Galeria de fotos abre e fecha suavemente
- [ ] Menu mobile responsivo funciona
- [ ] Formulários são fáceis de preencher no mobile

**Dispositivos testados:**
- [ ] iPhone/iOS
- [ ] Android

---

### 5️⃣ Testar Formulários
**Status:** ⚠️ PENDENTE  
**Prioridade:** 🟡 MÉDIA  
**Tempo:** 5 minutos

**Formulários a testar:**
1. **Formulário de Contato** (contato.html)
   - [ ] Preencher todos os campos
   - [ ] Clicar em "Enviar"
   - [ ] Verificar se chegou no email: comercial@wayserviceltda.com
   
2. **Formulário de Orçamento** (orcamento.html)
   - [ ] Preencher todos os campos
   - [ ] Clicar em "Enviar Orçamento"
   - [ ] Verificar se chegou no email: comercial@wayserviceltda.com

3. **Canal de Denúncia** (canal-denuncia.html)
   - [ ] Preencher formulário
   - [ ] Verificar se é enviado corretamente

**Observação:** Se os formulários não estiverem chegando, verificar configuração do Squarespace Forms ou FormSubmit.

---

### 6️⃣ Links e Navegação
**Status:** ⚠️ PENDENTE  
**Prioridade:** 🟢 BAIXA  
**Tempo:** 5 minutos

**Verificar:**
- [ ] Todos os links do menu funcionam
- [ ] Links para páginas de projetos funcionam
- [ ] Links de redes sociais funcionam (se houver)
- [ ] Email clicável abre cliente de email
- [ ] Telefone clicável funciona
- [ ] Não há links quebrados (erro 404)

---

### 7️⃣ SEO e Meta Tags
**Status:** ✅ IMPLEMENTADO  
**Prioridade:** 🟢 BAIXA  

**Verificar com ferramentas:**
1. **Rich Results Test**
   - Acesse: https://search.google.com/test/rich-results
   - URL: `https://wayserviceltda.com`
   - Verificar se Schema.org está correto

2. **Mobile-Friendly Test**
   - Acesse: https://search.google.com/test/mobile-friendly
   - URL: `https://wayserviceltda.com`
   - Deve mostrar "A página é compatível com dispositivos móveis"

---

## 📊 CONFIGURAÇÕES AVANÇADAS (OPCIONAL)

### 8️⃣ Google Business Profile
**Status:** ⚠️ PENDENTE  
**Prioridade:** 🟡 RECOMENDADO  
**Tempo:** 15 minutos

**Benefícios:**
- Aparecer no Google Maps
- Reviews de clientes
- Informações de contato no Google

**O que fazer:**
1. Acesse: https://business.google.com
2. Clique em "Gerenciar agora"
3. Adicione a empresa:
   - Nome: **WayService Engenharia Ltda**
   - Categoria: **Construtora** / **Engenharia Civil**
   - Endereço: (seu endereço comercial)
   - Telefone: (18) 9 9742-1905
   - Site: https://wayserviceltda.com
4. Verificar a empresa (Google envia código por carta/telefone)

---

### 9️⃣ Backup Automático
**Status:** ⚠️ PENDENTE  
**Prioridade:** 🟢 RECOMENDADO  

**Configurar backup do código:**
- ✅ GitHub já configurado (repositório: amorimbrunoengenharia-cmd/wayservice)
- [ ] Configurar backup no Squarespace (se disponível)
- [ ] Documentar processo de restauração

---

### 🔟 Certificado SSL
**Status:** ⚠️ VERIFICAR  
**Prioridade:** 🔴 CRÍTICA  

**O que fazer:**
1. Acesse: `https://wayserviceltda.com`
2. Verificar se aparece cadeado 🔒 no navegador
3. Se não aparecer, configurar SSL no Squarespace:
   - Settings → SSL
   - Ativar "Secure (Preferred)"

**SSL é OBRIGATÓRIO para:**
- Google indexar corretamente
- Formulários funcionarem
- Confiança dos visitantes

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

### 30 dias após deploy:
- [ ] Site indexado no Google (aparecer na busca "wayservice")
- [ ] Google Analytics mostrando dados
- [ ] Pelo menos 1 conversão via formulário
- [ ] PageSpeed > 90 no mobile

### 90 dias após deploy:
- [ ] Aparecer na 1ª página para "construtora obras públicas [cidade]"
- [ ] 50+ visitantes/mês
- [ ] 5+ conversões via formulário
- [ ] 10+ reviews no Google Business (se configurado)

---

## 📞 CONTATOS DE SUPORTE

**Site:** wayserviceltda.com  
**Email:** comercial@wayserviceltda.com  
**Telefone:** (18) 9 9742-1905  
**Repositório GitHub:** https://github.com/amorimbrunoengenharia-cmd/wayservice

---

## ✅ PROGRESSO GERAL

**Concluído:** 0/10 itens  
**Pendente:** 10/10 itens  
**Próxima ação:** Google Search Console (Item #1)

---

**Última atualização:** 30/01/2026  
**Responsável:** Bruno Amorim
