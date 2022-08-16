import eel
import  search 
import desktop

app_name = "html"
end_point = "main.html"
size = (700, 600)

@eel.expose
def rakuten_search(search_keyword):
    search.rakuten_search(search_keyword)

desktop.start(app_name, end_point, size)