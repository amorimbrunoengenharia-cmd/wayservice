# ⚡ COMANDOS FINAIS PARA DEPLOY

## ✅ JÁ EXECUTADO AUTOMATICAMENTE:

```bash
✅ git init
✅ git add .
✅ git commit -m "Deploy completo - Site Way Service com domínio personalizado"
```

---

## 🎯 AGORA VOCÊ PRECISA FAZER:

### PASSO 1: Criar Repositório no GitHub (2 minutos)

1. **Abra este link:** https://github.com/new

2. **Configure o repositório:**
   - 📝 **Repository name:** `wayservice-site`
   - 📝 **Description:** Site oficial da Way Service Construções
   - 🔓 **IMPORTANTE:** Selecione **"Public"** (obrigatório para GitHub Pages gratuito)
   - ❌ **NÃO marque:** "Add a README", "Add .gitignore", "Choose a license"
   
3. **Clique em:** "Create repository"

4. **Copie a URL do repositório** que aparecerá (exemplo):
   ```
   https://github.com/SEU-USUARIO/wayservice-site.git
   ```

---

### PASSO 2: Conectar e Enviar (1 comando)

**No terminal do VS Code abaixo, cole este comando substituindo SEU-USUARIO:**

```powershell
git remote add origin https://github.com/SEU-USUARIO/wayservice-site.git; git push -u origin main
```

**EXEMPLO (substitua brunoamorim pelo SEU usuário):**
```powershell
git remote add origin https://github.com/brunoamorim/wayservice-site.git; git push -u origin main
```

**O que vai acontecer:**
1. Git vai conectar ao seu repositório GitHub
2. Vai pedir autenticação (use seu token ou faça login)
3. Vai enviar todos os arquivos (pode demorar 1-2 minutos)

---

### 🔑 AUTENTICAÇÃO DO GITHUB

Quando executar o push, o GitHub vai pedir autenticação:

**OPÇÃO A - GitHub CLI (Mais Fácil):**
```powershell
# Instalar (se não tiver)
winget install GitHub.cli

# Fazer login
gh auth login
```

**OPÇÃO B - Personal Access Token:**
1. Acesse: https://github.com/settings/tokens
2. Clique "Generate new token" → "Classic"
3. Marque: `repo` (full control)
4. Copie o token gerado
5. Quando pedir senha, cole o TOKEN (não sua senha normal)

---

## 🌐 PASSO 3: Ativar GitHub Pages (3 minutos)

Após o `git push` ser bem-sucedido:

1. **Vá para seu repositório:** `https://github.com/SEU-USUARIO/wayservice-site`
2. **Clique em:** ⚙️ **Settings** (Configurações)
3. **No menu lateral esquerdo:** clique em **Pages**
4. **Em "Source":**
   - Branch: selecione `main`
   - Folder: selecione `/ (root)`
5. **Clique em:** 💾 **Save**
6. **Em "Custom domain":**
   - Digite: `wayserviceltda.com`
   - Clique em **Save**
   - ⚠️ Vai aparecer erro "DNS check unsuccessful" - É NORMAL! Continue.

✅ **Pronto! GitHub configurado.**

---

## 🌍 PASSO 4: Configurar DNS no Google (5 minutos)

### Acesse seu painel Google:
- Google Domains: https://domains.google.com
- OU Google Workspace Admin: https://admin.google.com → Domínios

### Clique em wayserviceltda.com → DNS

### Adicione 4 REGISTROS A:

```
Tipo: A    Host: @    Valor: 185.199.108.153    TTL: 3600
Tipo: A    Host: @    Valor: 185.199.109.153    TTL: 3600
Tipo: A    Host: @    Valor: 185.199.110.153    TTL: 3600
Tipo: A    Host: @    Valor: 185.199.111.153    TTL: 3600
```

### Adicione 1 REGISTRO CNAME:

