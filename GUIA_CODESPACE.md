# 🚀 Guia de Uso do GitHub Codespace - PDF-Extractor

**Bem-vindo ao ambiente de desenvolvimento do PDF-Extractor!**

Este guia explica como acessar e utilizar o repositório através do GitHub Codespaces, com todas as ferramentas e dependências pré-configuradas.

---

## 📋 Índice

1. [O que é um Codespace?](#o-que-é-um-codespace)
2. [Como Criar seu Codespace](#como-criar-seu-codespace)
3. [Primeiro Acesso](#primeiro-acesso)
4. [Explorando os Relatórios](#explorando-os-relatórios)
5. [Testando o Sistema](#testando-o-sistema)
6. [Desenvolvendo Novas Features](#desenvolvendo-novas-features)
7. [Troubleshooting](#troubleshooting)

---

## O que é um Codespace?

**GitHub Codespaces** é um ambiente de desenvolvimento completo na nuvem que roda no navegador ou VS Code. Benefícios:

- ✅ **Zero configuração**: Tudo pré-instalado (Python, Tesseract, bibliotecas)
- ✅ **Acesso de qualquer lugar**: Apenas internet necessária
- ✅ **Performance**: Máquinas potentes na nuvem
- ✅ **Consistência**: Mesmo ambiente para toda a equipe
- ✅ **Gratuito**: 60 horas/mês para contas pessoais

---

## Como Criar seu Codespace

### Passo 1: Acesse o Repositório no GitHub

Navegue até: `https://github.com/jricardosouza/PDF-Extractor`

### Passo 2: Criar o Codespace

1. Clique no botão verde **Code**
2. Selecione a aba **Codespaces**
3. Clique em **Create codespace on [nome-do-branch]**

![Criar Codespace](https://docs.github.com/assets/cb-138303/images/help/codespaces/new-codespace-button.png)

### Passo 3: Aguarde a Configuração

- ⏱️ **Primeira vez**: 3-5 minutos (instala tudo)
- ⏱️ **Próximas vezes**: 10-30 segundos (ambiente salvo)

Você verá:
```
🚀 Configurando ambiente de desenvolvimento PDF-Extractor...
📦 Atualizando sistema...
🔍 Instalando Tesseract OCR...
🖼️ Instalando dependências de processamento de imagem...
...
✅ Ambiente de desenvolvimento configurado com sucesso!
```

### Passo 4: VS Code no Navegador

O VS Code abrirá automaticamente no navegador com:
- **Terminal** integrado na parte inferior
- **Explorer** lateral com arquivos do projeto
- **Extensões Python** já instaladas e configuradas

---

## Primeiro Acesso

### 1. Verificar Configuração

Abra o terminal (`` Ctrl+` `` ou **View** → **Terminal**) e execute:

```bash
# Verificar versão Python
python --version
# Esperado: Python 3.11.x

# Verificar Tesseract OCR
tesseract --version
# Esperado: tesseract 4.x ou 5.x

# Verificar dependências instaladas
pip list | grep -E "pdfplumber|pandas|pytesseract"
```

### 2. Estrutura do Projeto

Navegue pelos arquivos no Explorer (lateral esquerda):

```
PDF-Extractor/
├── 📄 ANALISE_COMPLETA_REPOSITORIO.md    ← COMECE AQUI!
├── 📄 ANALISE_VIABILIDADE_OCR_REGEX.md   ← Roadmap OCR
├── 📄 GUIA_CODESPACE.md                  ← Você está aqui
├── 📄 README.md                           ← Documentação do usuário
│
├── 📁 pdf_text_extractor/                 ← Código-fonte principal
│   ├── __init__.py
│   ├── cleaner.py                         ← Motor de limpeza
│   ├── extractor.py                       ← Extrator principal
│   ├── batch_processor.py                 ← Processamento em lote
│   └── config.py                          ← Configurações
│
├── 📁 examples/                           ← Exemplos de uso
│   ├── simple_usage.py
│   └── batch_usage.py
│
├── 📁 tests/                              ← Testes unitários
│   └── test_cleaner.py
│
├── 📁 data/                               ← Diretórios de dados
│   ├── input/                             ← Coloque PDFs aqui
│   └── output/                            ← Resultados vão aqui
│
└── 📁 .devcontainer/                      ← Configuração Codespace
    ├── devcontainer.json
    ├── setup.sh
    └── README.md
```

### 3. Configurar Variáveis de Ambiente

O arquivo `.env` já foi criado automaticamente. Para personalizá-lo:

```bash
# Editar no terminal
nano .env

# OU abrir no editor
code .env
```

Configurações importantes:
```bash
INPUT_DIR=data/input
OUTPUT_DIR=data/output
LOG_LEVEL=INFO
MIN_TEXT_LENGTH=50
EXTRACT_TABLES=True
```

---

## Explorando os Relatórios

### 📊 Relatório 1: Análise Completa do Repositório

**Arquivo**: `ANALISE_COMPLETA_REPOSITORIO.md`

**Conteúdo**:
- ✅ Análise detalhada de 876 linhas de código
- ✅ Avaliação de qualidade (Nota: 7.7/10)
- ✅ Identificação de vulnerabilidades de segurança
- ✅ Recomendações priorizadas (Alta/Média/Baixa)
- ✅ Roadmap de melhorias

**Como ler**:
```bash
# No terminal
cat ANALISE_COMPLETA_REPOSITORIO.md | less

# OU abrir no editor (recomendado para markdown formatado)
code ANALISE_COMPLETA_REPOSITORIO.md
```

**Dica**: Use `Ctrl+Shift+V` no VS Code para ver preview formatado do markdown.

### 🔮 Relatório 2: Viabilidade OCR e Regex

**Arquivo**: `ANALISE_VIABILIDADE_OCR_REGEX.md`

**Conteúdo**:
- ✅ Análise técnica de implementação OCR
- ✅ Comparativo de bibliotecas (Tesseract vs PaddleOCR vs EasyOCR)
- ✅ Roadmap detalhado (5 semanas, 108 horas)
- ✅ Padrões regex para documentos brasileiros (CPF, CNPJ, etc.)
- ✅ Arquitetura proposta com diagramas Mermaid
- ✅ Decisão: **GO ✅** - Implementação recomendada

**Destaques**:
- 📈 ROI positivo em menos de 1 mês
- 🎯 Acurácia esperada: 85-92%
- ⚡ Ganho de produtividade: 70-85%

---

## Testando o Sistema

### Teste 1: Processamento Básico (Sem PDFs)

Executar testes unitários existentes:

```bash
# Todos os testes
pytest tests/ -v

# Com cobertura
pytest --cov=pdf_text_extractor tests/

# Apenas um arquivo
pytest tests/test_cleaner.py -v
```

**Resultado esperado**:
```
tests/test_cleaner.py::TestPDFTextCleaner::test_initialization PASSED
tests/test_cleaner.py::TestPDFTextCleaner::test_remove_page_numbers PASSED
tests/test_cleaner.py::TestPDFTextCleaner::test_remove_headers PASSED
...
========== 12 passed in 0.43s ==========
```

### Teste 2: Processamento com PDF de Exemplo

**Criar um PDF de teste**:

Opção 1 - Usar exemplo simples:
```bash
# Criar exemplo de texto
cat > data/input/teste.txt << 'EOF'
--- PÁGINA 1 ---
RELINT S81 n° 001/2025
Data: 25 FEV 2025

Conteúdo importante do documento.
Nome: João da Silva
CPF: 123.456.789-00
Telefone: (98) 98765-4321
--- PÁGINA 2 ---
RELINT S81 n° 001/2025
Continuação do documento...
EOF

# Nota: Para PDF real, você precisará fazer upload de um arquivo
```

Opção 2 - Upload de PDF real:
```bash
# No Codespace, arrastar e soltar PDF para data/input/
# OU usar comando de upload do terminal
```

**Executar processamento**:

```bash
# Processar arquivo único
python main.py data/input/seu_pdf.pdf -o data/output/resultado.txt

# Com template para documentos legais
python main.py data/input/seu_pdf.pdf -o data/output/resultado.txt --template legal_docs

# Processar diretório inteiro
python main.py data/input -o data/output --directory

# Ver ajuda completa
python main.py --help
```

### Teste 3: Uso Programático

```bash
# Executar exemplo simples
python examples/simple_usage.py

# Executar exemplo em lote
python examples/batch_usage.py
```

**OU** criar seu próprio script:

```python
# meu_teste.py
from pdf_text_extractor import CleanPDFExtractor

# Criar extrator
extractor = CleanPDFExtractor()

# Extrair texto limpo
clean_text = extractor.extract_clean_text("data/input/teste.pdf")

print(f"📄 Texto extraído: {len(clean_text)} caracteres")
print(clean_text[:500])  # Primeiros 500 caracteres
```

---

## Desenvolvendo Novas Features

### Workflow de Desenvolvimento

#### 1. Criar Branch de Feature

```bash
# Para implementar OCR (exemplo)
git checkout -b feature/ocr-implementation

# Para corrigir bug
git checkout -b fix/security-validation

# Para melhorias
git checkout -b improvement/add-brazilian-regex-patterns
```

#### 2. Desenvolvimento com TDD (Recomendado)

```bash
# 1. Escrever teste que falha
# tests/test_ocr_processor.py
def test_ocr_extracts_text_from_image():
    processor = OCRProcessor()
    text = processor.extract("test_image.png")
    assert "expected text" in text

# 2. Executar teste (deve falhar)
pytest tests/test_ocr_processor.py -v

# 3. Implementar funcionalidade
# pdf_text_extractor/ocr_processor.py
class OCRProcessor:
    def extract(self, image_path):
        # Implementação...
        pass

# 4. Executar teste novamente (deve passar)
pytest tests/test_ocr_processor.py -v

# 5. Refatorar se necessário
```

#### 3. Verificar Qualidade

```bash
# Formatação automática
black pdf_text_extractor/ tests/
isort pdf_text_extractor/ tests/

# Linting
flake8 pdf_text_extractor/ tests/

# Type checking
mypy pdf_text_extractor/

# Análise de segurança
bandit -r pdf_text_extractor/

# Cobertura de testes
pytest --cov=pdf_text_extractor --cov-report=html tests/
# Abrir htmlcov/index.html no navegador
```

#### 4. Commit e Push

```bash
# Adicionar arquivos
git add .

# Commit com mensagem descritiva
git commit -m "feat: adicionar suporte básico para OCR com Tesseract

- Implementar OCRProcessor com Tesseract engine
- Adicionar pré-processamento de imagens
- Adicionar detecção automática de PDFs escaneados
- Testes unitários para OCRProcessor
- Documentação do novo módulo

Refs: ANALISE_VIABILIDADE_OCR_REGEX.md - Fase 1"

# Push para branch remoto
git push -u origin feature/ocr-implementation
```

#### 5. Criar Pull Request

```bash
# Via GitHub CLI (já instalado no Codespace)
gh pr create \
  --title "feat: Implementar suporte OCR (Fase 1)" \
  --body "## Resumo
Implementação da Fase 1 do roadmap OCR conforme ANALISE_VIABILIDADE_OCR_REGEX.md

## Mudanças
- ✅ OCRProcessor básico com Tesseract
- ✅ Detecção de PDFs escaneados
- ✅ Pré-processamento de imagens
- ✅ Testes unitários (cobertura 85%)

## Testes
\`\`\`bash
pytest tests/test_ocr_processor.py -v
\`\`\`

## Checklist
- [x] Código formatado (black + isort)
- [x] Linting passou (flake8)
- [x] Testes passando (pytest)
- [x] Documentação atualizada
- [x] Sem vulnerabilidades (bandit)"
```

---

## Trabalhando com os Relatórios de Análise

### Implementar Recomendações de Alta Prioridade

Conforme `ANALISE_COMPLETA_REPOSITORIO.md`, as prioridades são:

#### 1. Implementar Validação de Segurança (8-12 horas)

```bash
# Criar arquivo de validadores
touch pdf_text_extractor/validators.py

# Editar
code pdf_text_extractor/validators.py
```

Copiar código do relatório (seção 9, item 1) e adaptar.

#### 2. Adicionar Testes Abrangentes (40-60 horas)

```bash
# Criar arquivos de teste
touch tests/test_extractor.py
touch tests/test_batch_processor.py
touch tests/test_config.py
touch tests/test_integration.py

# Criar fixtures
mkdir -p tests/fixtures
# Adicionar PDFs de teste em tests/fixtures/
```

#### 3. Configurar CI/CD (4-6 horas)

```bash
# Criar workflow GitHub Actions
mkdir -p .github/workflows
touch .github/workflows/ci.yml

# Editar
code .github/workflows/ci.yml
```

Copiar configuração YAML do relatório (seção 9, item 3).

### Implementar Roadmap OCR

Conforme `ANALISE_VIABILIDADE_OCR_REGEX.md`:

```bash
# Criar estrutura OCR
mkdir -p pdf_text_extractor/ocr/engines
mkdir -p pdf_text_extractor/regex

# Criar arquivos base
touch pdf_text_extractor/ocr/__init__.py
touch pdf_text_extractor/ocr/ocr_processor.py
touch pdf_text_extractor/ocr/image_preprocessor.py
touch pdf_text_extractor/ocr/confidence_analyzer.py

touch pdf_text_extractor/ocr/engines/__init__.py
touch pdf_text_extractor/ocr/engines/base_engine.py
touch pdf_text_extractor/ocr/engines/tesseract_engine.py

touch pdf_text_extractor/regex/__init__.py
touch pdf_text_extractor/regex/regex_extractor.py
touch pdf_text_extractor/regex/patterns_br.py
touch pdf_text_extractor/regex/validators.py

# Seguir roadmap: Fase 1 → Fase 2 → Fase 3 → Fase 4
```

**Copiar código dos exemplos** fornecidos no relatório de viabilidade (seção 5.3).

---

## Troubleshooting

### Problema: "Módulo não encontrado"

```bash
# Reinstalar dependências
pip install -r requirements.txt

# OU instalar módulo específico
pip install nome-do-modulo
```

### Problema: "Tesseract não funciona"

```bash
# Verificar instalação
tesseract --version

# Se não estiver instalado
sudo apt-get update
sudo apt-get install tesseract-ocr tesseract-ocr-por

# Testar
tesseract --list-langs
# Deve listar: por (português)
```

### Problema: "Permissão negada"

```bash
# Para arquivos
chmod +x arquivo.sh

# Para diretórios
chmod -R 755 data/
```

### Problema: "Git push falha"

```bash
# Verificar branch correta
git branch

# Deve estar em branch que começa com 'claude/'
# Se não estiver, criar branch correta:
git checkout -b claude/meu-branch-$(date +%s)

# Configurar upstream
git push -u origin nome-do-branch
```

### Problema: "Codespace lento"

```bash
# Verificar uso de recursos
htop

# Limpar cache
rm -rf .cache __pycache__ **/__pycache__

# Reconstruir Codespace (opção drástica)
# GitHub → Codespaces → [...] → Delete
# Depois criar novo Codespace
```

### Problema: "Arquivos não aparecem"

```bash
# Atualizar Explorer
# Pressionar F5 no VS Code

# OU listar no terminal
ls -la
```

---

## 💡 Dicas de Produtividade

### Atalhos Úteis

| Atalho | Ação |
|--------|------|
| `` Ctrl+` `` | Abrir/fechar terminal |
| `Ctrl+Shift+P` | Command Palette |
| `Ctrl+P` | Buscar arquivo |
| `Ctrl+Shift+F` | Buscar em todos os arquivos |
| `Ctrl+/` | Comentar/descomentar |
| `Ctrl+Shift+V` | Preview markdown |
| `F2` | Renomear símbolo |
| `F12` | Ir para definição |

### Extensões Recomendadas (Já Instaladas)

- ✅ **Python** (Microsoft) - IntelliSense, debugging
- ✅ **Pylance** - Type checking avançado
- ✅ **Black Formatter** - Formatação automática
- ✅ **Ruff** - Linter moderno e rápido
- ✅ **GitHub Copilot** - Sugestões de código AI (se disponível)

### Snippets Customizados

Criar snippet para testes:

1. `Ctrl+Shift+P` → **Preferences: Configure User Snippets**
2. Selecionar **python.json**
3. Adicionar:

```json
{
  "Pytest Test Function": {
    "prefix": "deftest",
    "body": [
      "def test_${1:name}(self):",
      "    \"\"\"${2:Description}\"\"\"",
      "    # Arrange",
      "    ${3:pass}",
      "    ",
      "    # Act",
      "    ${4:pass}",
      "    ",
      "    # Assert",
      "    assert ${5:condition}$0"
    ],
    "description": "Create pytest test function"
  }
}
```

Agora digite `deftest` + Tab para criar teste rapidamente!

---

## 📚 Recursos Adicionais

### Documentação do Projeto
- **README.md**: Guia do usuário final
- **ANALISE_COMPLETA_REPOSITORIO.md**: Análise técnica (leia primeiro!)
- **ANALISE_VIABILIDADE_OCR_REGEX.md**: Roadmap OCR detalhado
- **.devcontainer/README.md**: Detalhes do ambiente

### Links Externos
- [Python Official Docs](https://docs.python.org/3/)
- [pytest Documentation](https://docs.pytest.org/)
- [pdfplumber GitHub](https://github.com/jsvine/pdfplumber)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
- [GitHub Codespaces Docs](https://docs.github.com/codespaces)

### Comunidade
- **Issues**: https://github.com/jricardosouza/PDF-Extractor/issues
- **Discussions**: https://github.com/jricardosouza/PDF-Extractor/discussions
- **Pull Requests**: https://github.com/jricardosouza/PDF-Extractor/pulls

---

## 🎓 Próximos Passos Sugeridos

1. **✅ Ler**: `ANALISE_COMPLETA_REPOSITORIO.md` (15-20 min)
2. **✅ Ler**: `ANALISE_VIABILIDADE_OCR_REGEX.md` (20-30 min)
3. **✅ Explorar**: Código-fonte em `pdf_text_extractor/` (30 min)
4. **✅ Testar**: Executar testes e exemplos (15 min)
5. **✅ Priorizar**: Escolher uma recomendação de Alta Prioridade
6. **✅ Implementar**: Seguir TDD e boas práticas
7. **✅ Commitar**: Fazer commit e push
8. **✅ PR**: Abrir Pull Request para revisão

---

## 🤝 Como Contribuir

### Tipos de Contribuições

- 🐛 **Bug Fixes**: Corrigir problemas identificados
- ✨ **Features**: Implementar funcionalidades do roadmap
- 📝 **Documentação**: Melhorar ou corrigir documentação
- 🧪 **Testes**: Aumentar cobertura de testes
- 🔒 **Segurança**: Implementar validações e correções

### Processo

1. **Issue First**: Criar ou escolher uma issue
2. **Branch**: Criar branch descritiva (`feat/`, `fix/`, `docs/`)
3. **Develop**: Implementar com testes
4. **Quality**: Passar por linting, formatação, testes
5. **PR**: Abrir Pull Request com descrição clara
6. **Review**: Aguardar revisão e fazer ajustes
7. **Merge**: Após aprovação, merge para main

---

## 📞 Suporte

### Problemas com Codespace
- **Documentação**: https://docs.github.com/codespaces
- **Status**: https://www.githubstatus.com/

### Problemas com Projeto
- **Issues**: https://github.com/jricardosouza/PDF-Extractor/issues
- **Email**: [seu-email-aqui]

### Dúvidas Técnicas
- Consultar relatórios de análise
- Verificar documentação das bibliotecas
- Abrir discussion no GitHub

---

**🎉 Pronto! Você está configurado para desenvolver no PDF-Extractor!**

Bom código! 🚀

---

**Última atualização**: 06 de Novembro de 2025
**Versão**: 1.0
