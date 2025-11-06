"""
Módulo de extração de texto de PDFs.
"""
import pdfplumber
import logging
from pathlib import Path
from typing import Dict, Optional, Any
from .cleaner import PDFTextCleaner

logger = logging.getLogger(__name__)


class CleanPDFExtractor:
    """
    Extrator principal que coordena a extração de texto
    e aplicação de filtros de limpeza.
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Inicializa o extrator de PDF.
        
        Args:
            config: Dicionário de configuração personalizada
        """
        self.config = config or {}
        self.cleaner = PDFTextCleaner()
        self.extract_tables = self.config.get("extract_tables", True)
        self.preserve_structure = self.config.get("preserve_structure", False)
        self.min_text_length = self.config.get("min_text_length", 50)
        self.remove_headers = self.config.get("remove_headers", True)
        self.normalize_spaces = self.config.get("normalize_spaces", True)
        
        logger.info("CleanPDFExtractor inicializado")
    
    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """
        Extrai texto de um arquivo PDF.
        
        Args:
            pdf_path: Caminho para o arquivo PDF
            
        Returns:
            Texto extraído do PDF
            
        Raises:
            FileNotFoundError: Se o arquivo não for encontrado
            Exception: Para outros erros de processamento
        """
        pdf_file = Path(pdf_path)
        
        if not pdf_file.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {pdf_path}")
        
        logger.info(f"Extraindo texto de: {pdf_path}")
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                text_parts = []
                
                for page_num, page in enumerate(pdf.pages, 1):
                    logger.debug(f"Processando página {page_num}/{len(pdf.pages)}")
                    
                    # Extrai texto da página
                    page_text = page.extract_text() or ""
                    
                    # Extrai tabelas se configurado
                    if self.extract_tables:
                        tables = page.extract_tables()
                        if tables:
                            for table in tables:
                                table_text = self._format_table(table)
                                page_text += f"\n\n{table_text}"
                    
                    text_parts.append(page_text)
                
                full_text = "\n\n".join(text_parts)
                logger.info(f"Texto extraído: {len(full_text)} caracteres")
                
                return full_text
                
        except Exception as e:
            logger.error(f"Erro ao extrair texto de {pdf_path}: {str(e)}")
            raise
    
    def extract_clean_text(self, pdf_path: str) -> str:
        """
        Extrai e limpa o texto de um arquivo PDF.
        
        Args:
            pdf_path: Caminho para o arquivo PDF
            
        Returns:
            Texto limpo extraído do PDF
        """
        # Extrai texto bruto
        raw_text = self.extract_text_from_pdf(pdf_path)
        
        # Aplica limpeza
        clean_text = self.cleaner.clean_text(raw_text)
        
        # Remove cabeçalhos se configurado
        if self.remove_headers:
            clean_text = self.cleaner.remove_headers(clean_text)
        
        # Normaliza espaços se configurado
        if self.normalize_spaces:
            clean_text = self.cleaner.normalize_spaces(clean_text)
        
        # Verifica comprimento mínimo
        if len(clean_text) < self.min_text_length:
            logger.warning(
                f"Texto extraído muito curto ({len(clean_text)} caracteres). "
                f"Mínimo esperado: {self.min_text_length}"
            )
        
        logger.info(f"Texto limpo: {len(clean_text)} caracteres")
        
        return clean_text
    
    def extract_with_metadata(self, pdf_path: str) -> Dict[str, Any]:
        """
        Extrai texto e metadados do PDF.
        
        Args:
            pdf_path: Caminho para o arquivo PDF
            
        Returns:
            Dicionário com texto limpo e metadados
        """
        pdf_file = Path(pdf_path)
        
        # Extrai textos
        raw_text = self.extract_text_from_pdf(pdf_path)
        clean_text = self.cleaner.clean_text(raw_text)
        
        if self.remove_headers:
            clean_text = self.cleaner.remove_headers(clean_text)
        
        if self.normalize_spaces:
            clean_text = self.cleaner.normalize_spaces(clean_text)
        
        # Obtém estatísticas
        stats = self.cleaner.get_cleaning_stats(raw_text, clean_text)
        
        # Extrai metadados do PDF
        with pdfplumber.open(pdf_path) as pdf:
            metadata = pdf.metadata or {}
            num_pages = len(pdf.pages)
        
        return {
            "filename": pdf_file.name,
            "filepath": str(pdf_file.absolute()),
            "num_pages": num_pages,
            "raw_text": raw_text,
            "clean_text": clean_text,
            "metadata": metadata,
            "stats": stats,
        }
    
    def _format_table(self, table: list) -> str:
        """
        Formata uma tabela extraída em texto.
        
        Args:
            table: Lista de listas representando a tabela
            
        Returns:
            Texto formatado da tabela
        """
        if not table:
            return ""
        
        formatted_rows = []
        for row in table:
            # Remove valores None e converte para string
            clean_row = [str(cell) if cell is not None else "" for cell in row]
            formatted_rows.append(" | ".join(clean_row))
        
        return "\n".join(formatted_rows)
