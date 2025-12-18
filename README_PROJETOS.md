# Sistema de Galeria Dinâmica de Projetos - Way Service

## 📁 Estrutura de Arquivos

Este sistema transforma a seção estática de "Projetos" em uma galeria dinâmica gerenciada por JSON.

### Arquivos do Sistema:

- **`projetos.json`** - Arquivo de dados com todos os projetos
- **`projetos.js`** - Script que renderiza os cards e gerencia o lightbox
- **`projetos.html`** - Página de projetos (já configurada)
- **`styles.css`** - Estilos (já possui CSS do lightbox + contador)

---

## 🖼️ Organização de Imagens

### Regra Importante:
Cada projeto tem sua própria pasta dentro de `img/`.

#### Estrutura de Pastas:
```
img/
├── forum-auriflama/
│   ├── capa.jpg
│   ├── foto1.jpg
│   ├── foto2.jpg
│   ├── foto3.jpg
│   └── foto4.jpg
├── lojas-americanas/
│   ├── capa.jpg
│   ├── foto1.jpg
│   ├── foto2.jpg
│   └── foto3.jpg
├── infraestrutura-industrial/
│   ├── capa.jpg
│   ├── foto1.jpg
│   ├── foto2.jpg
│   ├── foto3.jpg
│   ├── foto4.jpg
│   └── foto5.jpg
└── ... (outros projetos)
```

---

## ➕ Como Adicionar um Novo Projeto

### Passo 1: Criar a Pasta
Crie uma pasta dentro de `img/` com o nome do projeto (use kebab-case):

```bash
img/nova-obra/
```

### Passo 2: Adicionar as Fotos
Coloque todas as fotos do projeto dentro da pasta criada:

```
img/nova-obra/
├── capa.jpg       (imagem de capa)
├── foto1.jpg
├── foto2.jpg
├── foto3.jpg
└── foto4.jpg
```

### Passo 3: Editar o projetos.json
Abra o arquivo `projetos.json` e adicione um novo objeto no array:

```json
{
  "id": "nova-obra",
  "titulo": "Nome do Projeto",
  "categoria": "comercial",
  "tipo_autoria": "empresa",
  "responsavel_tecnico": "WayService Engenharia",
  "imagemCapa": "img/nova-obra/capa.jpg",
  "descricao": "Descrição completa do projeto...",
  "localizacao": "Cidade/Estado",
  "area": "500 m²",
  "ano": "2024",
  "badge": "Concluído",
  "galeria": [
    "img/nova-obra/foto1.jpg",
    "img/nova-obra/foto2.jpg",
    "img/nova-obra/foto3.jpg",
    "img/nova-obra/foto4.jpg"
  ]
}
```

**Sobre Acervo Técnico:**
- Use `"tipo_autoria": "empresa"` para obras executadas pela WayService
- Use `"tipo_autoria": "acervo_pessoal"` para obras executadas pessoalmente pelos engenheiros
- O campo `responsavel_tecnico` pode ser:
  - `"WayService Engenharia"` (obras da empresa)
  - `"Eng. Bruno"` (acervo pessoal)
  - `"Eng. José Sergio"` (acervo pessoal)
  - `"Eng. Bruno & Eng. José Sergio"` (acervo conjunto)

### Passo 4: Salvar e Atualizar
Salve o arquivo `projetos.json` e recarregue a página. O novo projeto aparecerá automaticamente!

---

## 🏷️ Categorias Disponíveis

- `"comercial"` - Projetos comerciais e corporativos
- `"obras_publicas"` - Obras públicas e institucionais
- `"industrial"` - Projetos industriais
- `"infraestrutura"` - Infraestrutura crítica
- `"varejo"` - Projetos de varejo
- `"manutencao"` - Manutenção e reparos

Cada categoria tem seu próprio gradiente de cores e ícone.

---

## 🎨 Campos do JSON

### Campos Obrigatórios:
- `id` - Identificador único (mesmo nome da pasta)
- `titulo` - Nome do projeto
- `categoria` - Uma das categorias listadas acima
- `imagemCapa` - Caminho da imagem de capa
- `descricao` - Descrição do projeto
- `galeria` - Array com os caminhos das fotos

