# 📋 COLA - IPs E CONFIGURAÇÕES PARA COPIAR

## 🌐 REGISTROS DNS - GOOGLE WORKSPACE

### ➕ 4 REGISTROS A (copie um por vez)

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**Como adicionar:**
1. Google Domains/Admin → wayserviceltda.com → DNS
2. Criar novo registro
3. Tipo: **A**
4. Host: **@**
5. Valor: **(cole um IP acima)**
6. TTL: **3600**
7. Salvar
8. **Repetir para os 4 IPs**

---

### ➕ 1 REGISTRO CNAME

**⚠️ ANTES DE COLAR:** Substitua `SEU-USUARIO` pelo seu usuário do GitHub

```
SEU-USUARIO.github.io.
```

**⚠️ MANTENHA O PONTO FINAL** (exemplo: `brunoamorim.github.io.`)

**Como adicionar:**
1. Criar novo registro
2. Tipo: **CNAME**
3. Host: **www**
4. Valor: **(cole acima com SEU usuário)**
5. TTL: **3600**
6. Salvar

---

## 🔧 COMANDO GIT (copiar e colar no terminal)

**⚠️ ANTES DE EXECUTAR:** Substitua `SEU-USUARIO` pelo seu usuário do GitHub

```powershell
git remote add origin https://github.com/SEU-USUARIO/wayservice-site.git; git push -u origin main
```

**Exemplo com usuário brunoamorim:**
```powershell
git remote add origin https://github.com/brunoamorim/wayservice-site.git; git push -u origin main
```

---

## ✅ CONFIGURAÇÃO GITHUB PAGES

1. **URL do repositório:** `https://github.com/SEU-USUARIO/wayservice-site`
2. **Settings → Pages**
3. **Source:**
   - Branch: `main`
   - Folder: `/ (root)`
4. **Custom domain:**
   ```
   wayserviceltda.com
   ```
5. **Enforce HTTPS:** ☑️ (marcar após DNS propagar)

---

## 🧪 TESTAR DNS (após 2-4 horas)

```powershell
nslookup wayserviceltda.com
```

**Resultado esperado:**
```
Addresses:  185.199.108.153
           185.199.109.153
           185.199.110.153
           185.199.111.153
```

---

## 🔗 LINKS IMPORTANTES

**Criar repositório GitHub:**
https://github.com/new

**Configurar DNS Google Domains:**
https://domains.google.com

**Configurar DNS Google Workspace:**
https://admin.google.com

**Verificar propagação DNS:**
https://dnschecker.org/

**Documentação GitHub Pages:**
https://docs.github.com/en/pages

---

## 📞 TOKEN GITHUB (se precisar de autenticação)

**Criar token:**
https://github.com/settings/tokens

**Permissões necessárias:**
- ✅ `repo` (full control of private repositories)

**Como usar:**
- Quando o git pedir senha, cole o TOKEN (não sua senha normal)

---

## ⏱️ TIMELINE

```
⏰ Agora          → Criar repo GitHub (2 min)
⏰ Agora + 3 min  → git push (1 min)
⏰ Agora + 6 min  → Ativar Pages (3 min)
⏰ Agora + 11 min → Configurar DNS (5 min)
⏰ Agora + 2-4h   → DNS propaga
⏰ Depois da prop → Ativar HTTPS (2 min)
✅ SITE ONLINE!
```

---

## 🎯 RESULTADO FINAL

✅ https://wayserviceltda.com
✅ https://www.wayserviceltda.com
✅ SSL automático (HTTPS com cadeado verde)
✅ Deploy automático (próximos git push)
✅ 100% gratuito
✅ Profissional

---

## 📄 ARQUIVOS CRIADOS

- ✅ **CNAME** - Configuração de domínio
- 📘 **COMANDOS_FINAIS.md** - Passo a passo completo
- 🌐 **GUIA_DNS_GOOGLE.md** - Configuração DNS detalhada
- 🚀 **DEPLOY_COMANDOS.md** - Comandos Git explicados
- 📋 **COLA.md** - Este arquivo (para copiar/colar rápido)

---

## 🏁 COMECE AGORA

1. Abra: https://github.com/new
2. Crie repo público: `wayservice-site`
3. Volte aqui e execute o comando git
4. Ative GitHub Pages
5. Configure DNS no Google
6. Aguarde propagação (2-4h)
7. Ative HTTPS
8. ✅ SITE ONLINE!
