# Guia de Estruturação do Projeto

## 📁 Estrutura Completa do Repositório

Este documento descreve a estrutura completa do repositório **PDF Text Extractor** e como cada componente foi organizado para facilitar o desenvolvimento, manutenção e deploy no GitHub.

## 🗂️ Árvore de Diretórios

```
pdf-text-extractor/
│
├── .env.example                 # Exemplo de configuração de variáveis de ambiente
├── .gitignore                   # Arquivos e diretórios ignorados pelo Git
├── LICENSE                      # Licença MIT do projeto
├── README.md                    # Documentação principal do projeto
├── GUIA_ESTRUTURACAO.md        # Este arquivo - guia de estruturação
├── requirements.txt             # Dependências Python do projeto
├── setup.py                     # Configuração para instalação do pacote
├── main.py                      # Script principal de linha de comando
│
├── pdf_text_extractor/          # Pacote principal
│   ├── __init__.py             # Inicialização do pacote e exports
│   ├── config.py               # Configurações e templates
│   ├── cleaner.py              # PDFTextCleaner - Motor de limpeza
│   ├── extractor.py            # CleanPDFExtractor - Extrator principal
│   └── batch_processor.py      # PDFBatchProcessor - Processamento em lote
│
├── tests/                       # Testes unitários
│   ├── __init__.py
│   ├── test_cleaner.py         # Testes do PDFTextCleaner
│   ├── test_extractor.py       # Testes do CleanPDFExtractor
│   └── test_batch_processor.py # Testes do PDFBatchProcessor
│
├── examples/                    # Exemplos de uso
│   ├── __init__.py
│   ├── simple_usage.py         # Exemplo de uso simples
│   └── batch_usage.py          # Exemplo de processamento em lote
│
├── data/                        # Diretórios de dados
│   ├── input/                  # PDFs de entrada
│   │   └── .gitkeep
│   └── output/                 # Textos processados
│       └── .gitkeep
│
└── docs/                        # Documentação adicional
    └── API.md                  # Documentação da API
```

## 📋 Descrição dos Arquivos Principais

### Arquivos de Configuração

#### `.env.example`
Arquivo de exemplo com todas as variáveis de ambiente configuráveis. O usuário deve copiar para `.env` e ajustar conforme necessário.

**Variáveis principais:**
- `INPUT_DIR`: Diretório de entrada de PDFs
- `OUTPUT_DIR`: Diretório de saída de textos limpos
- `MIN_TEXT_LENGTH`: Comprimento mínimo de texto
- `EXTRACT_TABLES`: Extrair tabelas (True/False)
- `REMOVE_HEADERS`: Remover cabeçalhos (True/False)
- `NORMALIZE_SPACES`: Normalizar espaços (True/False)
- `OUTPUT_FORMAT`: Formato de saída (txt/json/csv)

#### `.gitignore`
Arquivo que especifica quais arquivos e diretórios devem ser ignorados pelo Git.

**Principais exclusões:**
- Arquivos Python compilados (`__pycache__/`, `*.pyc`)
- Ambientes virtuais (`venv/`, `.venv/`)
- Variáveis de ambiente (`.env`)
- Dados de entrada/saída (`data/input/*.pdf`, `data/output/*`)
- Logs e temporários

#### `requirements.txt`
Lista todas as dependências Python necessárias para o projeto.

**Dependências principais:**
- `pdfplumber>=0.11.0` - Extração de texto de PDFs
- `pandas>=2.0.0` - Manipulação de dados
- `python-dotenv>=1.0.0` - Gerenciamento de variáveis de ambiente

#### `setup.py`
Configuração para instalação do pacote via pip.

**Permite:**
- Instalação via `pip install -e .`
- Distribuição no PyPI
- Definição de metadados do projeto

### Código Fonte

#### `main.py`
Script principal que fornece interface de linha de comando (CLI).

**Funcionalidades:**
- Processamento de arquivo único
- Processamento em lote de diretórios
- Suporte a templates pré-configurados
- Configuração via argumentos de linha de comando

**Exemplos de uso:**
```bash
# Arquivo único
python main.py documento.pdf -o saida.txt

# Diretório completo
python main.py data/input -o data/output --directory

# Com template
python main.py documento.pdf -o saida.txt --template legal_docs
```

#### `pdf_text_extractor/__init__.py`
Inicializa o pacote e exporta as classes principais.

**Exports:**
- `PDFTextCleaner`
- `CleanPDFExtractor`
- `PDFBatchProcessor`

#### `pdf_text_extractor/config.py`
Gerencia configurações e templates pré-definidos.

**Recursos:**
- Carregamento de variáveis de ambiente
- Templates pré-configurados (legal_docs, corporate, nlp_ready)
- Configurações padrão

#### `pdf_text_extractor/cleaner.py`
Motor de limpeza com algoritmos regex avançados.

**Principais métodos:**
- `clean_text()`: Aplica todos os filtros de limpeza
- `remove_headers()`: Remove cabeçalhos repetitivos
- `normalize_spaces()`: Normaliza espaçamento
- `get_cleaning_stats()`: Calcula estatísticas de limpeza

**Padrões regex implementados:**
- Remoção de numeração de páginas
- Filtro de cabeçalhos (RELINT, SEPOL, SSINTE)
- Limpeza de códigos de documento
- Normalização de espaços e quebras de linha

#### `pdf_text_extractor/extractor.py`
Extrator principal que coordena a extração e limpeza.

