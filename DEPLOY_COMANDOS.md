# 🚀 COMANDOS PARA DEPLOY - GITHUB PAGES

## ✅ PRÉ-REQUISITO
1. Criar repositório **PÚBLICO** no GitHub: https://github.com/new
   - Nome sugerido: `wayservice-site`
   - ⚠️ **IMPORTANTE:** Marcar como **PUBLIC** (GitHub Pages gratuito só funciona em repos públicos)
   - ✅ **NÃO** adicionar README, .gitignore ou licença (já temos)

## 📋 COMANDOS PARA EXECUTAR (copie e cole no terminal)

```powershell
# 1. Inicializar Git (se ainda não estiver)
git init

# 2. Configurar seu nome e email (substitua pelos seus dados)
git config user.name "Seu Nome"
git config user.email "seu-email@exemplo.com"

# 3. Adicionar todos os arquivos
git add .

# 4. Fazer primeiro commit
git commit -m "Deploy inicial - Site Way Service"

# 5. Renomear branch para main (GitHub usa main como padrão)
git branch -M main

# 6. Adicionar repositório remoto (SUBSTITUA SEU-USUARIO pelo seu usuário do GitHub)
git remote add origin https://github.com/SEU-USUARIO/wayservice-site.git

# 7. Fazer push para GitHub
git push -u origin main
```

## 🔑 AUTENTICAÇÃO

Quando executar `git push`, o GitHub vai pedir autenticação:

**Opção 1: Personal Access Token (Recomendado)**
1. Acesse: https://github.com/settings/tokens
2. Clique em "Generate new token" → "Classic"
3. Marque: `repo` (controle total de repositórios privados)
4. Copie o token gerado
5. No terminal, quando pedir senha, cole o TOKEN (não a senha da conta)

**Opção 2: GitHub CLI (Mais Fácil)**
```powershell
# Instalar GitHub CLI
winget install GitHub.cli

# Fazer login
gh auth login

# Depois pode usar git normalmente
```

## ⚙️ ATIVAR GITHUB PAGES

Após o push bem-sucedido:

1. Acesse seu repositório no GitHub
2. Vá em **Settings** (Configurações)
3. No menu lateral esquerdo, clique em **Pages**
4. Em **Source**, selecione:
   - Branch: `main`
   - Folder: `/ (root)`
5. Clique em **Save**
6. ✅ Aguarde 2-3 minutos

**Seu site estará temporariamente em:**
`https://SEU-USUARIO.github.io/wayservice-site/`

## 🌐 CONFIGURAR DOMÍNIO PERSONALIZADO

Após ativar GitHub Pages:

1. Ainda na página "Pages" (GitHub Settings)
2. Em **Custom domain**, digite: `wayserviceltda.com`
3. Clique em **Save**
4. ⚠️ Vai aparecer erro "DNS check unsuccessful" - NORMAL!
5. Configure o DNS no Google (veja GUIA_DNS_GOOGLE.md)
6. Aguarde 24-48h para propagação completa
7. ✅ Marque "Enforce HTTPS" quando disponível

## 🎯 RESUMO RÁPIDO

```bash
cd "C:\Users\Usuario\Desktop\Particular Bruno Amorim\4. Projeto WayService\Site WayService"
git init
git add .
git commit -m "Deploy inicial - Site Way Service"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/wayservice-site.git
git push -u origin main
```

## 🆘 PROBLEMAS COMUNS

**Erro: "remote origin already exists"**
```bash
git remote remove origin
git remote add origin https://github.com/SEU-USUARIO/wayservice-site.git
```

**Erro: "authentication failed"**
- Use Personal Access Token, não senha
- Ou instale GitHub CLI: `gh auth login`

**Erro: "repository not found"**
- Verifique se criou o repositório no GitHub
- Confirme que usou o nome correto
- Confirme que o repositório é PÚBLICO
