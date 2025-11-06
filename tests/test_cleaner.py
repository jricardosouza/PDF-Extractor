"""
Testes unitários para o módulo PDFTextCleaner.
"""
import pytest
from pdf_text_extractor.cleaner import PDFTextCleaner


class TestPDFTextCleaner:
    """Testes para a classe PDFTextCleaner."""
    
    def setup_method(self):
        """Configuração antes de cada teste."""
        self.cleaner = PDFTextCleaner()
    
    def test_initialization(self):
        """Testa a inicialização do cleaner."""
        assert self.cleaner is not None
        assert len(self.cleaner.patterns) > 0
    
    def test_remove_page_numbers(self):
        """Testa remoção de numeração de páginas."""
        text = "--- PÁGINA 1 ---\nConteúdo importante\n1 / 8"
        cleaned = self.cleaner.clean_text(text)
        
        assert "PÁGINA 1" not in cleaned
        assert "1 / 8" not in cleaned
        assert "Conteúdo importante" in cleaned
    
    def test_remove_headers(self):
        """Testa remoção de cabeçalhos repetitivos."""
        text = "RELINT SEPOL/SSINTE\nConteúdo importante"
        cleaned = self.cleaner.clean_text(text)
        
        assert "RELINT" not in cleaned
        assert "SEPOL" not in cleaned
        assert "Conteúdo importante" in cleaned
    
    def test_remove_document_codes(self):
        """Testa remoção de códigos de documento."""
        text = "Código: 0011170143\nConteúdo importante"
        cleaned = self.cleaner.clean_text(text)
        
        assert "0011170143" not in cleaned
        assert "Conteúdo importante" in cleaned
    
    def test_normalize_spaces(self):
        """Testa normalização de espaços."""
        text = "Texto    com    espaços     múltiplos"
        normalized = self.cleaner.normalize_spaces(text)
        
        assert "    " not in normalized
        assert "Texto com espaços múltiplos" in normalized
    
    def test_normalize_newlines(self):
        """Testa normalização de quebras de linha."""
        text = "Linha 1\n\n\n\n\nLinha 2"
        cleaned = self.cleaner.clean_text(text)
        
        assert "\n\n\n" not in cleaned
    
    def test_get_cleaning_stats(self):
        """Testa cálculo de estatísticas de limpeza."""
        original = "--- PÁGINA 1 ---\nConteúdo\n1 / 8"
        cleaned = self.cleaner.clean_text(original)
        
        stats = self.cleaner.get_cleaning_stats(original, cleaned)
        
        assert "original_length" in stats
        assert "cleaned_length" in stats
        assert "characters_removed" in stats
        assert "reduction_percentage" in stats
        assert stats["original_length"] > stats["cleaned_length"]
    
    def test_empty_text(self):
        """Testa comportamento com texto vazio."""
        cleaned = self.cleaner.clean_text("")
        assert cleaned == ""
    
    def test_custom_patterns(self):
        """Testa padrões customizados."""
        custom_patterns = {"custom": r"CUSTOM_PATTERN"}
        cleaner = PDFTextCleaner(custom_patterns)
        
        assert "custom" in cleaner.patterns