```
Tipo: CNAME    Host: www    Valor: SEU-USUARIO.github.io.    TTL: 3600
```
⚠️ **IMPORTANTE:** Substitua SEU-USUARIO e **mantenha o ponto final** `.`

---

## ⏰ PASSO 5: Aguardar Propagação (2-4 horas)

**O que vai acontecer:**
- ⏱️ Mínimo: 15 minutos
- ✅ Normal: 2-4 horas
- 🐢 Máximo: 48 horas

**Enquanto isso, acesse temporariamente:**
```
https://SEU-USUARIO.github.io/wayservice-site/
```

**Teste a propagação DNS:**
```powershell
nslookup wayserviceltda.com
```

Deve retornar os 4 IPs do GitHub:
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

---

## 🔒 PASSO 6: Ativar HTTPS (2 minutos)

Após DNS propagar (teste com nslookup):

1. Volte ao GitHub → Settings → Pages
2. ✅ Marque: **"Enforce HTTPS"**
3. Aguarde 1-2 minutos

---

## 🎉 PRONTO! SEU SITE ESTARÁ ONLINE:

✅ **https://wayserviceltda.com**
✅ **https://www.wayserviceltda.com**

---

## 📊 RESUMO VISUAL

```
┌─────────────────────────────────────────────────┐
│  1. Criar repo GitHub (2 min)                   │
│     └─> https://github.com/new                  │
├─────────────────────────────────────────────────┤
│  2. git push (1 comando)                        │
│     └─> git remote add origin ... && git push  │
├─────────────────────────────────────────────────┤
│  3. Ativar Pages no GitHub (3 min)             │
│     └─> Settings → Pages → main → Save         │
├─────────────────────────────────────────────────┤
│  4. Configurar DNS no Google (5 min)           │
│     └─> 4 registros A + 1 CNAME                │
├─────────────────────────────────────────────────┤
│  5. Aguardar propagação (2-4h)                 │
│     └─> Testar com nslookup                    │
├─────────────────────────────────────────────────┤
│  6. Ativar HTTPS no GitHub (2 min)             │
│     └─> Settings → Pages → Enforce HTTPS       │
└─────────────────────────────────────────────────┘
```

**⏱️ TEMPO TOTAL ATIVO:** 13 minutos
**⏱️ TEMPO DE ESPERA:** 2-4 horas (DNS)

---

## 🆘 EM CASO DE PROBLEMAS

### ❌ "authentication failed" no git push
**Solução:** Use Personal Access Token ou `gh auth login`

### ❌ "DNS check unsuccessful" no GitHub
**Solução:** Normal! Configure o DNS e aguarde 2-4h

### ❌ Site não carrega após 48h
**Verificar:**
1. ✅ 4 registros A estão corretos?
2. ✅ CNAME www está correto? (com ponto final)
3. ✅ Arquivo CNAME existe no repositório?
4. ✅ GitHub Pages está ativado?

### ❌ "repository not found" no git push
**Solução:** Verifique:
1. Criou o repositório no GitHub?
2. Repositório é PÚBLICO?
3. URL está correta?

---

## 📞 DOCUMENTAÇÃO COMPLETA

- 📘 **Comandos Git detalhados:** `DEPLOY_COMANDOS.md`
- 🌐 **Configuração DNS passo a passo:** `GUIA_DNS_GOOGLE.md`
- 🚀 **Visão geral de deploy:** `GUIA_DEPLOY.md`

---

## ✅ CHECKLIST FINAL

- [ ] Repositório criado no GitHub (público)
- [ ] git push executado com sucesso
- [ ] GitHub Pages ativado (Settings → Pages)
- [ ] Domínio personalizado configurado no GitHub
- [ ] 4 Registros A adicionados no Google DNS
- [ ] 1 Registro CNAME adicionado no Google DNS
- [ ] DNS propagado (teste com nslookup)
- [ ] HTTPS ativado (Enforce HTTPS marcado)
- [ ] Site carregando em https://wayserviceltda.com

---

🎯 **COMECE AGORA PELO PASSO 1:** https://github.com/new
