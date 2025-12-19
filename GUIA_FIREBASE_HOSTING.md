# 🌐 HOSPEDAR SITE NO GOOGLE WORKSPACE/GOOGLE CLOUD

## 📋 OPÇÕES DISPONÍVEIS

### ❌ Google Sites (Novo Modelo)
**NÃO RECOMENDADO** para seu caso porque:
- Não aceita HTML/CSS/JS personalizado
- Requer reconstruir tudo no editor visual
- Você perderia todo o código que já tem

---

### ✅ OPÇÃO 1: FIREBASE HOSTING (Recomendado) 🔥

**Por que Firebase?**
- ✅ Parte do Google Cloud
- ✅ 100% GRATUITO (plano Spark)
- ✅ SSL automático (HTTPS)
- ✅ CDN global super rápido
- ✅ Deploy automático
- ✅ Domínio personalizado (wayserviceltda.com)
- ✅ Funciona perfeitamente com sites HTML estáticos

**Limites gratuitos:**
- 10 GB de armazenamento
- 360 MB/dia de transferência
- Mais que suficiente para seu site!

---

## 🚀 GUIA COMPLETO - FIREBASE HOSTING

### **PASSO 1: Instalar Firebase CLI**

No terminal do VS Code, execute:

```powershell
# Instalar Node.js (se não tiver)
winget install OpenJS.NodeJS

# Instalar Firebase CLI
npm install -g firebase-tools
```

---

### **PASSO 2: Login no Firebase**

```powershell
firebase login
```

Isso vai abrir seu navegador para fazer login com sua conta Google (a mesma do Google Workspace).

---

### **PASSO 3: Inicializar Firebase no Projeto**

No terminal, dentro da pasta do site:

```powershell
# Ir para a pasta do projeto
cd "C:\Users\Usuario\Desktop\Particular Bruno Amorim\4. Projeto WayService\Site WayService"

# Inicializar Firebase
firebase init hosting
```

**Respostas para as perguntas:**

1. **"Please select an option:"** → `Create a new project`
2. **"Please specify a unique project ID:"** → `wayservice-site` (ou outro nome único)
3. **"What do you want to use as your public directory?"** → Pressione Enter (usa a pasta atual)
4. **"Configure as a single-page app?"** → `N` (No)
5. **"Set up automatic builds and deploys with GitHub?"** → `N` (No)
6. **"File index.html already exists. Overwrite?"** → `N` (No)

---

### **PASSO 4: Configurar firebase.json**

O Firebase criou um arquivo `firebase.json`. Vamos ajustá-lo:

```json
{
  "hosting": {
    "public": ".",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**",
      "**/*.py",
      "**/*.md",
      "CNAME",
      ".git"
    ],
    "headers": [
      {
        "source": "**/*.@(jpg|jpeg|gif|png|webp|svg|ico)",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "max-age=31536000"
          }
        ]
      },
      {
        "source": "**/*.@(css|js)",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "max-age=31536000"
          }
        ]
      }
    ],
    "cleanUrls": true
  }
}
```

---

### **PASSO 5: Deploy para Firebase**

```powershell
firebase deploy
```

✅ **Pronto!** Seu site estará online em:
```
https://wayservice-site.web.app
https://wayservice-site.firebaseapp.com
```

---

### **PASSO 6: Conectar Domínio Personalizado**

#### A. No Firebase Console:

1. Acesse: **https://console.firebase.google.com/**
2. Selecione seu projeto: **wayservice-site**
3. No menu lateral, vá em **Hosting**
4. Clique em **"Add custom domain"** (Adicionar domínio personalizado)
5. Digite: `wayserviceltda.com`
6. Clique em **Continue**

Firebase vai mostrar os registros DNS necessários.

#### B. Configurar DNS no Squarespace:

Firebase vai pedir 2 tipos de registros:

**1. Registro A (para wayserviceltda.com):**
```
Type: A
Host: @
Value: (IP fornecido pelo Firebase)
TTL: 3600
```

**2. Registro TXT (verificação):**
```
Type: TXT
Host: @
Value: (código fornecido pelo Firebase)
TTL: 3600
```

**3. Registro A (para www.wayserviceltda.com):**
```
Type: A
Host: www
Value: (IP fornecido pelo Firebase)
TTL: 3600
```

#### C. No Squarespace:

1. Login: **https://pt.squarespace.com/**
2. Vá em **Domínios** → **wayserviceltda.com**
3. Clique em **DNS Settings**
4. Adicione os registros fornecidos pelo Firebase
5. Salvar

#### D. Verificar no Firebase:

1. Volte ao Firebase Console
2. Clique em **"Verify"** (Verificar)
3. Aguarde a verificação (pode levar alguns minutos)
4. ✅ SSL será ativado automaticamente em 24h

---

## 📋 OPÇÃO 2: GOOGLE CLOUD STORAGE

Se preferir usar Google Cloud Storage direto:

### **PASSO 1: Criar Bucket**

