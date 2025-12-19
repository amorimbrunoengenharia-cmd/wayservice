# 🚀 Guia para Colocar o Site Way Service Online

## 📋 Opções de Hospedagem

### 1️⃣ **GitHub Pages** (GRATUITO - Recomendado para começar)

#### Vantagens:
- ✅ 100% Gratuito
- ✅ SSL automático (HTTPS)
- ✅ Pode usar domínio personalizado (wayserviceltda.com)
- ✅ Deploy automático ao fazer commit

#### Passo a Passo:

**A. Criar Repositório no GitHub**
1. Acesse [github.com](https://github.com)
2. Clique em "New repository"
3. Nome: `wayservice-site`
4. Marque como "Public"
5. Clique em "Create repository"

**B. Fazer Upload dos Arquivos**

No terminal do VS Code, execute:

```bash
# Inicializar Git no projeto
git init

# Adicionar todos os arquivos
git add .

# Fazer primeiro commit
git commit -m "Deploy inicial do site Way Service"

# Adicionar repositório remoto (substitua SEU-USUARIO pelo seu usuário do GitHub)
git remote add origin https://github.com/SEU-USUARIO/wayservice-site.git

# Enviar arquivos
git branch -M main
git push -u origin main
```

**C. Ativar GitHub Pages**
1. No repositório, vá em "Settings"
2. No menu lateral, clique em "Pages"
3. Em "Source", selecione "main" branch
4. Clique em "Save"
5. Aguarde alguns minutos

✅ Site estará disponível em: `https://SEU-USUARIO.github.io/wayservice-site/`

**D. Configurar Domínio Personalizado (Opcional)**
1. Nas configurações do GitHub Pages, adicione `wayserviceltda.com` em "Custom domain"
2. No painel do seu domínio (onde você comprou), configure:
   - Tipo A: `185.199.108.153`
   - Tipo A: `185.199.109.153`
   - Tipo A: `185.199.110.153`
   - Tipo A: `185.199.111.153`
   - CNAME www: `SEU-USUARIO.github.io`

---

### 2️⃣ **Netlify** (GRATUITO - Deploy mais Fácil)

#### Vantagens:
- ✅ 100% Gratuito
- ✅ Deploy por arrastar e soltar
- ✅ SSL automático
- ✅ Domínio personalizado grátis

#### Passo a Passo:

**A. Via Interface Web (Mais Simples)**
1. Acesse [netlify.com](https://www.netlify.com)
2. Crie uma conta (pode usar GitHub)
3. Clique em "Add new site" > "Deploy manually"
4. Arraste TODA a pasta do site para a área
5. Aguarde o deploy

✅ Site online em segundos com URL tipo: `random-name.netlify.app`

**B. Configurar Domínio Personalizado**
1. No painel do Netlify, vá em "Domain settings"
2. Clique em "Add custom domain"
3. Digite `wayserviceltda.com`
4. Configure os DNS no painel do seu domínio:
   - Tipo A: `75.2.60.5` (Netlify Load Balancer)
   - CNAME www: `nome-do-site.netlify.app`

---

### 3️⃣ **Vercel** (GRATUITO - Muito Rápido)

#### Vantagens:
- ✅ 100% Gratuito
- ✅ Deploy extremamente rápido
- ✅ SSL automático
- ✅ Boa integração com Git

#### Passo a Passo:

**A. Via CLI**
```bash
# Instalar Vercel CLI
npm install -g vercel

# Fazer deploy (na pasta do projeto)
vercel

# Seguir instruções no terminal
```

**B. Via Interface Web**
1. Acesse [vercel.com](https://vercel.com)
2. Crie conta (pode usar GitHub)
3. Clique em "Add New Project"
4. Conecte seu GitHub ou faça upload manual
5. Deploy automático

---

### 4️⃣ **Hospedagem Tradicional** (PAGO - cPanel/FTP)

#### Para usar com wayserviceltda.com:

**A. Se você já tem hospedagem contratada:**

1. Acesse o painel cPanel do seu provedor
2. Vá em "File Manager"
3. Navegue até a pasta `public_html`
4. Faça upload de TODOS os arquivos:
   - index.html
   - projetos.html
   - contato.html
   - orcamento.html
   - todos os projeto-*.html
   - styles.css
   - script.js
   - projetos.js
   - projetos.json
   - Pasta img/ completa
   - Pasta logo/ completa
   - sitemap.xml
   - robots.txt

**B. Via FTP (FileZilla):**

1. Baixe [FileZilla](https://filezilla-project.org/)
2. Configure conexão:
   - Host: ftp.wayserviceltda.com
   - Usuário: (fornecido pela hospedagem)
   - Senha: (fornecida pela hospedagem)
   - Porta: 21
3. Arraste todos os arquivos para `public_html/`

---

## 🔧 Configurações Importantes Antes do Deploy

### 1. Verificar URLs Absolutas

Se for hospedar em subpasta (ex: github.io/wayservice-site/), você precisa ajustar os caminhos.

**Criar arquivo `config.js`:**
```javascript
// Se estiver em subpasta, adicione '/wayservice-site'
// Se estiver no domínio raiz, deixe vazio
const BASE_PATH = '';

// Exemplo para GitHub Pages em subpasta:
// const BASE_PATH = '/wayservice-site';
```

### 2. Atualizar Links se Necessário

Apenas se for usar subpasta (GitHub Pages sem domínio personalizado):
- Mudar `src="img/..."` para `src="${BASE_PATH}/img/..."`
- Mudar `href="projetos.html"` para `href="${BASE_PATH}/projetos.html"`

### 3. Testar Localmente Antes

```bash
# Instalar servidor local simples
npm install -g http-server

# Rodar na pasta do projeto
http-server

# Abrir no navegador: http://localhost:8080
```

---

## ✅ Checklist Pré-Deploy

- [ ] Todos os arquivos HTML estão corretos
- [ ] Todas as imagens estão otimizadas
- [ ] projetos.json está atualizado
- [ ] sitemap.xml contém todas as páginas
- [ ] robots.txt está configurado
- [ ] Testado localmente
- [ ] Links internos funcionando
- [ ] Formulários de contato configurados
- [ ] Google Analytics configurado (se aplicável)

---

## 🎯 Recomendação

**Para começar agora:** Use **Netlify** (opção mais simples)

1. Acesse netlify.com
2. Arraste a pasta do site
3. Site online em 30 segundos!

**Para uso profissional:** Configure o domínio wayserviceltda.com apontando para o Netlify

---

## 🆘 Precisa de Ajuda?

Me avise qual opção você quer usar e eu posso:
- Gerar os comandos específicos
- Ajustar configurações necessárias
- Configurar integração com Git
- Automatizar deploys futuros

