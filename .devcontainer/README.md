# DevContainer Configuration

Este diretório contém a configuração do ambiente de desenvolvimento para o PDF-Extractor otimizado para GitHub Codespaces.

## 🚀 Início Rápido

### Usando GitHub Codespaces

1. **Abra o repositório no GitHub**
2. Clique em **Code** → **Codespaces** → **Create codespace on [branch]**
3. Aguarde a criação automática do ambiente (2-5 minutos)
4. O ambiente será configurado automaticamente com todas as dependências

### Usando VS Code Local

1. Instale a extensão **Remote - Containers**
2. Abra a pasta do projeto no VS Code
3. Pressione `F1` → **Remote-Containers: Reopen in Container**
4. Aguarde a construção do container

## 📦 O que está incluído?

### Base
- **Python 3.11** (ambiente completo)
- **Git** + **GitHub CLI**
- **Tesseract OCR** com suporte a português

### Extensões VS Code
- Python (Pylance, Black, Flake8, isort)
- Ruff (linter moderno)
- YAML, TOML, Markdown
- GitHub Copilot (se disponível)

### Bibliotecas Python
#### Core (Instaladas automaticamente)
- `pdfplumber` - Extração de PDF
- `pandas` - Manipulação de dados
- `python-dotenv` - Variáveis de ambiente
- `openpyxl` - Suporte Excel
- `tabulate` - Formatação de tabelas

#### Desenvolvimento
- `pytest` + `pytest-cov` - Testes e cobertura
- `black` + `isort` - Formatação de código
- `flake8` + `mypy` - Linting e type checking
- `bandit` + `safety` - Análise de segurança

#### OCR (Pré-configuradas para desenvolvimento futuro)
- `pytesseract` - Interface Python para Tesseract
- `pdf2image` - Conversão PDF → Imagem
- `Pillow` - Processamento de imagens
- `opencv-python` - Visão computacional

## 🔧 Configuração

### Arquivo .env

O script de setup cria automaticamente um arquivo `.env` baseado no `.env.example`. Configure conforme necessário:

```bash
# Editar configurações
nano .env
```

### Portas

As seguintes portas são encaminhadas automaticamente:
- **5000**: Flask (se usar API REST)
- **8000**: FastAPI (se usar API REST)

## 📁 Estrutura de Diretórios

Os seguintes diretórios são criados automaticamente:
```
data/
├── input/      # PDFs de entrada
└── output/     # Resultados processados
logs/           # Arquivos de log
.cache/         # Cache de processamento
tests/
└── fixtures/   # Arquivos de teste
```

## 🧪 Testes

### Executar todos os testes
```bash
pytest tests/ -v
```

### Com cobertura
```bash
pytest --cov=pdf_text_extractor --cov-report=html tests/
```

### Testes específicos
```bash
pytest tests/test_cleaner.py -v
```

## 🛠️ Comandos Úteis

### Formatação de código
```bash
# Black (formatador)
black pdf_text_extractor/ tests/

# isort (organizar imports)
isort pdf_text_extractor/ tests/
```

### Linting
```bash
# Flake8
flake8 pdf_text_extractor/ tests/

# mypy (type checking)
mypy pdf_text_extractor/

# Bandit (segurança)
bandit -r pdf_text_extractor/
```

### Verificação de dependências
```bash
# Verificar vulnerabilidades
safety check

# Verificar atualizações
pip list --outdated
```

## 🐛 Troubleshooting

### Tesseract não funciona
```bash
# Verificar instalação
tesseract --version

# Reinstalar se necessário
sudo apt-get install --reinstall tesseract-ocr tesseract-ocr-por
```

### Módulo não encontrado
```bash
# Reinstalar dependências
pip install -r requirements.txt
```

### Permissões
```bash
# Dar permissão para diretórios
chmod -R 755 data/ logs/
```

## 📚 Recursos Adicionais

- **README.md**: Documentação principal do projeto
- **ANALISE_COMPLETA_REPOSITORIO.md**: Análise técnica detalhada
- **ANALISE_VIABILIDADE_OCR_REGEX.md**: Roadmap de implementação OCR

## 🔄 Atualizar Ambiente

Se o `devcontainer.json` ou `setup.sh` forem atualizados:

1. **Codespaces**: Delete e recrie o Codespace
2. **Local**: `F1` → **Remote-Containers: Rebuild Container**

## 💡 Dicas

- Use `Ctrl+Shift+P` para acessar comandos do VS Code
- Ative o formatação automática ao salvar (já configurado)
- Use `pytest --lf` para executar apenas testes que falharam
- Consulte os relatórios de análise antes de modificar código

## 🆘 Suporte

Para problemas com o ambiente de desenvolvimento:
1. Verifique os logs em `/tmp/devcontainer-setup.log`
2. Abra uma issue no GitHub
3. Consulte a documentação oficial do DevContainers

---

**Última atualização**: 06 de Novembro de 2025
