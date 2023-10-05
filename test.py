import cv2
source = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
print(face_detector.empty())
def detect_face(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(img_gray, 1.3, 5)
    for face in faces:
        x, y, w, h = face
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)
    return img
while True:
    ret, img = source.read()
    if ret:
        img = detect_face(img)
        cv2.imshow('duong', img)
        key = cv2.waitKey(20)
        if key == ord('q'):
            break
    else: break