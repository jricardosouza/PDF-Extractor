"""
PDF Text Extractor - Sistema Avançado de Processamento Documental

Este pacote fornece ferramentas para extrair texto limpo de documentos PDF,
removendo elementos de poluição como cabeçalhos, rodapés, numeração de páginas
e códigos de documento.
"""

__version__ = "1.0.0"
__author__ = "Seu Nome"

from .cleaner import PDFTextCleaner
from .extractor import CleanPDFExtractor
from .batch_processor import PDFBatchProcessor

__all__ = [
    "PDFTextCleaner",
    "CleanPDFExtractor",
    "PDFBatchProcessor",
]
