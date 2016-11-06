<?php

/* クエリ取得 */
$str = $_SERVER['QUERY_STRING'];
parse_str($str,$array);
 
/* ファイルポインタをオープン */
$file = fopen("./data/posDataCSV.csv", "wb");
 
/* CSVファイルを配列へ */
if( $file ){
  var_dump( fputcsv($file, $array) );
}
 
/* ファイルポインタをクローズ */
fclose($file);
?>