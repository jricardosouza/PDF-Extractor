"""
Exemplo de uso simples do PDF Text Extractor.
Demonstra como processar um único arquivo PDF.
"""
import sys
from pathlib import Path

# Adiciona o diretório pai ao path para importar o módulo
sys.path.insert(0, str(Path(__file__).parent.parent))

from pdf_text_extractor import CleanPDFExtractor


def main():
    """Exemplo básico de extração de texto."""
    
    # Caminho do PDF de exemplo
    pdf_path = "data/input/exemplo.pdf"
    
    # Cria o extrator com configuração padrão
    extractor = CleanPDFExtractor()
    
    print("="*80)
    print("EXEMPLO DE USO SIMPLES - PDF TEXT EXTRACTOR")
    print("="*80)
    
    try:
        # Extrai texto limpo
        print(f"\nProcessando: {pdf_path}")
        clean_text = extractor.extract_clean_text(pdf_path)
        
        # Exibe resultado
        print(f"\n✓ Texto extraído com sucesso!")
        print(f"  Total de caracteres: {len(clean_text)}")
        print(f"\nPrimeiros 500 caracteres:")
        print("-"*80)
        print(clean_text[:500])
        print("-"*80)
        
        # Salva resultado
        output_path = "data/output/exemplo_clean.txt"
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        Path(output_path).write_text(clean_text, encoding='utf-8')
        
        print(f"\n✓ Texto salvo em: {output_path}")
        
    except FileNotFoundError:
        print(f"\n✗ Erro: Arquivo não encontrado: {pdf_path}")
        print("  Certifique-se de colocar um PDF em data/input/exemplo.pdf")
    
    except Exception as e:
        print(f"\n✗ Erro ao processar: {str(e)}")


if __name__ == "__main__":
    main()
