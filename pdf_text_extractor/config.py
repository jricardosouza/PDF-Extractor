"""
Módulo de configuração para o PDF Text Extractor.
"""
import os
from typing import Dict, Any
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()


class Config:
    """Classe de configuração centralizada."""
    
    # Diretórios
    INPUT_DIR = os.getenv("INPUT_DIR", "data/input")
    OUTPUT_DIR = os.getenv("OUTPUT_DIR", "data/output")
    
    # Configurações de Processamento
    MIN_TEXT_LENGTH = int(os.getenv("MIN_TEXT_LENGTH", "50"))
    EXTRACT_TABLES = os.getenv("EXTRACT_TABLES", "True").lower() == "true"
    PRESERVE_STRUCTURE = os.getenv("PRESERVE_STRUCTURE", "False").lower() == "true"
    REMOVE_HEADERS = os.getenv("REMOVE_HEADERS", "True").lower() == "true"
    NORMALIZE_SPACES = os.getenv("NORMALIZE_SPACES", "True").lower() == "true"
    
    # Formato de Saída
    OUTPUT_FORMAT = os.getenv("OUTPUT_FORMAT", "txt")
    
    # Configurações de Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "logs/pdf_extractor.log")
    
    # Configurações de Performance
    MAX_WORKERS = int(os.getenv("MAX_WORKERS", "4"))
    BATCH_SIZE = int(os.getenv("BATCH_SIZE", "10"))
    
    # Padrões Customizados
    CUSTOM_PATTERNS = os.getenv("CUSTOM_PATTERNS", None)
    
    @classmethod
    def get_config_dict(cls) -> Dict[str, Any]:
        """Retorna um dicionário com todas as configurações."""
        return {
            "extract_tables": cls.EXTRACT_TABLES,
            "preserve_structure": cls.PRESERVE_STRUCTURE,
            "min_text_length": cls.MIN_TEXT_LENGTH,
            "remove_headers": cls.REMOVE_HEADERS,
            "normalize_spaces": cls.NORMALIZE_SPACES,
            "output_format": cls.OUTPUT_FORMAT,
        }
    
    @classmethod
    def get_template_config(cls, template_name: str) -> Dict[str, Any]:
        """Retorna configurações pré-definidas para templates específicos."""
        templates = {
            "legal_docs": {
                "extract_tables": True,
                "preserve_structure": True,
                "remove_headers": False,
                "normalize_spaces": True,
                "min_text_length": 50,
            },
            "corporate": {
                "extract_tables": True,
                "preserve_structure": False,
                "remove_headers": True,
                "normalize_spaces": True,
                "min_text_length": 50,
            },
            "nlp_ready": {
                "extract_tables": False,
                "preserve_structure": False,
                "remove_headers": True,
                "normalize_spaces": True,
                "min_text_length": 100,
            },
        }
        return templates.get(template_name, cls.get_config_dict())
