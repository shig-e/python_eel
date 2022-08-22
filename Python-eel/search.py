
from time import sleep
import os
import re
import eel
import pandas as pd

from common.output import Output
from common.rakuten_api import RakutenAPI

from dotenv import load_dotenv
load_dotenv('.env')

@eel.expose
def rakuten_search(path):
    
    data = []
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
        
        req = rakuten.get_requests(url, params)
        sleep(3)
        result = rakuten.check_header(req)
        print(params)
        for _item in result["Items"]:
            item = _item["Item"]
            name = item["itemName"].replace("\n3000", ",")
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
            df = pd.DataFrame.from_dict(data, dtype=object)
            eel.view_log_js(name)  # type: ignore
            output.write_csv(df) 