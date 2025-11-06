"""
Módulo de processamento em lote de PDFs.
"""
import logging
import json
import csv
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime
import pandas as pd
from .extractor import CleanPDFExtractor

logger = logging.getLogger(__name__)


class PDFBatchProcessor:
    """
    Processador em lote que gerencia múltiplos documentos
    e gera relatórios consolidados.
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Inicializa o processador em lote.
        
        Args:
            config: Dicionário de configuração personalizada
        """
        self.config = config or {}
        self.extractor = CleanPDFExtractor(config)
        self.output_format = self.config.get("output_format", "txt")
        self.results = []
        
        logger.info("PDFBatchProcessor inicializado")
    
    def process_directory(
        self, 
        input_dir: str, 
        output_dir: str,
        recursive: bool = False
    ) -> List[Dict[str, Any]]:
        """
        Processa todos os PDFs em um diretório.
        
        Args:
            input_dir: Diretório de entrada com PDFs
            output_dir: Diretório de saída para textos limpos
            recursive: Se True, processa subdiretórios recursivamente
            
        Returns:
            Lista de resultados do processamento
        """
        input_path = Path(input_dir)
        output_path = Path(output_dir)
        
        # Cria diretório de saída se não existir
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Encontra todos os PDFs
        if recursive:
            pdf_files = list(input_path.rglob("*.pdf"))
        else:
            pdf_files = list(input_path.glob("*.pdf"))
        
        logger.info(f"Encontrados {len(pdf_files)} arquivos PDF em {input_dir}")
        
        if not pdf_files:
            logger.warning("Nenhum arquivo PDF encontrado")
            return []
        
        # Processa cada PDF
        results = []
        start_time = datetime.now()
        
        for idx, pdf_file in enumerate(pdf_files, 1):
            logger.info(f"Processando [{idx}/{len(pdf_files)}]: {pdf_file.name}")
            
            try:
                result = self._process_single_file(pdf_file, output_path)
                results.append(result)
                
            except Exception as e:
                logger.error(f"Erro ao processar {pdf_file.name}: {str(e)}")
                results.append({
                    "filename": pdf_file.name,
                    "status": "error",
                    "error": str(e),
                })
        
        end_time = datetime.now()
        processing_time = (end_time - start_time).total_seconds()
        
        # Gera relatório consolidado
        self._generate_report(results, output_path, processing_time)
        
        self.results = results
        logger.info(f"Processamento concluído em {processing_time:.2f} segundos")
        
        return results
    
    def _process_single_file(
        self, 
        pdf_file: Path, 
        output_dir: Path
    ) -> Dict[str, Any]:
        """
        Processa um único arquivo PDF.
        
        Args:
            pdf_file: Caminho do arquivo PDF
            output_dir: Diretório de saída
            
        Returns:
            Dicionário com resultado do processamento
        """
        file_start = datetime.now()
        
        # Extrai texto com metadados
        data = self.extractor.extract_with_metadata(str(pdf_file))
        
        # Salva texto limpo
        output_file = output_dir / f"{pdf_file.stem}_clean.{self.output_format}"
        self._save_output(data["clean_text"], output_file)
        
        file_end = datetime.now()
        processing_time = (file_end - file_start).total_seconds()
        
        return {
            "filename": pdf_file.name,
            "status": "success",
            "num_pages": data["num_pages"],
            "original_chars": data["stats"]["original_length"],
            "cleaned_chars": data["stats"]["cleaned_length"],
            "chars_removed": data["stats"]["characters_removed"],
            "reduction_percentage": data["stats"]["reduction_percentage"],
            "content_preserved": data["stats"]["content_preserved_percentage"],
            "processing_time": round(processing_time, 2),
            "output_file": str(output_file),
        }
    
    def _save_output(self, text: str, output_file: Path):
        """
        Salva o texto processado no formato especificado.
        
        Args:
            text: Texto a ser salvo
            output_file: Caminho do arquivo de saída
        """
        if self.output_format == "txt":
            output_file.write_text(text, encoding="utf-8")
        
        elif self.output_format == "json":
            data = {
                "text": text,
                "length": len(text),
                "timestamp": datetime.now().isoformat(),
            }
            output_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        
        elif self.output_format == "csv":
            # Para CSV, salva linha por linha
            lines = text.split('\n')
            with output_file.open('w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["line_number", "text"])
                for idx, line in enumerate(lines, 1):
                    writer.writerow([idx, line])
        
        logger.debug(f"Texto salvo em: {output_file}")
    
    def _generate_report(
        self, 
        results: List[Dict[str, Any]], 
        output_dir: Path,
        total_time: float
    ):
        """
        Gera relatório consolidado do processamento.
        
        Args:
            results: Lista de resultados do processamento
            output_dir: Diretório de saída
            total_time: Tempo total de processamento
        """
        report_file = output_dir / "processing_report.json"
        
        # Calcula estatísticas gerais
        successful = [r for r in results if r["status"] == "success"]
        failed = [r for r in results if r["status"] == "error"]
        
        total_pages = sum(r.get("num_pages", 0) for r in successful)
        total_chars_removed = sum(r.get("chars_removed", 0) for r in successful)
        avg_reduction = sum(r.get("reduction_percentage", 0) for r in successful) / len(successful) if successful else 0
        avg_preserved = sum(r.get("content_preserved", 0) for r in successful) / len(successful) if successful else 0
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "total_files": len(results),
                "successful": len(successful),
                "failed": len(failed),
                "total_pages": total_pages,
                "total_processing_time": round(total_time, 2),
                "avg_time_per_file": round(total_time / len(results), 2) if results else 0,
                "docs_per_second": round(len(results) / total_time, 2) if total_time > 0 else 0,
            },
            "statistics": {
                "total_chars_removed": total_chars_removed,
                "avg_reduction_percentage": round(avg_reduction, 2),
                "avg_content_preserved": round(avg_preserved, 2),
            },
            "files": results,
        }
        
        # Salva relatório JSON
        report_file.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        
        # Gera também um relatório CSV
        if successful:
            df = pd.DataFrame(successful)
            csv_report = output_dir / "processing_report.csv"
            df.to_csv(csv_report, index=False, encoding="utf-8")
        
        logger.info(f"Relatório gerado em: {report_file}")
        
        # Log do resumo
        logger.info(f"Resumo: {len(successful)} sucesso, {len(failed)} falhas")
        logger.info(f"Velocidade: {report['summary']['docs_per_second']:.2f} docs/segundo")
