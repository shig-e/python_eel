import eel
import desktop
import search 


def main():
    app_name = "web"
    end_point = "main.html"
    size=(800,700)
    
    @eel.expose
    def rakuten_search(path):
        search.rakuten_search(path)
    
    desktop.start(app_name,end_point,size)

if __name__ == "__main__":
    main()