1. Acesse: **https://console.cloud.google.com/storage**
2. Clique em **"Create bucket"**
3. Nome: `wayserviceltda.com` (exatamente o domínio)
4. Location type: **Multi-region**
5. Storage class: **Standard**
6. Access control: **Fine-grained**
7. Create

### **PASSO 2: Upload dos Arquivos**

1. Entre no bucket criado
2. Clique em **"Upload files"** ou **"Upload folder"**
3. Selecione todos os arquivos do seu site
4. Upload

### **PASSO 3: Tornar Público**

1. No bucket, vá em **Permissions**
2. Clique em **"Add members"**
3. New members: `allUsers`
4. Role: **Storage Object Viewer**
5. Save

### **PASSO 4: Configurar Website**

1. No bucket, vá em **"Edit website configuration"**
2. Index page: `index.html`
3. Error page: `index.html`
4. Save

### **PASSO 5: DNS (Squarespace)**

No Squarespace, adicione:

```
Type: CNAME
Host: @
Value: c.storage.googleapis.com.
TTL: 3600

Type: CNAME
Host: www
Value: c.storage.googleapis.com.
TTL: 3600
```

⚠️ **Limitação:** Google Cloud Storage não fornece SSL automático para domínios personalizados sem Cloud Load Balancer (pago).

---

## 🎯 COMPARAÇÃO

| Feature | Firebase Hosting | Cloud Storage | GitHub Pages |
|---------|------------------|---------------|--------------|
| **Custo** | ✅ Gratuito | ⚠️ Pago após 1GB/mês | ✅ Gratuito |
| **SSL Automático** | ✅ Sim | ❌ Não (requer LB) | ✅ Sim |
| **Deploy Fácil** | ✅ CLI simples | ⚠️ Upload manual | ✅ Git push |
| **CDN Global** | ✅ Incluso | ⚠️ Separado | ✅ Incluso |
| **Google Workspace** | ✅ Integrado | ✅ Integrado | ❌ Não |
| **Velocidade** | ⚡ Muito rápido | ⚡ Rápido | ⚡ Rápido |

---

## 💡 RECOMENDAÇÃO FINAL

### Para Google Workspace/Cloud: **FIREBASE HOSTING** 🔥

**Por quê?**
1. ✅ Parte oficial do Google Cloud
2. ✅ 100% gratuito para seu tamanho de site
3. ✅ SSL automático
4. ✅ Deploy super fácil (1 comando)
5. ✅ CDN global incluído
6. ✅ Integração perfeita com Google Workspace
7. ✅ Deploy automático com `firebase deploy`

---

## 📋 COMANDOS RESUMIDOS - FIREBASE

```powershell
# 1. Instalar (uma vez)
npm install -g firebase-tools

# 2. Login (uma vez)
firebase login

# 3. Inicializar (uma vez)
cd "C:\Users\Usuario\Desktop\Particular Bruno Amorim\4. Projeto WayService\Site WayService"
firebase init hosting

# 4. Deploy (toda vez que atualizar o site)
firebase deploy

# 5. Ver site ao vivo
firebase open hosting:site
```

---

## ⏱️ TIMELINE

```
⏰ Agora          → Instalar Firebase CLI (5 min)
⏰ +5 min         → Login e init (5 min)
⏰ +10 min        → Primeiro deploy (2 min)
⏰ +12 min        → Site online no Firebase!
⏰ +15 min        → Adicionar domínio personalizado (5 min)
⏰ +20 min        → Configurar DNS no Squarespace (5 min)
⏰ +2-24h         → Propagação DNS + SSL automático
✅ SITE ONLINE COM DOMÍNIO PERSONALIZADO!
```

---

## 🆘 TROUBLESHOOTING

### ❌ "npm: command not found"
**Solução:** Instale Node.js primeiro
```powershell
winget install OpenJS.NodeJS
```
Feche e reabra o terminal.

### ❌ "Firebase command not found"
**Solução:** Reinstale Firebase CLI
```powershell
npm install -g firebase-tools
```

### ❌ "Permission denied"
**Solução:** Execute como administrador ou use:
```powershell
npm install -g firebase-tools --force
```

### ❌ "Project ID already exists"
**Solução:** Use outro nome único:
```
wayservice-oficial
wayservice-ltda
wayservice-2024
```

---

## 📞 LINKS ÚTEIS

**Firebase Console:**
- https://console.firebase.google.com/

**Firebase CLI Docs:**
- https://firebase.google.com/docs/cli

**Firebase Hosting Docs:**
- https://firebase.google.com/docs/hosting

**Squarespace DNS:**
- https://pt.squarespace.com/

---

## ✅ PRÓXIMOS PASSOS

**Me avise quando estiver pronto e eu executo os comandos para você!**

Os passos serão:
1. ✅ Instalar Firebase CLI
2. ✅ Login no Firebase
3. ✅ Init do projeto
4. ✅ Deploy inicial
5. ✅ Configurar domínio personalizado

**Quer que eu comece agora?** 🚀