### Campos Opcionais:
- `tipo_autoria` - "empresa" (padrão) ou "acervo_pessoal"
- `responsavel_tecnico` - Nome do responsável (ex: "Eng. Bruno", "WayService Engenharia")
- `localizacao` - Cidade/Estado do projeto
- `area` - Área construída (ex: "1.500 m²")
- `ano` - Ano de conclusão (ex: "2024")
- `badge` - Status do projeto (padrão: "Concluído")

### 📋 Sistema de Acervo Técnico:

O sistema diferencia obras executadas pela empresa (WayService) de obras executadas pessoalmente pelos engenheiros sócios. Isso é totalmente legal e comum no mercado de engenharia.

**Quando usar cada tipo:**

1. **`tipo_autoria: "empresa"`** - Obras executadas pela WayService CNPJ
   - `responsavel_tecnico: "WayService Engenharia"`
   - Badge não aparece (é o padrão)

2. **`tipo_autoria: "acervo_pessoal"`** - Obras de experiências anteriores dos sócios
   - `responsavel_tecnico: "Eng. Bruno"` ou `"Eng. José Sergio"` ou `"Eng. Bruno & Eng. José Sergio"`
   - Badge azul aparece no card: "Acervo: Eng. Bruno"
   - Informação também exibida no lightbox

**Visual do Badge:**
- Cor azul sutil (diferente do verde da empresa)
- Ícone de certificado
- Posicionado no canto superior esquerdo do card
- Hover com efeito de destaque

---

## 🎯 Funcionalidades

### 1. Renderização Dinâmica
- Os cards são gerados automaticamente a partir do JSON
- Não precisa editar o HTML manualmente

### 2. Lightbox com Galeria
- Ao clicar em "Ver Álbum", abre o lightbox em tela cheia
- Navegação com setas (← →) ou botões
- Contador de fotos (1 / 5)
- Suporte a teclado (ESC para fechar, ← → para navegar)

### 3. Filtros e Busca
- Filtros por categoria (se implementados no HTML)
- Busca por texto no título, descrição ou localização

### 4. Animações
- Cards aparecem com animação reveal-scale
- Delays alternados para efeito cascata
- Contador de projetos animado

---

## 🚀 Exemplo Completo

```json
{
  "id": "residencia-elis",
  "titulo": "Residência Elis - Reforma Completa",
  "categoria": "residencial",
  "imagemCapa": "img/residencia-elis/capa.jpg",
  "descricao": "Reforma completa de interiores com modernização de acabamentos, adequação elétrica e hidráulica. Projeto executado em 60 dias com zero atrasos.",
  "localizacao": "Londrina/PR",
  "area": "250 m²",
  "ano": "2024",
  "badge": "Concluído",
  "galeria": [
    "img/residencia-elis/sala.jpg",
    "img/residencia-elis/cozinha.jpg",
    "img/residencia-elis/banheiro.jpg",
    "img/residencia-elis/quarto.jpg",
    "img/residencia-elis/fachada.jpg"
  ]
}
```

---

## 📝 Notas Importantes

1. **Nomes de Pastas**: Use kebab-case (minúsculas e hífens): `meu-projeto`, não `Meu Projeto`
2. **Formatos de Imagem**: Use JPG ou PNG (recomendado: JPG com qualidade 80-85%)
3. **Tamanho das Imagens**: Recomendado 1920x1080px para galeria
4. **Ordem no JSON**: Os projetos aparecem na ordem em que estão no arquivo
5. **GitHub Pages**: O sistema funciona perfeitamente em hospedagem estática

---

## 🔧 Troubleshooting

### Projeto não aparece?
- Verifique se o JSON está válido (use jsonlint.com)
- Confira se os caminhos das imagens estão corretos
- Veja o Console do navegador (F12) para erros

### Imagem não carrega?
- Verifique o caminho no JSON
- Confirme que o arquivo existe na pasta
- Teste o caminho diretamente no navegador

### Lightbox não abre?
- Verifique se `projetos.js` está carregado
- Veja se há erros no Console (F12)
- Confira se o botão tem o atributo `data-project-id`

---

## 🎉 Pronto!

Agora você pode gerenciar todo o portfólio editando apenas o arquivo `projetos.json` e adicionando fotos nas pastas correspondentes. Simples, organizado e profissional!
