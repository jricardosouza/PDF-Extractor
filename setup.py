from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pdf-text-extractor",
    version="1.0.0",
    author="Seu Nome",
    description="Sistema Avançado de Processamento Documental",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pdfplumber>=0.11.0",
        "pandas>=2.0.0",
        "python-dotenv>=1.0.0",
    ],
)
