# 📊 Guia de Configuração do Google Analytics 4 (GA4)

## ✅ Status da Implementação

**Google Analytics 4 já está implementado em todas as páginas do site!**
- ✅ 17 páginas HTML configuradas com script GA4
- ✅ Código placeholder `G-XXXXXXXXXX` inserido em todas as páginas
- ⚠️ **Ação Necessária:** Substituir `G-XXXXXXXXXX` pelo ID real da propriedade GA4

---

## 🚀 Passo a Passo para Ativar

### 1. Criar Conta Google Analytics 4

1. Acesse: [https://analytics.google.com](https://analytics.google.com)
2. Clique em **"Começar a medir"** ou **"Criar propriedade"**
3. Preencha os dados:
   - **Nome da conta:** WayService Engenharia
   - **Nome da propriedade:** Site WayService
   - **Fuso horário:** (GMT-03:00) Brasília
   - **Moeda:** Real Brasileiro (BRL)

### 2. Configurar Fluxo de Dados da Web

1. Selecione **"Web"** como plataforma
2. Preencha:
   - **URL do site:** `https://wayservice.com`
   - **Nome do fluxo:** Site Principal
3. Clique em **"Criar fluxo"**

### 3. Copiar o ID de Medição

1. Após criar o fluxo, você verá o **ID de medição** no formato: `G-XXXXXXXXXX`
2. **Copie este ID** (exemplo: `G-ABC1234567`)

---

## 🔧 Atualizar o Site com o ID Real

### Substituir o Placeholder

Execute o seguinte comando PowerShell (substitua `G-ABC1234567` pelo seu ID real):

```powershell
# Substituir G-XXXXXXXXXX pelo ID real em todos os arquivos HTML
$idReal = "G-ABC1234567"  # ⚠️ SUBSTITUA PELO SEU ID REAL

Get-ChildItem -Filter "*.html" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw -Encoding UTF8
    $content = $content -replace 'G-XXXXXXXXXX', $idReal
    $content | Set-Content $_.FullName -Encoding UTF8 -NoNewline
    Write-Host "✅ Atualizado: $($_.Name)" -ForegroundColor Green
}

Write-Host "`n🎉 Todos os arquivos atualizados com o ID: $idReal" -ForegroundColor Cyan
```

**Ou execute manualmente:**

```powershell
# Exemplo com ID real
(Get-Content index.html -Raw) -replace 'G-XXXXXXXXXX', 'G-ABC1234567' | Set-Content index.html -NoNewline
```

---

## 📈 Eventos e Conversões Importantes

### Eventos Automáticos do GA4

✅ **Já rastreados automaticamente:**
- `page_view` - Visualizações de página
- `scroll` - Rolagem (90%)
- `click` - Cliques em links externos
- `file_download` - Downloads de arquivos

### Conversões Recomendadas

Configure as seguintes conversões no GA4:

1. **Formulário de Orçamento Enviado**
   - Evento: `form_submit`
   - Página: `/orcamento.html`

2. **Formulário de Contato Enviado**
   - Evento: `form_submit`
   - Página: `/contato.html`

3. **Visualização de Projetos**
   - Evento: `page_view`
   - Página: `/projeto-*.html`

4. **Clique em WhatsApp**
   - Evento: `click`
   - Classe: `whatsapp-float`

5. **Clique em Telefone**
   - Evento: `click`
   - Classe: `phone-float`

---

## 🎯 Configurações Recomendadas

### 1. Google Search Console

1. Acesse: [https://search.google.com/search-console](https://search.google.com/search-console)
2. Adicione a propriedade: `https://wayservice.com`
3. Vincule com o Google Analytics:
   - GA4 → **Administrador** → **Vínculos do Search Console**

### 2. Google Ads (Futuramente)

Se usar Google Ads, vincule a conta:
- GA4 → **Administrador** → **Vínculos do Google Ads**

### 3. Relatórios Personalizados

Configure relatórios para:
- **Taxa de conversão por origem** (Google, Direto, Redes Sociais)
- **Projetos mais visualizados**
- **Páginas de saída** (onde os visitantes saem)
- **Tempo médio na página**

---

## 📊 Métricas Importantes para Acompanhar

### Conversões
- 🎯 **Formulários enviados** (orçamento + contato)
- 📱 **Cliques em WhatsApp**
- 📞 **Cliques em telefone**
- 📄 **Downloads de documentos**

### Engajamento
- ⏱️ **Tempo médio na página**
- 📄 **Páginas por sessão**
- 📈 **Taxa de rejeição**
- 🔄 **Usuários recorrentes**

### Origens de Tráfego
- 🔍 **Google Orgânico** (SEO)
- 💰 **Google Ads** (campanhas pagas)
- 📱 **Redes Sociais** (LinkedIn, Instagram)
- 🔗 **Referências** (outros sites)
- 📧 **Email Marketing**

---

## 🔍 Testar se está Funcionando

### 1. Verificação em Tempo Real

1. Acesse: Google Analytics → **Relatórios** → **Tempo real**
2. Abra o site: `https://wayservice.com`
3. Você deve ver sua visita aparecer em até 30 segundos

### 2. Tag Assistant (Extensão Chrome)

1. Instale: [Tag Assistant Legacy](https://chrome.google.com/webstore/detail/tag-assistant-legacy/kejbdjndbnbjgmefkgdddjlbokphdefk)
2. Abra o site e clique na extensão
3. Verifique se o tag `gtag.js - G-XXXXXXXXXX` aparece em verde ✅

### 3. Console do Navegador

```javascript
// Verificar se o gtag está carregado
console.log(window.dataLayer);
// Deve retornar um array com eventos
```

---

## ⚠️ Checklist Final

Antes de considerar a implementação completa:

- [ ] Criar conta Google Analytics 4
- [ ] Obter ID de medição (G-XXXXXXXXXX)
- [ ] Substituir placeholder pelo ID real em todos os HTML
- [ ] Fazer commit e deploy das alterações
- [ ] Testar em tempo real no GA4
- [ ] Configurar conversões (formulários, WhatsApp, telefone)
- [ ] Vincular com Google Search Console
- [ ] Criar relatórios personalizados
- [ ] Configurar alertas de anomalias
- [ ] Documentar processo para equipe

---

## 📚 Recursos Úteis

- [Documentação oficial GA4](https://support.google.com/analytics/answer/9304153)
- [Curso gratuito Google Analytics Academy](https://analytics.google.com/analytics/academy/)
- [Guia de configuração de eventos personalizados](https://support.google.com/analytics/answer/9322688)

---

## 🆘 Suporte

Se tiver dúvidas durante a configuração:
1. Consulte a [Central de Ajuda do Google Analytics](https://support.google.com/analytics)
2. Use o chat de suporte dentro do GA4 (canto inferior direito)
3. Comunidade do Google Analytics: [Forum](https://support.google.com/analytics/community)

---

**✅ Implementado em:** 23/12/2025  
**🔄 Última atualização:** 23/12/2025  
**👨‍💻 Implementado por:** GitHub Copilot
