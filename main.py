"""
Script principal para execução do PDF Text Extractor.
"""
import argparse
import logging
import sys
from pathlib import Path
from pdf_text_extractor import CleanPDFExtractor, PDFBatchProcessor
from pdf_text_extractor.config import Config


def setup_logging(log_level: str = "INFO"):
    """Configura o sistema de logging."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(Config.LOG_FILE, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )


def process_single_file(pdf_path: str, output_path: str = None, config: dict = None):
    """
    Processa um único arquivo PDF.
    
    Args:
        pdf_path: Caminho do arquivo PDF
        output_path: Caminho opcional para salvar o resultado
        config: Configuração personalizada
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Processando arquivo único: {pdf_path}")
    
    extractor = CleanPDFExtractor(config or Config.get_config_dict())
    
    try:
        clean_text = extractor.extract_clean_text(pdf_path)
        
        if output_path:
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(clean_text, encoding='utf-8')
            logger.info(f"Texto limpo salvo em: {output_path}")
        else:
            print("\n" + "="*80)
            print("TEXTO LIMPO EXTRAÍDO")
            print("="*80)
            print(clean_text)
            print("="*80)
            print(f"\nTotal de caracteres: {len(clean_text)}")
        
        return clean_text
        
    except Exception as e:
        logger.error(f"Erro ao processar arquivo: {str(e)}")
        raise


def process_directory(input_dir: str, output_dir: str, config: dict = None, recursive: bool = False):
    """
    Processa todos os PDFs em um diretório.
    
    Args:
        input_dir: Diretório de entrada
        output_dir: Diretório de saída
        config: Configuração personalizada
        recursive: Processar subdiretórios
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Processando diretório: {input_dir}")
    
    processor = PDFBatchProcessor(config or Config.get_config_dict())
    
    try:
        results = processor.process_directory(input_dir, output_dir, recursive)
        
        # Exibe resumo
        successful = sum(1 for r in results if r["status"] == "success")
        failed = sum(1 for r in results if r["status"] == "error")
        
        print("\n" + "="*80)
        print("PROCESSAMENTO CONCLUÍDO")
        print("="*80)
        print(f"Total de arquivos: {len(results)}")
        print(f"Sucesso: {successful}")
        print(f"Falhas: {failed}")
        print(f"Relatório salvo em: {output_dir}/processing_report.json")
        print("="*80)
        
        return results
        
    except Exception as e:
        logger.error(f"Erro ao processar diretório: {str(e)}")
        raise


def main():
    """Função principal do script."""
    parser = argparse.ArgumentParser(
        description="PDF Text Extractor - Sistema Avançado de Processamento Documental"
    )
    
    parser.add_argument(
        "input",
        help="Arquivo PDF ou diretório de entrada"
    )
    
    parser.add_argument(
        "-o", "--output",
        help="Arquivo ou diretório de saída"
    )
    
    parser.add_argument(
        "-d", "--directory",
        action="store_true",
        help="Processar diretório inteiro"
    )
    
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="Processar subdiretórios recursivamente"
    )
    
    parser.add_argument(
        "-t", "--template",
        choices=["legal_docs", "corporate", "nlp_ready"],
        help="Usar template de configuração pré-definido"
    )
    
    parser.add_argument(
        "--no-tables",
        action="store_true",
        help="Não extrair tabelas"
    )
    
    parser.add_argument(
        "--preserve-structure",
        action="store_true",
        help="Preservar estrutura do documento"
    )
    
    parser.add_argument(
        "--format",
        choices=["txt", "json", "csv"],
        default="txt",
        help="Formato de saída (padrão: txt)"
    )
    
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Nível de logging (padrão: INFO)"
    )
    
    args = parser.parse_args()
    
    # Configura logging
    setup_logging(args.log_level)
    logger = logging.getLogger(__name__)
    
    # Prepara configuração
    if args.template:
        config = Config.get_template_config(args.template)
    else:
        config = Config.get_config_dict()
    
    # Aplica argumentos da linha de comando
    if args.no_tables:
        config["extract_tables"] = False
    
    if args.preserve_structure:
        config["preserve_structure"] = True
    
    config["output_format"] = args.format
    
    # Processa
    try:
        if args.directory:
            if not args.output:
                logger.error("Diretório de saída (-o) é obrigatório para processamento em lote")
                sys.exit(1)
            
            process_directory(args.input, args.output, config, args.recursive)
        else:
            process_single_file(args.input, args.output, config)
        
        logger.info("Processamento concluído com sucesso!")
        
    except Exception as e:
        logger.error(f"Erro fatal: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