**Principais métodos:**
- `extract_text_from_pdf()`: Extrai texto bruto
- `extract_clean_text()`: Extrai e limpa texto
- `extract_with_metadata()`: Extrai texto com metadados

**Recursos:**
- Extração página por página
- Suporte a tabelas
- Preservação opcional de estrutura
- Geração de metadados

#### `pdf_text_extractor/batch_processor.py`
Processador em lote para múltiplos documentos.

**Principais métodos:**
- `process_directory()`: Processa todos os PDFs de um diretório
- `_process_single_file()`: Processa um único arquivo
- `_generate_report()`: Gera relatório consolidado

**Recursos:**
- Processamento recursivo de subdiretórios
- Geração de relatórios em JSON e CSV
- Estatísticas detalhadas de performance
- Tratamento robusto de erros

### Testes

#### `tests/test_cleaner.py`
Testes unitários para o módulo de limpeza.

**Testes implementados:**
- Remoção de numeração de páginas
- Remoção de cabeçalhos
- Remoção de códigos de documento
- Normalização de espaços
- Cálculo de estatísticas

### Exemplos

#### `examples/simple_usage.py`
Demonstra uso básico com um único arquivo.

**Mostra:**
- Inicialização do extrator
- Extração de texto limpo
- Salvamento do resultado

#### `examples/batch_usage.py`
Demonstra processamento em lote.

**Mostra:**
- Configuração personalizada
- Processamento de múltiplos arquivos
- Análise de resultados e estatísticas

## 🚀 Preparação para Push no GitHub

### Passo 1: Inicializar Repositório Git

```bash
cd pdf-text-extractor
git init
```

### Passo 2: Adicionar Arquivos

```bash
git add .
```

### Passo 3: Fazer Commit Inicial

```bash
git commit -m "Initial commit: PDF Text Extractor - Sistema Avançado de Processamento Documental"
```

### Passo 4: Criar Repositório no GitHub

1. Acesse [GitHub](https://github.com)
2. Clique em "New repository"
3. Nome: `pdf-text-extractor`
4. Descrição: "Sistema Avançado de Processamento Documental - Extrator de Texto Limpo para PDFs"
5. Escolha: Public ou Private
6. **NÃO** inicialize com README, .gitignore ou LICENSE (já temos esses arquivos)

### Passo 5: Conectar e Fazer Push

```bash
# Adicionar remote
git remote add origin https://github.com/seu-usuario/pdf-text-extractor.git

# Renomear branch para main (se necessário)
git branch -M main

# Fazer push
git push -u origin main
```

## 📦 Instalação e Uso Após Clone

### Para Desenvolvedores

```bash
# Clonar repositório
git clone https://github.com/seu-usuario/pdf-text-extractor.git
cd pdf-text-extractor

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt

# Instalar em modo desenvolvimento
pip install -e .

# Configurar variáveis de ambiente
cp .env.example .env
# Editar .env conforme necessário

# Executar testes
pytest tests/
```

### Para Usuários

```bash
# Clonar repositório
git clone https://github.com/seu-usuario/pdf-text-extractor.git
cd pdf-text-extractor

# Instalar
pip install -r requirements.txt

# Usar
python main.py seu_documento.pdf -o saida.txt
```

## 🔧 Manutenção e Desenvolvimento

### Adicionar Nova Funcionalidade

1. Criar branch: `git checkout -b feature/nova-funcionalidade`
2. Desenvolver e testar
3. Commit: `git commit -m "Add: nova funcionalidade"`
4. Push: `git push origin feature/nova-funcionalidade`
5. Criar Pull Request no GitHub

### Atualizar Dependências

```bash
# Atualizar requirements.txt
pip freeze > requirements.txt

# Commit
git add requirements.txt
git commit -m "Update: dependencies"
git push
```

### Criar Release

```bash
# Tag de versão
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

## 📊 Métricas de Qualidade do Código

### Cobertura de Testes

```bash
pytest --cov=pdf_text_extractor tests/
```

### Análise de Código

```bash
# Flake8 (linting)
flake8 pdf_text_extractor/

# Black (formatação)
black pdf_text_extractor/

# MyPy (type checking)
mypy pdf_text_extractor/
```

## 🎯 Checklist Pré-Push

- [ ] Todos os testes passando
- [ ] Código formatado com Black
- [ ] Sem erros de linting (Flake8)
- [ ] README.md atualizado
- [ ] Versão atualizada em `__init__.py` e `setup.py`
- [ ] CHANGELOG.md atualizado (se existir)
- [ ] .gitignore configurado corretamente
- [ ] Variáveis sensíveis em .env (não commitadas)
- [ ] Exemplos funcionando
- [ ] Documentação atualizada

## 📝 Boas Práticas

1. **Commits Semânticos**: Use prefixos como `Add:`, `Fix:`, `Update:`, `Refactor:`
2. **Branches**: Use feature branches para novas funcionalidades
3. **Pull Requests**: Sempre revise código antes de merge
4. **Testes**: Mantenha cobertura de testes acima de 80%
5. **Documentação**: Mantenha README e docstrings atualizados
6. **Versionamento**: Siga [Semantic Versioning](https://semver.org/)

## 🔗 Links Úteis

- [Documentação pdfplumber](https://github.com/jsvine/pdfplumber)
- [Guia Python Packaging](https://packaging.python.org/)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

**Estrutura criada com base nas melhores práticas de desenvolvimento Python e organização de projetos open source.**
