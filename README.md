# Ì≥ö Automa√ß√£o de Busca e Precifica√ß√£o de Livros

## Ì≥ñ Descri√ß√£o

Este projeto √© uma **automa√ß√£o inteligente** desenvolvida em Python que realiza buscas automatizadas de livros em m√∫ltiplas fontes online, coletando informa√ß√µes de pre√ßo e disponibilidade.

### ÌæØ Objetivo

O sistema busca livros em duas fontes principais:
1. **Project Gutenberg** - Biblioteca digital com mais de 70.000 livros gratuitos
2. **Books to Scrape** - Site de demonstra√ß√£o para pr√°tica de web scraping

## Ìª†Ô∏è Tecnologias Utilizadas

- Python 3.x
- Selenium WebDriver
- Pandas
- openpyxl

## Ì≥¶ Instala√ß√£o

### 1. Clone o reposit√≥rio
```bash
git clone https://github.com/Delson24/Automacao-de-Busca-Precificacao-de-Livros.git
cd Automacao-de-Busca-Precificacao-de-Livros
```

### 2. Crie ambiente virtual
```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows Git Bash
```

### 3. Instale as depend√™ncias
```bash
pip install selenium pandas openpyxl
```

### 4. Configure o ChromeDriver
- Baixe o [ChromeDriver](https://chromedriver.chromium.org/)
- Adicione ao PATH do sistema

## Ì∫Ä Como Usar

### 1. Prepare a planilha de entrada
Crie um arquivo `produtos.xlsx` com as colunas:
- `nome` - Nome do livro
- `autor` - Autor do livro
- `categoria` - Categoria (ex: Classics, Fiction, etc.)

### 2. Execute o notebook
Abra `automacao.ipynb` no Jupyter Notebook e execute as c√©lulas em ordem.

### 3. Resultado
O arquivo `produtosAtualizados.xlsx` ser√° gerado com:
- `preco` - Pre√ßo do livro (ou 0 se gratuito)
- `link` - Link para o livro

## Ì≥ä Exemplo

**Entrada:**
| nome | autor | categoria |
|------|-------|-----------|
| Frankenstein | Mary Shelley | Classics |

**Sa√≠da:**
| nome | autor | categoria | preco | link |
|------|-------|-----------|-------|------|
| Frankenstein | Mary Shelley | Classics | 0 | https://www.gutenberg.org/ebooks/84 |

## Ì¥ç Funcionamento
1. L√™ a lista de livros do arquivo Excel
2. Para cada livro:
   - Busca no Project Gutenberg
   - Se n√£o encontrar, busca no Books to Scrape
   - Salva o resultado na planilha
3. Gera arquivo atualizado

## ‚ö†Ô∏è Observa√ß√µes
- Respeite os termos de uso dos sites ao fazer scraping
- O ChromeDriver deve estar instalado e no PATH

## Ì¥ù Contribui√ß√µes
Contribui√ß√µes s√£o bem-vindas! Sinta-se √† vontade para abrir issues ou pull requests.

## Ì≥Ñ Licen√ßa
Este projeto est√° sob a licen√ßa MIT.

## Ì±§ Autor
Delson - [GitHub](https://github.com/Delson24)
