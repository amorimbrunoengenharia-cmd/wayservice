# 🌐 CONFIGURAÇÃO DNS - GOOGLE WORKSPACE

## 📍 ONDE CONFIGURAR

1. Acesse o painel do Google Admin: https://admin.google.com
2. Navegue até: **Domínios** → **Gerenciar domínios**
3. Clique em **wayserviceltda.com**
4. Clique em **DNS** ou **Gerenciar DNS**

**OU**

Se comprou o domínio via Google Domains diretamente:
1. Acesse: https://domains.google.com
2. Clique em **wayserviceltda.com**
3. No menu lateral, clique em **DNS**

---

## 🗑️ PASSO 1: REMOVER REGISTROS CONFLITANTES

**⚠️ ANTES DE ADICIONAR, REMOVA ESTES SE EXISTIREM:**

Procure e **DELETE** qualquer registro do tipo:
- ✘ Registro **A** apontando para `wayserviceltda.com` (sem www)
- ✘ Registro **CNAME** chamado `@` (raiz)
- ✘ Registro **A** de redirecionamento web antigo

**MANTENHA (NÃO DELETE):**
- ✅ Registros **MX** (email)
- ✅ Registros **TXT** (verificação)
- ✅ Registros **SPF**, **DKIM** (segurança email)

### ⚠️ ATENÇÃO CRÍTICA: PRESERVAR REGISTROS MX DO GOOGLE WORKSPACE

**🚨 SE VOCÊ USA GOOGLE WORKSPACE PARA E-MAILS:**

Os registros MX são ESSENCIAIS para o funcionamento do e-mail. **NUNCA delete** os seguintes registros:

```
Tipo: MX | Prioridade: 1  | Valor: ASPMX.L.GOOGLE.COM
Tipo: MX | Prioridade: 5  | Valor: ALT1.ASPMX.L.GOOGLE.COM
Tipo: MX | Prioridade: 5  | Valor: ALT2.ASPMX.L.GOOGLE.COM
Tipo: MX | Prioridade: 10 | Valor: ALT3.ASPMX.L.GOOGLE.COM
Tipo: MX | Prioridade: 10 | Valor: ALT4.ASPMX.L.GOOGLE.COM
```

**Mantenha também:**
- Registros SPF: `v=spf1 include:_spf.google.com ~all`
- Registros DKIM (google._domainkey)
- Registros DMARC

**❌ O QUE ACONTECE SE DELETAR:**
- Seus e-mails @wayserviceltda.com PARAM de funcionar
- Você não receberá novos e-mails
- Você não conseguirá enviar e-mails

**✅ O QUE DEVE FAZER:**
- Apenas ADICIONE os registros A e CNAME do GitHub Pages
- MANTENHA todos os registros MX e de e-mail existentes
- Os dois sistemas (site + e-mail) funcionarão SIMULTANEAMENTE

---

## ➕ PASSO 2: ADICIONAR REGISTROS DO GITHUB PAGES

### 🔹 REGISTROS A (IP do GitHub) - OBRIGATÓRIOS

Clique em **Criar novo registro** e adicione **4 registros A**:

#### Registro A #1
```
Nome/Host: @
Tipo: A
TTL: 3600 (ou 1 hora)
Dados/Valor: 185.199.108.153
```

#### Registro A #2
```
Nome/Host: @
Tipo: A
TTL: 3600
Dados/Valor: 185.199.109.153
```

#### Registro A #3
```
Nome/Host: @
Tipo: A
TTL: 3600
Dados/Valor: 185.199.110.153
```

#### Registro A #4
```
Nome/Host: @
Tipo: A
TTL: 3600
Dados/Valor: 185.199.111.153
```

### 🔹 REGISTRO CNAME (www) - OBRIGATÓRIO

Clique em **Criar novo registro**:

#### Registro CNAME
```
Nome/Host: www
Tipo: CNAME
TTL: 3600
Dados/Valor: SEU-USUARIO.github.io.
```
⚠️ **IMPORTANTE:** 
- Substitua `SEU-USUARIO` pelo seu usuário do GitHub
- **MANTENHA o ponto `.` no final** (ex: `brunoamorim.github.io.`)

---

## 📋 RESUMO - COPIE E COLE

### ✅ CONFIGURAÇÃO FINAL DEVE FICAR ASSIM:

