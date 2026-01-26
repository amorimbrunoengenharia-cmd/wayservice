# 🌐 CONFIGURAÇÃO DNS - SQUARESPACE → GITHUB PAGES

## 📍 ONDE CONFIGURAR

1. Acesse: **https://pt.squarespace.com/**
2. Faça login na sua conta
3. No painel, vá em **Domínios** ou **Domains**
4. Clique no domínio **wayserviceltda.com**
5. Clique em **Configurações de DNS** ou **DNS Settings**

---

## 🚨 ATENÇÃO CRÍTICA: PRESERVAR REGISTROS MX DO GOOGLE WORKSPACE

**⚠️ ANTES DE FAZER QUALQUER ALTERAÇÃO DE DNS:**

Se você usa **Google Workspace** (Gmail empresarial) com seu domínio, é ESSENCIAL manter os registros MX:

### Registros MX que DEVEM ser mantidos:

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
- Registros de verificação TXT do Google

### ❌ O QUE ACONTECE SE DELETAR:
- Seus e-mails @wayserviceltda.com PARAM de funcionar imediatamente
- Você perderá recebimento e envio de e-mails
- Recuperação pode levar 48-72 horas

### ✅ SOLUÇÃO:
Ao adicionar registros A ou CNAME para o site, **apenas ADICIONE** os novos registros. **NUNCA delete** os registros MX existentes. Ambos os sistemas funcionarão simultaneamente:
- Registros A/CNAME → Site no GitHub Pages
- Registros MX → E-mail no Google Workspace

---

## ⚠️ IMPORTANTE - MÉTODO CORRETO PARA SQUARESPACE

### 🔴 ATENÇÃO: Squarespace tem limitações!

Se o domínio foi **registrado através do Squarespace**, você tem duas opções:

#### **OPÇÃO A - Usar Subdomínio (Mais Simples)** ✅ Recomendado

Use um subdomínio como `site.wayserviceltda.com` ou `www.wayserviceltda.com`:

**1. Configuração no Squarespace:**
- Adicione apenas 1 registro CNAME:
```
Host: www
Type: CNAME
Value: amorimbrunoengenharia-cmd.github.io.
TTL: 3600
```

**2. Configuração no GitHub Pages:**
- No arquivo CNAME (já criado), mude para:
```
www.wayserviceltda.com
```

**3. Redirecionar domínio principal:**
- No Squarespace, configure um redirecionamento de `wayserviceltda.com` para `www.wayserviceltda.com`

---

#### **OPÇÃO B - Domínio Raiz (Mais Complexo)**

⚠️ **Squarespace não permite registros A personalizados facilmente** se o domínio foi registrado lá.

**Você precisará:**

1. **Transferir o domínio para outro registrador** (Google Domains, Cloudflare, etc.)
   - OU -
2. **Usar DNS Externo** (Cloudflare - GRATUITO)

---

## 🚀 SOLUÇÃO RÁPIDA - CLOUDFLARE (GRATUITO) 

### Por que Cloudflare?
- ✅ DNS gratuito e rápido
- ✅ SSL automático
- ✅ Permite registros A personalizados
- ✅ Não precisa transferir o domínio

### Passo a Passo:

#### **PASSO 1: Criar conta Cloudflare**

1. Acesse: **https://dash.cloudflare.com/sign-up**
2. Crie uma conta gratuita
3. Clique em **"Adicionar um site"** ou **"Add a site"**
4. Digite: `wayserviceltda.com`
5. Selecione o plano **"Free"** (gratuito)

#### **PASSO 2: Configurar DNS no Cloudflare**

Cloudflare vai escanear seus registros DNS atuais. Depois:

1. **Remova** qualquer registro A ou CNAME apontando para Squarespace
2. **Adicione 4 Registros A** (GitHub Pages):

```
Type: A    Name: @    Content: 185.199.108.153    Proxy: OFF (cinza)
Type: A    Name: @    Content: 185.199.109.153    Proxy: OFF (cinza)
Type: A    Name: @    Content: 185.199.110.153    Proxy: OFF (cinza)
Type: A    Name: @    Content: 185.199.111.153    Proxy: OFF (cinza)
```

⚠️ **IMPORTANTE:** Deixe a "nuvem" em **CINZA** (proxy OFF), não laranja!

3. **Adicione 1 Registro CNAME** (www):

```
Type: CNAME    Name: www    Content: amorimbrunoengenharia-cmd.github.io    Proxy: OFF (cinza)
```

#### **PASSO 3: Alterar Nameservers no Squarespace**

Cloudflare vai fornecer 2 nameservers, algo como:
```
ava.ns.cloudflare.com
phil.ns.cloudflare.com
```

