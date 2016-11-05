# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 画像の読み込み
 # 第一引数：読み込む画像のパス
 # 第二引数：カラータイプ　-1: RGBA, 0: グレースケール, 1: RGB
img = cv2.imread("sample_picture.jpg", 1) # 画像をグレースケールに変換して読み込む

# 画像をHSVに変換
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 取得する色の範囲を指定する
#lower_rail = np.array([80, 50, 50])
lower_rail = np.array([27, 50, 50])
upper_rail = np.array([120, 255, 255])

# 指定した色に基づいたマスク画像の生成
img_mask = cv2.inRange(hsv, lower_rail, upper_rail)

# フレーム画像とマスク画像の共通の領域を抽出する。
img_color = cv2.bitwise_and(img, img, mask=img_mask)

cv2.imshow("SHOW COLOR IMAGE", img_color)

# 画像の表示
 # 第一引数：ウィンドウを識別するための名前
 # 第二引数：表示する画像
cv2.imshow("img", img)

# キーが押させるまで画像を表示したままにする
 # 第一引数：キーイベントを待つ時間　0: 無限, 0以上: 指定ミリ秒待つ
cv2.waitKey(0)

# 作成したウィンドウを全て破棄
cv2.destroyAllWindows()
