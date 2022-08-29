
from pathlib import Path




RAKUTEN_EXCEL_FILEPATH = "./file/{file_name}_data.xlsx"

        
class Excel(object):
    
    def __init__(self, file_name):
        self.file_name = file_name
        
    def write_excel(self, df) -> bool:
        dir = Path("./file") 
        dir.mkdir(parents=True, exist_ok=True)
        # path作成
        excel_path = RAKUTEN_EXCEL_FILEPATH.format(
            file_name=self.file_name)
    
        try:
            df.to_excel(excel_path, index=False, encoding="utf-8-sig")
            return True
        except Exception as e:
            print(e)
            return False
    