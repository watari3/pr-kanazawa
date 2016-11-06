var IMG_KEY_X = "IMG_X";
var IMG_KEY_Y = "IMG_Y";
var IMG_HTML_ID = "IMG_PIN"

var CSV_SECTION_X = 0;            //X座標
var CSV_SECTION_Y = 1;            //Y座標

var imgX;   //X座標
var imgY;   //Y座標

/*インターバル処理 */
var timerID;
var DEFAULT_INTERVAL_TIME = 1000;         //インターバル時間(msec)

var csvDataArray = new Array();

var CSVFILENAME = "posDataCSV.csv";　//ファイル名
/**
 * マップの読み込みを実施
 */
function onLoadMap()
{
　 //１秒間隔でタイマーを実施
   timerID = setInterval("ReloadMaps()", DEFAULT_INTERVAL_TIME);      
}
/**
 * マップの読み込みを実施
 */
function ReloadMaps()
{
   //保存しているファイルからマップ位置情報を取得
   getCSV();
   //位置情報を取得
   getTrainPos();

　 //イメージの位置情報をセット
   var x = parseInt(imgX);
   var y = parseInt(imgY);

   //イメージ画像を移動
   moveImg(IMG_HTML_ID, x, y);
}
/**
 * イメージを移動します。
 * @param elementid タグ名
 * @param x 座標位置 横
 * @param y 座標位置 縦
 */
function moveImg(elementid, x, y) {
  var img = document.getElementById(elementid);
  document.getElementById(elementid).style.left = x + "px";
  document.getElementById(elementid).style.top  = y + "px"; 
}

/**
 * URL解析して、クエリ文字列を返す
 * @returns {Array} クエリ文字列
 */
function getUrlVars()
{
    var vars = [], max = 0, hash = "", array = "";
    var url = window.location.search;

    //?を取り除くため、1から始める。複数のクエリ文字列に対応するため、&で区切る
    hash  = url.slice(1).split('&');    
    max = hash.length;
    for (var i = 0; i < max; i++) {
        array = hash[i].split('=');    //keyと値に分割。
        vars.push(array[0]);    //末尾にクエリ文字列のkeyを挿入。
        vars[array[0]] = array[1];    //先ほど確保したkeyに、値を代入。
    }
    return vars;
}
/**
* ファイル内容取得処理
*/
function getTrainPos()
{
   imgX = csvDataArray[0][CSV_SECTION_X];
   imgY = csvDataArray[0][CSV_SECTION_Y];
}
/**
* CSVファイル取得処理
*
* @param {string} csvfileName CSVファイル名
*/
function getCSV() {
    // HTTPでファイルを読み込むためのXMLHttpRrequestオブジェクトを生成
    var req = new XMLHttpRequest();
    var csvUrl = "./data/" + CSVFILENAME;
    req.onreadystatechange = function() {
        if (req.readyState == 4) {
            convertCSVtoArray(req.responseText); // 渡されるのは読み込んだCSVデータ
        }
    }
    req.open("GET", csvUrl, true);
    req.send(null); // HTTPリクエストの発行
}
/**
* 読み込んだCSVデータを二次元配列に変換する
*
* @param {string} str 文字列
*/
function convertCSVtoArray(str) {
    // 読み込んだCSVデータが文字列として渡される
    var result = []; // 最終的な二次元配列を入れるための配列
    var tmp = str.split("\n"); // 改行を区切り文字として行を要素とした配列を生成 
    // 各行ごとにカンマで区切った文字列を要素とした二次元配列を生成
    for (var i = 0; i < tmp.length; ++i) {
        result[i] = tmp[i].split(',');
    }
    csvDataArray = result;
}