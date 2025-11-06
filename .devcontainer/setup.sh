#!/bin/bash

echo "🚀 Configurando ambiente de desenvolvimento PDF-Extractor..."

# Atualizar sistema
echo "📦 Atualizando sistema..."
sudo apt-get update -y

# Instalar Tesseract OCR (para futura implementação)
echo "🔍 Instalando Tesseract OCR..."
sudo apt-get install -y tesseract-ocr tesseract-ocr-por libtesseract-dev

# Instalar dependências de processamento de imagem
echo "🖼️ Instalando dependências de processamento de imagem..."
sudo apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    poppler-utils

# Criar ambiente virtual Python
echo "🐍 Configurando ambiente Python..."
python -m pip install --upgrade pip
pip install --upgrade setuptools wheel

# Instalar dependências do projeto
echo "📚 Instalando dependências do projeto..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

# Instalar dependências de desenvolvimento
echo "🛠️ Instalando ferramentas de desenvolvimento..."
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

# Instalar dependências OCR (para desenvolvimento futuro)
echo "🔮 Instalando dependências OCR (pré-configuração)..."
pip install \
    pytesseract>=0.3.10 \
    pdf2image>=1.16.3 \
    Pillow>=10.0.0 \
    opencv-python-headless>=4.8.0

# Criar diretórios necessários
echo "📁 Criando estrutura de diretórios..."
mkdir -p data/input data/output logs .cache tests/fixtures

# Configurar git
echo "🔧 Configurando Git..."
git config --global core.autocrlf input
git config --global pull.rebase false

# Criar arquivo .env se não existir
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
    echo "⚙️ Criando arquivo .env..."
    cp .env.example .env
    echo "✅ Arquivo .env criado. Configure conforme necessário."
fi

# Verificar instalações
echo ""
echo "🔍 Verificando instalações..."
echo "Python: $(python --version)"
echo "Pip: $(pip --version)"
echo "Tesseract: $(tesseract --version | head -1)"
echo "Git: $(git --version)"

# Executar testes se existirem
if [ -d "tests" ] && [ -n "$(ls -A tests)" ]; then
    echo ""
    echo "🧪 Executando testes..."
    pytest tests/ -v --tb=short || echo "⚠️ Alguns testes falharam. Revise os resultados acima."
fi

echo ""
echo "✅ Ambiente de desenvolvimento configurado com sucesso!"
echo ""
echo "📖 Próximos passos:"
echo "  1. Revise o arquivo .env e configure conforme necessário"
echo "  2. Coloque PDFs de teste em data/input/"
echo "  3. Execute: python main.py data/input/exemplo.pdf -o data/output/saida.txt"
echo "  4. Para testes: pytest tests/ -v"
echo "  5. Para cobertura: pytest --cov=pdf_text_extractor tests/"
echo ""
echo "📚 Documentação:"
echo "  - README.md: Guia de uso completo"
echo "  - ANALISE_COMPLETA_REPOSITORIO.md: Análise técnica detalhada"
echo "  - ANALISE_VIABILIDADE_OCR_REGEX.md: Roadmap de implementação OCR"
echo ""
echo "🎉 Bom desenvolvimento!"
