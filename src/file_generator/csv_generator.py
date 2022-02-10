import csv
from typing import List

from .base_generator import FileGenerator


class CSVGenerator(FileGenerator):
    def write_file(self, content: str, file_name: str):
        try:
            csv_file = open(file_name, "w+")
            headers = self.setup_header(content)
            csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
            csv_writer.writeheader()
            csv_file.close()
            print("CSV created!")
        except Exception as e:
            print(f"Error on writing file: {e}")

    def setup_header(self, content: str) -> List[str]:
        return self.transformer(content)

    def transformer(self, content: str) -> List[str]:
        return list(content)
