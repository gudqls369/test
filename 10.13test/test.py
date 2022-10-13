import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
imgs = ['10.13test\photo.jpg']

results = model(imgs)

tmp_img = cv2.imread("10.13test\photo.jpg")
print('세로:', tmp_img.shape[0], 'px', '가로:', tmp_img.shape[1], 'px')

cv2.rectangle(tmp_img, (int(results.xyxy[0][0][0].item()), int(results.xyxy[0][0][1].item())), (int(results.xyxy[0][0][2].item()), int(results.xyxy[0][0][3].item())), (255,255,255))
cv2.rectangle(tmp_img, (int(results.xyxy[0][1][0].item()), int(results.xyxy[0][1][1].item())), (int(results.xyxy[0][1][2].item()), int(results.xyxy[0][1][3].item())), (255,255,255))
cv2.rectangle(tmp_img, (int(results.xyxy[0][2][0].item()), int(results.xyxy[0][2][1].item())), (int(results.xyxy[0][2][2].item()), int(results.xyxy[0][2][3].item())), (255,255,255))
cv2.rectangle(tmp_img, (int(results.xyxy[0][3][0].item()), int(results.xyxy[0][3][1].item())), (int(results.xyxy[0][3][2].item()), int(results.xyxy[0][3][3].item())), (255,255,255))
cv2.rectangle(tmp_img, (int(results.xyxy[0][4][0].item()), int(results.xyxy[0][4][1].item())), (int(results.xyxy[0][4][2].item()), int(results.xyxy[0][4][3].item())), (255,255,255))
cv2.imwrite('result1.png', tmp_img)

tmp_img = cv2.imread("10.13test\photo.jpg")
people1 = tmp_img[int(results.xyxy[0][0][1].item()):int(results.xyxy[0][0][3].item()), int(results.xyxy[0][0][0].item()):int(results.xyxy[0][0][2].item())].copy()
cv2.imwrite('people1.png', people1)
people2 = tmp_img[int(results.xyxy[0][1][1].item()):int(results.xyxy[0][1][3].item()), int(results.xyxy[0][1][0].item()):int(results.xyxy[0][1][2].item())].copy()
cv2.imwrite('people2.png', people2)
people3 = tmp_img[int(results.xyxy[0][2][1].item()):int(results.xyxy[0][2][3].item()), int(results.xyxy[0][2][0].item()):int(results.xyxy[0][2][2].item())].copy()
cv2.imwrite('people3.png', people3)
people4 = tmp_img[int(results.xyxy[0][3][1].item()):int(results.xyxy[0][3][3].item()), int(results.xyxy[0][3][0].item()):int(results.xyxy[0][3][2].item())].copy()
cv2.imwrite('people4.png', people4)
people5 = tmp_img[int(results.xyxy[0][4][1].item()):int(results.xyxy[0][4][3].item()), int(results.xyxy[0][4][0].item()):int(results.xyxy[0][4][2].item())].copy()
cv2.imwrite('people5.png', people5)