| Tipo | Nome | Valor | TTL |
|------|------|-------|-----|
| A | @ | 185.199.108.153 | 3600 |
| A | @ | 185.199.109.153 | 3600 |
| A | @ | 185.199.110.153 | 3600 |
| A | @ | 185.199.111.153 | 3600 |
| CNAME | www | SEU-USUARIO.github.io. | 3600 |

---

## ⏱️ PASSO 3: AGUARDAR PROPAGAÇÃO

**Tempo de propagação:**
- ⚡ Mínimo: 15 minutos
- 🕐 Normal: 2-4 horas
- 🐌 Máximo: 24-48 horas

**Enquanto isso, você pode:**
- Acessar temporariamente via: `https://SEU-USUARIO.github.io/wayservice-site/`
- Conferir propagação em: https://dnschecker.org/
  - Digite: `wayserviceltda.com`
  - Deve mostrar os IPs do GitHub

---

## ✅ PASSO 4: VERIFICAR SE FUNCIONOU

### Testar DNS:
```powershell
# No PowerShell, execute:
nslookup wayserviceltda.com
```

**Resultado esperado:**
```
Servidor:  ...
Endereço:  ...

Nome:    wayserviceltda.com
Addresses:  185.199.108.153
           185.199.109.153
           185.199.110.153
           185.199.111.153
```

### Testar www:
```powershell
nslookup www.wayserviceltda.com
```

**Resultado esperado:**
```
Nome:    SEU-USUARIO.github.io
Endereço:  ...
Aliases:  www.wayserviceltda.com
```

---

## 🔒 PASSO 5: ATIVAR HTTPS (OBRIGATÓRIO)

Após DNS propagar (2-4h depois):

1. Volte ao GitHub → Settings → Pages
2. ✅ Marque **"Enforce HTTPS"**
3. Aguarde 1-2 minutos

**Seu site estará em:**
- ✅ https://wayserviceltda.com
- ✅ https://www.wayserviceltda.com (redirecionará automaticamente)

---

## 🎯 IPs DO GITHUB (PARA COPIAR)

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**CNAME www:**
```
SEU-USUARIO.github.io.
```
(⚠️ **Não esqueça o ponto final!**)

---

## 🆘 RESOLUÇÃO DE PROBLEMAS

### ❌ "DNS check unsuccessful" no GitHub Pages
**Causa:** DNS ainda não propagou
**Solução:** Aguarde 2-4h, depois recarregue a página do GitHub Pages

### ❌ "Domain already taken" no GitHub Pages
**Causa:** Outro usuário já configurou esse domínio
**Solução:** Verifique se você é o proprietário e remova do outro repo

### ❌ Site não carrega após 48h
**Verificar:**
1. Registros A estão corretos? (4 IPs)
2. CNAME www está correto? (com ponto final)
3. Arquivo CNAME existe no repositório?
4. GitHub Pages está ativado na branch `main`?

### ❌ Certificado SSL "Not Secure"
**Causa:** HTTPS ainda não ativado ou DNS não propagou
**Solução:** 
1. Aguarde DNS propagar (teste com nslookup)
2. Desmarque "Enforce HTTPS" no GitHub Pages
3. Aguarde 5 minutos
4. Marque novamente "Enforce HTTPS"
5. Aguarde 5 minutos

---

## 📞 SUPORTE

**GitHub Pages:**
- Documentação: https://docs.github.com/en/pages
- Status: https://www.githubstatus.com/

**Google Domains:**
- Suporte: https://support.google.com/domains

**Verificar DNS:**
- https://dnschecker.org/
- https://www.whatsmydns.net/

---

## ✅ CHECKLIST FINAL

- [ ] 4 Registros A criados (IPs do GitHub)
- [ ] 1 Registro CNAME criado (www → github.io.)
- [ ] Arquivo CNAME no repositório
- [ ] GitHub Pages ativado (branch main)
- [ ] Domínio personalizado configurado no GitHub Pages
- [ ] DNS propagado (teste com nslookup)
- [ ] HTTPS ativado (cadeado verde)
- [ ] Redireciona www → sem www (ou vice-versa)
- [ ] Todas as páginas carregando
- [ ] Imagens carregando corretamente

🎉 **Parabéns! Seu site está online profissionalmente!**
