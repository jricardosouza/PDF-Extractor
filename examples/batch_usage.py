"""
Exemplo de uso em lote do PDF Text Extractor.
Demonstra como processar múltiplos arquivos PDF de uma vez.
"""
import sys
from pathlib import Path

# Adiciona o diretório pai ao path para importar o módulo
sys.path.insert(0, str(Path(__file__).parent.parent))

from pdf_text_extractor import PDFBatchProcessor
from pdf_text_extractor.config import Config


def main():
    """Exemplo de processamento em lote."""
    
    # Diretórios
    input_dir = "data/input"
    output_dir = "data/output"
    
    print("="*80)
    print("EXEMPLO DE PROCESSAMENTO EM LOTE - PDF TEXT EXTRACTOR")
    print("="*80)
    
    # Configuração personalizada
    config = {
        'extract_tables': True,
        'preserve_structure': False,
        'min_text_length': 50,
        'remove_headers': True,
        'normalize_spaces': True,
        'output_format': 'txt'
    }
    
    # Cria o processador
    processor = PDFBatchProcessor(config)
    
    try:
        print(f"\nProcessando PDFs em: {input_dir}")
        print(f"Salvando resultados em: {output_dir}")
        print("-"*80)
        
        # Processa todos os PDFs
        results = processor.process_directory(input_dir, output_dir)
        
        # Exibe estatísticas
        print("\n" + "="*80)
        print("RESULTADOS DO PROCESSAMENTO")
        print("="*80)
        
        successful = [r for r in results if r["status"] == "success"]
        failed = [r for r in results if r["status"] == "error"]
        
        print(f"\n📊 Resumo Geral:")
        print(f"  • Total de arquivos: {len(results)}")
        print(f"  • Processados com sucesso: {len(successful)}")
        print(f"  • Falhas: {len(failed)}")
        
        if successful:
            total_time = sum(r["processing_time"] for r in successful)
            avg_time = total_time / len(successful)
            avg_preserved = sum(r["content_preserved"] for r in successful) / len(successful)
            
            print(f"\n⚡ Performance:")
            print(f"  • Tempo total: {total_time:.2f}s")
            print(f"  • Tempo médio por arquivo: {avg_time:.2f}s")
            print(f"  • Velocidade: {len(successful)/total_time:.2f} docs/segundo")
            
            print(f"\n📈 Qualidade:")
            print(f"  • Conteúdo preservado (média): {avg_preserved:.1f}%")
            
            print(f"\n📄 Arquivos Processados:")
            for result in successful[:5]:  # Mostra os 5 primeiros
                print(f"  ✓ {result['filename']}")
                print(f"    - Páginas: {result['num_pages']}")
                print(f"    - Caracteres limpos: {result['cleaned_chars']}")
                print(f"    - Preservação: {result['content_preserved']:.1f}%")
                print(f"    - Tempo: {result['processing_time']:.2f}s")
            
            if len(successful) > 5:
                print(f"  ... e mais {len(successful) - 5} arquivos")
        
        if failed:
            print(f"\n❌ Arquivos com Erro:")
            for result in failed:
                print(f"  ✗ {result['filename']}: {result['error']}")
        
        print(f"\n📋 Relatório completo salvo em: {output_dir}/processing_report.json")
        print("="*80)
        
    except Exception as e:
        print(f"\n✗ Erro ao processar lote: {str(e)}")


if __name__ == "__main__":
    main()
