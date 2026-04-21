from pathlib import Path

import openpyxl

from src.utils.logger import get_logger


class Handler:

    def __init__(self):
        self.logger = get_logger(__name__)
        self.file_path = Path('src/resources')
        self.file_name = 'challenge.xlsx' 
    
    def read_file(self):
        self.logger.info('Iniciando a leitura do arquivo.')

        full_file_path = self.file_path / self.file_name
        
        try:
            if not full_file_path.exists():
                self.logger.error(f'Arquivo não encontrado: {full_file_path}')
                return
            
            self.logger.info(f'Carregando arquivo Excel: {full_file_path}')

            workbook = openpyxl.load_workbook(full_file_path)
            sheet = workbook.active

            self.logger.info(f'Leitura concluída. Aba selecionada: {sheet.title}')

            data = []
            for row in sheet.iter_rows(min_row=2, values_only=True):
                if not any(row):
                    continue
                
                extracted = {
                    'first_name': str(row[0]),
                    'last_name': str(row[1]),
                    'company_name': str(row[2]),
                    'role_in_company': str(row[3]),
                    'address': str(row[4]),
                    'email': str(row[5]),
                    'phone_number': str(row[6])
                }

                data.append(extracted)

            return data

        except Exception as e:
            self.logger.exception(f'Erro ao processar arquivo, detalhes: {e}')
            return data

