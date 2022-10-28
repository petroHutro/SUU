import cv2
import pytesseract


img = cv2.imread('/Users/*/SUU_3/test.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(img, config=config, lang="rus+eng"))

data = pytesseract.image_to_data(img, config=config, lang="rus+eng")

for i, el in enumerate(data.splitlines()):
    if i == 0:
        continue
    el = el.split()
    try:
        x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
        cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
        cv2.putText(img, el[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
    except IndexError:
        pass

cv2.imshow('Result', img)
cv2.waitKey(0)
