"""
Módulo de limpeza de texto extraído de PDFs.
"""
import re
import logging
from typing import Dict, List

logger = logging.getLogger(__name__)


class PDFTextCleaner:
    """
    Motor de limpeza que identifica e remove elementos de poluição
    usando padrões regex avançados.
    """
    
    def __init__(self, custom_patterns: Dict[str, str] = None):
        """
        Inicializa o limpador de texto com padrões regex.
        
        Args:
            custom_patterns: Dicionário opcional com padrões regex customizados
        """
        self.patterns = self._initialize_patterns()
        if custom_patterns:
            self.patterns.update(custom_patterns)
        logger.info(f"PDFTextCleaner inicializado com {len(self.patterns)} padrões")
    
    def _initialize_patterns(self) -> Dict[str, str]:
        """Inicializa os padrões regex para limpeza de texto."""
        return {
            # Remoção de numeração de páginas
            "page_numbers": r'(?:PÁGINA|página)\s*\d+|\d+\s*/\s*\d+',
            
            # Filtro de cabeçalhos repetitivos
            "headers_relint": r'(?:RELINT|SEPOL|SSINTE).*?(?=\n|$)',
            
            # Limpeza de códigos de documento
            "document_codes": r'\b\d{10,}\b',
            
            # Normalização de espaços
            "multiple_spaces": r'\s{2,}',
            
            # Quebras de linha excessivas
            "multiple_newlines": r'\n{3,}',
            
            # Padrões específicos adicionais
            "page_marker": r'---\s*PÁGINA\s*\d+\s*---',
            "footer_pattern": r'RESUMO:.*?(?=\n|$)',
        }
    
    def clean_text(self, text: str) -> str:
        """
        Remove numeração de páginas e aplica filtros de limpeza.
        
        Args:
            text: Texto bruto extraído do PDF
            
        Returns:
            Texto limpo e processado
        """
        if not text:
            return ""
        
        # Remove numeração de páginas
        text = re.sub(self.patterns["page_numbers"], '', text)
        
        # Remove cabeçalhos RELINT
        text = re.sub(self.patterns["headers_relint"], '', text)
        
        # Remove códigos longos de documento
        text = re.sub(self.patterns["document_codes"], '', text)
        
        # Normaliza espaços múltiplos
        text = re.sub(self.patterns["multiple_spaces"], ' ', text)
        
        # Normaliza quebras de linha excessivas
        text = re.sub(self.patterns["multiple_newlines"], '\n\n', text)
        
        # Remove marcadores de página
        text = re.sub(self.patterns["page_marker"], '', text)
        
        return text.strip()
    
    def remove_headers(self, text: str, header_patterns: List[str] = None) -> str:
        """
        Remove cabeçalhos repetitivos do texto.
        
        Args:
            text: Texto a ser processado
            header_patterns: Lista opcional de padrões de cabeçalho customizados
            
        Returns:
            Texto sem cabeçalhos repetitivos
        """
        if header_patterns is None:
            header_patterns = [
                r'(?:RELINT|SEPOL|SSINTE).*?(?=\n|$)',
            ]
        
        for pattern in header_patterns:
            text = re.sub(pattern, '', text)
        
        return text
    
    def normalize_spaces(self, text: str) -> str:
        """
        Normaliza espaçamentos e quebras de linha.
        
        Args:
            text: Texto a ser normalizado
            
        Returns:
            Texto com espaçamento normalizado
        """
        # Remove espaços múltiplos
        text = re.sub(r'\s{2,}', ' ', text)
        
        # Normaliza quebras de linha
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        # Remove espaços no início e fim de linhas
        lines = [line.strip() for line in text.split('\n')]
        
        return '\n'.join(lines)
    
    def get_cleaning_stats(self, original_text: str, cleaned_text: str) -> Dict[str, int]:
        """
        Calcula estatísticas sobre a limpeza realizada.
        
        Args:
            original_text: Texto original
            cleaned_text: Texto limpo
            
        Returns:
            Dicionário com estatísticas de limpeza
        """
        return {
            "original_length": len(original_text),
            "cleaned_length": len(cleaned_text),
            "characters_removed": len(original_text) - len(cleaned_text),
            "reduction_percentage": round(
                ((len(original_text) - len(cleaned_text)) / len(original_text) * 100), 2
            ) if len(original_text) > 0 else 0,
            "content_preserved_percentage": round(
                (len(cleaned_text) / len(original_text) * 100), 2
            ) if len(original_text) > 0 else 0,
        }