No **Squarespace**:
1. Vá em **Domínios** → **wayserviceltda.com**
2. Procure por **"Nameservers"** ou **"Servidores de nomes"**
3. Selecione **"Usar servidores de nomes personalizados"**
4. Cole os 2 nameservers do Cloudflare
5. **Salvar**

#### **PASSO 4: Verificar no Cloudflare**

1. Volte ao Cloudflare
2. Clique em **"Done, check nameservers"**
3. Aguarde 5-10 minutos para Cloudflare confirmar

#### **PASSO 5: SSL no Cloudflare**

1. No Cloudflare, vá em **SSL/TLS**
2. Selecione modo: **"Flexible"**

---

## 📋 OPÇÃO SIMPLIFICADA - APENAS WWW

Se não quiser usar Cloudflare, a solução mais simples:

### No Squarespace:

1. **Adicione registro CNAME:**
```
Host: www
Type: CNAME
Value: amorimbrunoengenharia-cmd.github.io.
TTL: Automatic
```

2. **Configure redirecionamento:**
- Redirecione `wayserviceltda.com` → `www.wayserviceltda.com`
- (Procure por "Domain Forwarding" ou "Redirecionamento")

### No seu projeto (arquivo CNAME):

Altere o conteúdo do arquivo CNAME para:
```
www.wayserviceltda.com
```

### No GitHub Pages:

1. Vá em **Settings → Pages**
2. Em **Custom domain**, digite: `www.wayserviceltda.com`
3. Aguarde verificação DNS (15-30 min)
4. Marque **"Enforce HTTPS"**

---

## ⏱️ TIMELINE

### Opção Cloudflare (Recomendada):
```
⏰ Agora          → Criar conta Cloudflare (5 min)
⏰ +5 min         → Configurar DNS no Cloudflare (5 min)
⏰ +10 min        → Alterar nameservers no Squarespace (5 min)
⏰ +30 min a 24h  → Propagação nameservers
⏰ Após propagação → Ativar HTTPS no GitHub (2 min)
✅ SITE ONLINE!
```

### Opção Apenas WWW (Mais Simples):
```
⏰ Agora          → Adicionar CNAME no Squarespace (3 min)
⏰ +3 min         → Alterar arquivo CNAME do projeto (1 min)
⏰ +4 min         → Configurar GitHub Pages (2 min)
⏰ +15 min a 2h   → Propagação DNS
⏰ Após propagação → Ativar HTTPS no GitHub (2 min)
✅ SITE ONLINE EM www.wayserviceltda.com!
```

---

## 🔍 VERIFICAR QUAL OPÇÃO VOCÊ TEM

Execute no PowerShell:

```powershell
nslookup -type=ns wayserviceltda.com
```

**Se mostrar nameservers do Squarespace** (ex: ns1.squarespace.com):
- ✅ Você pode usar Cloudflare (Opção A)
- ✅ Ou usar apenas www (Opção B)

---

## 🆘 QUAL OPÇÃO ESCOLHER?

### Use **Cloudflare** se:
- ✅ Quer usar `wayserviceltda.com` (sem www)
- ✅ Quer DNS mais rápido
- ✅ Quer controle total do DNS
- ✅ Quer SSL/CDN grátis adicional

### Use **Apenas WWW** se:
- ✅ Não se importa de usar `www.wayserviceltda.com`
- ✅ Quer solução mais simples
- ✅ Não quer criar outra conta (Cloudflare)

---

## 📞 LINKS ÚTEIS

**Cloudflare:**
- Criar conta: https://dash.cloudflare.com/sign-up
- Documentação: https://developers.cloudflare.com/dns/

**Squarespace:**
- Login: https://pt.squarespace.com/
- Suporte DNS: https://support.squarespace.com/hc/pt-br/articles/205812378

**GitHub Pages:**
- Documentação: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site

---

## ✅ PRÓXIMOS PASSOS

1. **Escolha sua opção:**
   - [ ] Cloudflare (domínio raiz + www)
   - [ ] Apenas WWW (mais simples)

2. **Siga o guia correspondente acima**

3. **Teste após propagação:**
```powershell
nslookup wayserviceltda.com
```

4. **Ative HTTPS no GitHub Pages**

---

## 🎉 RESULTADO FINAL

### Com Cloudflare:
✅ **https://wayserviceltda.com**
✅ **https://www.wayserviceltda.com**

### Apenas WWW:
✅ **https://www.wayserviceltda.com**
↪️ **wayserviceltda.com** → redireciona para www

---

## 💡 RECOMENDAÇÃO

**Use Cloudflare!** É gratuito, leva apenas 15 minutos, e você terá:
- ✅ Controle total do DNS
- ✅ Domínio raiz funcionando (sem www)
- ✅ SSL automático
- ✅ CDN global (site mais rápido)
- ✅ Proteção DDoS básica

**Precisa de ajuda?** Me avise qual opção você quer seguir!
