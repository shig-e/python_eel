
from time import sleep
import os
import re
import eel
import pandas as pd

from common.output import Output
from common.rakuten_api import RakutenAPI
from common.logger import set_logger
from common.execl import Excel

from dotenv import load_dotenv
load_dotenv('.env')
log = set_logger()


def rakuten_search(path):
    log.info("スクレイピング開始")
    data = []
    count = 0
    succes = 1
    fail = 0
    max_page = 10
    for i in range(1, max_page+1):
        params = {
            "applicationId": os.environ.get('APP_ID'),
            "format": "json",
            "keyword": path,
            "genreId": 0,
            "page": i,
            "hits": 30}
        url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
        
        rakuten = RakutenAPI(url, params)
        output = Output("Rakuten")
        excel = Excel("Rakuten")
        
        req = rakuten.get_requests(url, params)
        sleep(3)
        items = rakuten.check_header(req)
        
        for _item in items["Items"]:
            try:
                item = _item["Item"]
                name = item["itemName"].replace("\n3000", ",")
                eel.view_log_js(f"商品名: {name}")
                # print(eel.view_log_js(f"商品名: {name}"))
                price = int(item["itemPrice"])
                url = item["itemUrl"]
                discription = item["itemCaption"].replace("\u3000", ",")
                m = re.search(r'[0-9]{13}', discription)
                if m is not None:
                    jancode = m.group()
                else:
                    jancode = None
                
                data.append({"商品名": name,
                            "価格": price,
                            "url": url,
                            "説明文": discription,
                            "Jancode": jancode})
                log.info(f"[成功]{count} 件目 :{name}")
                succes += 1
            except Exception as e:
                log.info(f"[失敗] {count} 件目 : {name}")
                log.info(e)
                fail += 1
            finally:
                count += 1
        df = pd.DataFrame.from_dict(data, dtype=object)
        output.write_csv(df) 
        excel.write_excel(df)
        
    

                    
                    
    
        