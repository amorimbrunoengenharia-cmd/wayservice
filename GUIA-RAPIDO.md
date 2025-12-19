# Guia Rápido - Como Colocar o Site no Ar

## ⚡ Passos Principais

### 1️⃣ Criar Conta no Squarespace
- Acesse: https://www.squarespace.com
- Crie sua conta ou faça login
- Escolha "Criar um Site"

### 2️⃣ Adicionar o Código do Site

**No Squarespace:**
1. Vá em **Settings** (Configurações)
2. Clique em **Advanced** (Avançado)
3. Clique em **Code Injection** (Injeção de Código)
4. Na seção **Header**:
   - Cole TODO o conteúdo do arquivo `index.html`
   - Depois, adicione o CSS entre tags `<style>`:
   ```html
   <style>
   [Cole aqui todo o conteúdo do styles.css]
   </style>
   ```

### 3️⃣ Conectar seu Domínio do Google

**No Squarespace:**
1. Vá em **Settings** > **Domains**
2. Clique em **Use a Domain You Own**
3. Digite seu domínio (ex: wayservice.com.br)
4. Anote os endereços IP que o Squarespace mostrar

**No Google Admin (admin.google.com):**
1. Vá em **Domínios**
2. Clique no seu domínio
3. Vá em **DNS** > **Gerenciar registros personalizados**
4. Adicione os registros A que o Squarespace forneceu:
   
   | Tipo | Host | Valor |
   |------|------|-------|
   | A | @ | [IP do Squarespace] |
   | A | www | [IP do Squarespace] |

### 4️⃣ Aguardar e Testar

- Aguarde 2-24 horas para o DNS propagar
- Acesse seu domínio e veja o site no ar!
- Teste em celular e computador

## ✏️ Personalizações Importantes

Antes de publicar, atualize no arquivo `index.html`:

- [ ] **Telefone**: Linha 108 - `(00) 0000-0000`
- [ ] **Email**: Linha 109 - `contato@wayservice.com.br`
- [ ] **Endereço**: Linha 110 - `Seu endereço aqui`
- [ ] **Ano no rodapé**: Linha 134 - `2024`

## ⚠️ Importante: Manter o Email Funcionando

**NUNCA delete os registros MX do Google!**

Os registros MX são necessários para o email funcionar. No Google Domains, certifique-se de manter:

- ASPMX.L.GOOGLE.COM (prioridade 1)
- ALT1.ASPMX.L.GOOGLE.COM (prioridade 5)
- ALT2.ASPMX.L.GOOGLE.COM (prioridade 5)
- ALT3.ASPMX.L.GOOGLE.COM (prioridade 10)
- ALT4.ASPMX.L.GOOGLE.COM (prioridade 10)

## 📚 Documentação Completa

Para instruções detalhadas, consulte: **[DEPLOYMENT.md](DEPLOYMENT.md)**

## 🆘 Problemas Comuns

**Site não abre?**
- Aguarde mais tempo (até 48h)
- Limpe o cache do navegador
- Teste em modo anônimo

**Email parou de funcionar?**
- Verifique se os registros MX estão corretos
- Não delete nenhum registro do Google

**Visual está quebrado?**
- Verifique se copiou TODO o CSS
- Certifique-se que está dentro das tags `<style>`

## 💡 Dica Pro

Use este site para verificar se o DNS propagou:
https://www.whatsmydns.net

Digite seu domínio e selecione "A" para ver se os IPs do Squarespace aparecem globalmente.
