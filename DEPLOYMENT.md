# Guia de Deploy - WayService no Squarespace

Este documento fornece instruções detalhadas para fazer o deploy do site WayService no Squarespace usando o domínio comprado através do Google Workspace.

## Pré-requisitos

- Conta Squarespace ativa
- Domínio comprado através do Google Workspace
- Arquivos do site (index.html e styles.css)

## Parte 1: Configuração Inicial no Squarespace

### 1.1. Criar ou Acessar sua Conta Squarespace

1. Acesse [www.squarespace.com](https://www.squarespace.com)
2. Faça login ou crie uma nova conta
3. Clique em "Create a Website" ou "Criar um Site"

### 1.2. Escolher Template e Modo de Edição

Como você já tem o código HTML/CSS pronto, existem duas abordagens:

#### Opção A: Usando Code Injection (Mais Simples)
1. Escolha qualquer template básico do Squarespace
2. Vá para **Settings > Advanced > Code Injection**
3. Cole o conteúdo do `index.html` na seção **Header**
4. Cole o conteúdo do `styles.css` entre tags `<style>` e `</style>` também no **Header**

#### Opção B: Usando Developer Mode (Mais Controle)
1. O Squarespace Developer Mode permite usar HTML/CSS customizado
2. Acesse [developers.squarespace.com](https://developers.squarespace.com)
3. Siga o guia para configurar o Developer Platform
4. Use o Squarespace CLI para fazer upload dos arquivos

**Recomendação**: Para este projeto, a Opção A é mais simples e adequada.

## Parte 2: Conectar o Domínio do Google Workspace

### 2.1. Preparar o Domínio no Google Workspace

1. Acesse [admin.google.com](https://admin.google.com)
2. Faça login com sua conta de administrador do Google Workspace
3. Vá para **Domínios** no menu lateral

### 2.2. Obter Informações de DNS do Squarespace

1. No Squarespace, vá para **Settings > Domains**
2. Clique em **Use a Domain You Own** ou **Usar um Domínio que Você Possui**
3. Digite seu domínio (ex: wayservice.com.br)
4. Escolha **Connect a Domain You Already Own**
5. O Squarespace fornecerá registros DNS específicos

### 2.3. Configurar DNS no Google Domains

1. Volte ao Google Admin Console
2. Clique no seu domínio
3. Vá para **DNS** > **Manage custom records** ou **Gerenciar registros personalizados**
4. Adicione os registros DNS fornecidos pelo Squarespace:

   **Registros A típicos do Squarespace:**
   ```
   Tipo: A
   Host: @
   Valor: 198.185.159.144
   TTL: 3600

   Tipo: A
   Host: @
   Valor: 198.185.159.145
   TTL: 3600

   Tipo: A
   Host: www
   Valor: 198.49.23.145
   TTL: 3600

   Tipo: A
   Host: www
   Valor: 198.49.23.144
   TTL: 3600
   ```

   **Nota**: Use os IPs específicos fornecidos pelo Squarespace na sua interface, pois podem variar.

5. Se necessário, adicione registros CNAME:
   ```
   Tipo: CNAME
   Host: www
   Valor: ext-cust.squarespace.com
   TTL: 3600
   ```

### 2.4. Verificar a Propriedade do Domínio

1. O Squarespace pode solicitar verificação de propriedade
2. Adicione o registro TXT fornecido no Google Domains:
   ```
   Tipo: TXT
   Host: @
   Valor: [código fornecido pelo Squarespace]
   TTL: 3600
   ```

## Parte 3: Manter os Serviços do Google Workspace

**IMPORTANTE**: Você precisa manter os registros MX do Google Workspace para continuar usando o email.

### 3.1. Preservar Registros MX

Certifique-se de que os seguintes registros MX permaneçam configurados:

```
Tipo: MX
Host: @
Valor: ASPMX.L.GOOGLE.COM
Prioridade: 1

Tipo: MX
Host: @
Valor: ALT1.ASPMX.L.GOOGLE.COM
Prioridade: 5

Tipo: MX
Host: @
Valor: ALT2.ASPMX.L.GOOGLE.COM
Prioridade: 5

Tipo: MX
Host: @
Valor: ALT3.ASPMX.L.GOOGLE.COM
Prioridade: 10

Tipo: MX
Host: @
Valor: ALT4.ASPMX.L.GOOGLE.COM
Prioridade: 10
```

### 3.2. Outros Registros do Google Workspace

Mantenha também os registros SPF, DKIM e DMARC para segurança de email:

```
Tipo: TXT
Host: @
Valor: v=spf1 include:_spf.google.com ~all

Tipo: TXT
Host: google._domainkey
Valor: [seu valor DKIM do Google]
```

## Parte 4: Tempo de Propagação e Testes

### 4.1. Aguardar Propagação DNS

- A propagação DNS pode levar de 24 a 48 horas
- Geralmente ocorre em algumas horas
- Use ferramentas como [whatsmydns.net](https://www.whatsmydns.net) para verificar

### 4.2. Testar o Site

1. Acesse seu domínio em um navegador
2. Teste em diferentes dispositivos (desktop, tablet, mobile)
3. Verifique todos os links e seções
4. Teste o formulário de contato (veja seção 5.3 para configuração)

### 4.3. Configurar SSL/HTTPS

1. No Squarespace, vá para **Settings > Advanced > SSL**
2. Ative o SSL (geralmente automático após a conexão do domínio)
3. Force HTTPS para todas as páginas

## Parte 5: Personalizações e Ajustes

### 5.1. Atualizar Informações de Contato

No arquivo `index.html`, atualize:
- Telefone: `(00) 0000-0000`
- Email: `contato@wayservice.com.br`
- Endereço físico da empresa
- Horário de atendimento

### 5.2. Adicionar Logo da Empresa

1. Crie uma pasta `images` ou `assets`
2. Adicione o logo da empresa
3. Atualize o HTML para referenciar o logo:
   ```html
   <div class="logo">
       <img src="images/logo.png" alt="WayService Logo">
   </div>
   ```

### 5.3. Configurar Formulário de Contato

O Squarespace oferece integração de formulários. Você tem duas opções:

**Opção A: Usar Form Block do Squarespace (Recomendado)**
1. No editor Squarespace, adicione um **Form Block** na seção de contato
2. Configure os campos:
   - Nome (Text field)
   - Email (Email field)
   - Telefone (Phone field)
   - Mensagem (Text area)
3. Configure notificações por email em **Settings > Email**
4. O Squarespace processará os envios automaticamente

**Opção B: Configurar Form Action Personalizada**
1. Se usar o HTML diretamente, adicione o atributo `action` no formulário
2. Exemplo: `<form action="https://formspree.io/f/seu-id" method="POST">`
3. Ou use serviços como Formspree, FormSubmit, ou Web3Forms
4. Configure o endpoint de acordo com o serviço escolhido

**Nota**: O formulário atual no HTML não tem `action` configurado. Você deve escolher uma das opções acima para que ele funcione.

## Parte 6: SEO e Analytics

### 6.1. Configurar SEO Básico

1. No Squarespace: **Marketing > SEO**
2. Configure:
   - Título do site: "WayService - Construção de Obras Públicas e Industriais"
   - Descrição: "Construtora especializada em obras públicas e industriais"
   - Keywords: "construção, obras públicas, engenharia"

### 6.2. Integrar Google Analytics

1. Crie uma propriedade no [Google Analytics](https://analytics.google.com)
2. No Squarespace: **Settings > Advanced > External API Keys**
3. Cole o ID de acompanhamento do Google Analytics

### 6.3. Adicionar Google Search Console

1. Acesse [Google Search Console](https://search.google.com/search-console)
2. Adicione e verifique seu domínio
3. Envie o sitemap (Squarespace gera automaticamente)

## Parte 7: Manutenção e Atualizações

### 7.1. Backup do Site

- Mantenha cópias dos arquivos HTML/CSS neste repositório Git
- Faça backup regular das configurações do Squarespace
- Documente todas as mudanças

### 7.2. Atualizações de Conteúdo

Para atualizar o conteúdo:
1. Edite os arquivos HTML/CSS localmente
2. Teste as mudanças localmente
3. Faça upload via Code Injection ou Developer Mode
4. Verifique o site em produção

### 7.3. Monitoramento

- Verifique regularmente o Google Analytics
- Monitore o uptime do site
- Responda aos formulários de contato prontamente

## Troubleshooting Comum

### DNS não está propagando
- Verifique se os registros foram salvos corretamente
- Use ferramentas de verificação DNS
- Aguarde até 48 horas

### Email parou de funcionar
- Verifique se os registros MX do Google estão preservados
- Confirme prioridades dos registros MX
- Teste o envio/recebimento de emails

### Site não carrega corretamente
- Limpe o cache do navegador
- Verifique o console do navegador para erros
- Teste em modo anônimo/privado

### SSL não está funcionando
- Aguarde até 24 horas após conectar o domínio
- Verifique as configurações de SSL no Squarespace
- Force HTTPS nas configurações

## Recursos Adicionais

- [Documentação Squarespace](https://support.squarespace.com)
- [Google Workspace Help](https://support.google.com/a)
- [Squarespace Developers](https://developers.squarespace.com)

## Suporte

Para suporte técnico:
- Squarespace: Chat ao vivo ou email support
- Google Workspace: Console de administração > Suporte
- Este projeto: Abra uma issue no GitHub

---

**Data da última atualização**: Dezembro 2025
