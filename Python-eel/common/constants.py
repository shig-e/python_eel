import os

# 現在のディレクトリ
directory = {"current": ""}


class EelConfig(object):
    """ eel設定 """
    APP_NAME = os.path.join("web")
    END_POINT = "main.html"
    ALLOW_EXTENSIONS = [".html", ".js", ".ico"]
    WINDOW_SIZE = (700, 600)
