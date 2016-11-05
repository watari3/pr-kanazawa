# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys
# 引数読み込み
args = sys.argv

# 画像の読み込み
 # 第一引数：読み込む画像のパス
 # 第二引数：カラータイプ　-1: RGBA, 0: グレースケール, 1: RGB
img = cv2.imread(args[1], 1)
# 元の画像サイズを取得
orgHeight, orgWidth = img.shape[:2]
# リサイズ時の縮小比率
downsize = (orgHeight//10, orgWidth//10)

# 画像をHSVに変換
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 取得する色の範囲を指定する
lower_rail = np.array([27, 50, 50])
upper_rail = np.array([120, 255, 255])

# 指定した色に基づいたマスク画像の生成
img_mask = cv2.inRange(hsv, lower_rail, upper_rail)

# フレーム画像とマスク画像の共通の領域を抽出する。
img_color = cv2.bitwise_and(img, img, mask=img_mask)

# リサイズ処理
  # 縮小
halfImg = cv2.resize(img_color, downsize)
  # 拡大
resizeImg = cv2.resize(halfImg,(orgWidth,orgHeight))

# グレースケール
gray = cv2.cvtColor(resizeImg, cv2.COLOR_BGR2GRAY)

# 二値化
_ ,binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)

# ネガポジ反転
negaposi = cv2.bitwise_not(binary)
cv2.imwrite("output.jpg",negaposi)
