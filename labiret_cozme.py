import cv2
import numpy as np

dosya_adi = 'C:/odev/lab1'
img = cv2.imread(dosya_adi + '.jpg')
cv2.imshow('Labirent', img)


griton = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gri tonlamayı gerçekleştiriyoruz.

ret, thresh = cv2.threshold(griton, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imwrite(dosya_adi + '/1. Threshold1.jpg', thresh)
cv2.imshow('Threshold 1', thresh)
# Eşiklemede tersine çevirme, bize beyaz duvar ve siyah arka plana sahip ikili bir görüntü vermesini sağlıyoruz.



konturlar, hiyerarsi = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2:]
dc = cv2.drawContours(thresh, konturlar, 0, (255, 255, 255), 5)
cv2.imwrite(dosya_adi + '/2. Konturlar1.jpg', dc)
cv2.imshow('Konturlar 1', dc)
# Konturlar

dc = cv2.drawContours(dc, konturlar, 1, (0, 0, 0), 5)
cv2.imwrite(dosya_adi + '/3. Konturlar2.jpg', dc)
cv2.imshow('Konturlar 2', dc)

ret, thresh = cv2.threshold(dc, 240, 255, cv2.THRESH_BINARY)
cv2.imwrite(dosya_adi + '/4. Threshold2.jpg', thresh)
cv2.imshow('Threshold 2', thresh)

ke = 19
cizge = np.ones((ke, ke), np.uint8)

genisleme = cv2.dilate(thresh, cizge, iterations=1)
cv2.imwrite(dosya_adi + '/5. Genisleme.jpg', genisleme)
cv2.imshow('Genisleme', genisleme)

seyreltme = cv2.erode(genisleme, cizge, iterations=1)
cv2.imwrite(dosya_adi + '/6. Seyreltme.jpg', seyreltme)
cv2.imshow('Seyreltme', seyreltme)


diff = cv2.absdiff(genisleme, seyreltme)
cv2.imwrite(dosya_adi + '/7. Fark.jpg', diff)
cv2.imshow('Fark', diff)
# İki görüntü arasındaki farkı buluyoruz


b, g, r = cv2.split(img)
mask_inv = cv2.bitwise_not(diff)
cv2.imwrite(dosya_adi + '/8. Maske.jpg', mask_inv)
cv2.imshow('Maske', mask_inv)
# Labirentin kanallarını ayırıyoruz

r = cv2.bitwise_and(r, r, mask=mask_inv)
b = cv2.bitwise_and(b, b, mask=mask_inv)

res = cv2.merge((b, g, r))
cv2.imwrite(dosya_adi + '/9. CozulmusLabirent.jpg', res)
cv2.imshow('Cozulmus Labirent', res)
cv2.waitKey(0)
cv2.destroyAllWindows