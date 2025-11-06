#!/bin/bash

# Configuração de segurança e tratamento de erros
# Para em caso de erro, variáveis não definidas e erros em pipes
set -euo pipefail

# Função para log seguro (previne injeção de comandos)
log() {
    printf '%s\n' "$1"
}

# Função para verificar sucesso de comandos
check_success() {
    if [ $? -ne 0 ]; then
        log "❌ Erro: $1"
        exit 1
    fi
}

log "🚀 Configurando ambiente de desenvolvimento PDF-Extractor..."
log ""

# Atualizar sistema
log "📦 Atualizando sistema..."
sudo apt-get update -y
check_success "Falha ao atualizar sistema"

# Instalar Tesseract OCR (para futura implementação)
log "🔍 Instalando Tesseract OCR..."
sudo apt-get install -y tesseract-ocr tesseract-ocr-por libtesseract-dev
check_success "Falha ao instalar Tesseract OCR"

# Instalar dependências de processamento de imagem
log "🖼️ Instalando dependências de processamento de imagem..."
sudo apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    poppler-utils
check_success "Falha ao instalar dependências de imagem"

# Criar ambiente virtual Python
log "🐍 Configurando ambiente Python..."
python -m pip install --upgrade pip
check_success "Falha ao atualizar pip"

pip install --upgrade setuptools wheel
check_success "Falha ao atualizar setuptools/wheel"

# Instalar dependências do projeto
log "📚 Instalando dependências do projeto..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    check_success "Falha ao instalar dependências do projeto"
else
    log "⚠️ Arquivo requirements.txt não encontrado, pulando..."
fi

# Instalar dependências de desenvolvimento
log "🛠️ Instalando ferramentas de desenvolvimento..."
pip install \
    pytest>=7.4.0 \
    pytest-cov>=4.1.0 \
    pytest-mock>=3.11.0 \
    black>=23.0.0 \
    flake8>=6.0.0 \
    mypy>=1.5.0 \
    isort>=5.12.0 \
    bandit>=1.7.5 \
    safety>=2.3.5
check_success "Falha ao instalar ferramentas de desenvolvimento"

# Instalar dependências OCR (para desenvolvimento futuro)
log "🔮 Instalando dependências OCR (pré-configuração)..."
pip install \
    pytesseract>=0.3.10 \
    pdf2image>=1.16.3 \
    Pillow>=10.0.0 \
    opencv-python-headless>=4.8.0
check_success "Falha ao instalar dependências OCR"

# Criar diretórios necessários
log "📁 Criando estrutura de diretórios..."
mkdir -p data/input data/output logs .cache tests/fixtures
check_success "Falha ao criar diretórios"

# Configurar git
log "🔧 Configurando Git..."
git config --global core.autocrlf input
git config --global pull.rebase false

# Criar arquivo .env se não existir
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
    log "⚙️ Criando arquivo .env..."
    cp .env.example .env
    log ""
    log "⚠️  ATENÇÃO - SEGURANÇA:"
    log "   O arquivo .env foi criado com valores padrão."
    log "   IMPORTANTE: Revise e altere todos os valores sensíveis antes de usar!"
    log "   NUNCA commite o arquivo .env para o repositório."
    log "   Dados sensíveis incluem: senhas, tokens, chaves API, etc."
    log ""
fi

# Verificar instalações
log ""
log "🔍 Verificando instalações..."
log "Python: $(python --version)"
log "Pip: $(pip --version)"
log "Tesseract: $(tesseract --version | head -1)"
log "Git: $(git --version)"

# Executar testes se existirem
if [ -d "tests" ] && [ -n "$(ls -A tests)" ]; then
    log ""
    log "🧪 Executando testes..."
    # Não para em erro de testes (|| true)
    pytest tests/ -v --tb=short || log "⚠️ Alguns testes falharam. Revise os resultados acima."
fi

log ""
log "✅ Ambiente de desenvolvimento configurado com sucesso!"
log ""
log "📖 Próximos passos:"
log "  1. ⚠️  IMPORTANTE: Revise o arquivo .env e configure valores sensíveis"
log "  2. Coloque PDFs de teste em data/input/"
log "  3. Execute: python main.py data/input/exemplo.pdf -o data/output/saida.txt"
log "  4. Para testes: pytest tests/ -v"
log "  5. Para cobertura: pytest --cov=pdf_text_extractor tests/"
log ""
log "📚 Documentação:"
log "  - README.md: Guia de uso completo"
log "  - ANALISE_COMPLETA_REPOSITORIO.md: Análise técnica detalhada"
log "  - ANALISE_VIABILIDADE_OCR_REGEX.md: Roadmap de implementação OCR"
log "  - RESUMO_ANALISES.md: Resumo executivo"
log ""
log "🔒 Lembrete de Segurança:"
log "  - Nunca commite arquivos .env"
log "  - Sempre use valores únicos em produção"
log "  - Revise permissões de arquivos sensíveis"
log ""
log "🎉 Bom desenvolvimento!"
