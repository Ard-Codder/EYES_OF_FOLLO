from cv2 import cv2


def loading_displaying_saving():
    img = cv2.imread('images/test.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('girl', img)
    cv2.waitKey(0)
    cv2.imwrite('  .jpg', img)


def accessing_and_manipulating():
    img = cv2.imread('images/test.jpg')
    print("Высота:" + str(img.shape[0]))
    print("Ширина:" + str(img.shape[1]))
    print("Количество каналов:" + str(img.shape[2]))
    (b, g, r) = img[0, 0]
    print(f"Красный: {r}, Зелёный: {g}, Синий: {b}")
    img[0, 0] = (255, 0, 0)
    (b, g, r) = img[0, 0]
    print(f"Красный: {r}, Зелёный: {g}, Синий: {b}")


accessing_and_manipulating()
