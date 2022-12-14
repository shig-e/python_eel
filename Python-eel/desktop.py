# -*- coding: utf-8 -*-

import eel
import sys
import socket 
import search
from common.constants import EelConfig

# 定数
CHROME_ARGS = [
    '--incognit',  # シークレットモード
    '--disable-http-cache',  # キャッシュ無効
    '--disable-plugins',  # プラグイン無効
    '--disable-extensions',  # 拡張機能無効
    '--disable-dev-tools',  # デベロッパーツールを無効にする
]


# GUIからpathを受け取る
@eel.expose
def start_researching(path):
    search.rakuten_search(path)
    


def start():  # 画面生成
    eel.init(EelConfig.APP_NAME, allowed_extensions=EelConfig.ALLOW_EXTENSIONS)
    # 未使用ポート取得
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    options = {
        'mode': "chrome",
        'close_callback': exit,
        'port': port,
        'cmdline_args': CHROME_ARGS
    }
    eel.start(EelConfig.END_POINT, options=options,
        size=EelConfig.WINDOW_SIZE, suppress_error=True)

def exit(arg1, arg2):  # 終了時の処理
    sys.exit(0)
