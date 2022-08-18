var path = document.getElementById("path");

const btn = document.querySelector(".btn");

var result_text_area = document.getElementById("result_text_area");
var newElement = document.createElement("textarea");

eel.expose(view_log_js);
function view_log_js(result) {
    var newContent = document.createTextNode(result + "\n");
    newContent.appendChild(newContent);
    newElement.setAttribute("id", "result_area");
    result_text_area.innerBefore(newElement);
    console.log(result);
}

eel.expose(alert);
function alert_js(text) {
    alert(text);
}

// rakuten_searchにキーワードを渡す関数
function call_rakuten_search() {
    eel.rakuten_search(path.value);
}

// 検索ワードがない場合アラートを出す
btn.addEventListener("click", () => {
    var flag = true;
    if (path.value == "") {
        alert("検索したい商品を入力してください");
        flag = false;
    }
    if (flag) {
        call_rakuten_search();
    }
});