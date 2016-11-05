import cv2
import numpy as np

img = cv2.imread('sample_picture.jpg')

# グレースケール
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imwrite('gray.png', gray)

# 二値化
_ ,binary = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
# cv2.imwrite('binary.png', binary)

# エッジ抽出
edge = cv2.Canny(img, 50, 150)
# cv2.imwrite('edge.png', edge)

# ネガポジ反転
negaposi = cv2.bitwise_not(edge)
cv2.imwrite('negaposi.png', negaposi)


'''
# エッジ　
import cv2

#Gray Scaleで画像を読み込み
gray_img = cv2.imread('sample_picture.jpg',0)

#Cannyアルゴリズムでエッジ検出
canny_edges = cv2.Canny(gray_img,100,200)

#結果表示
cv2.imshow('sample_picture.jpg',canny_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
