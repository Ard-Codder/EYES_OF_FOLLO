import numpy as np
from cv2 import cv2


def image_arithmetic():
    print("opencv addition:", cv2.add(np.uint8([250]), np.uint8([30])))
    print("opencv subtract:", cv2.subtract(np.uint8([70]), np.uint8([100])))
    print("numpy addition:", np.uint8([250]) + np.uint8([30]))
    print("numpy subtract:", np.uint8([70]) - np.uint8([71]))


def splitting_and_merging():
    image = cv2.imread('images/test.jpg')
    b, g, r = cv2.split(image)
    cv2.imshow('blue', b)
    cv2.imshow('green', g)
    cv2.imshow('red', r)

    # Перетасовка значений по другим канала
    merge_image = cv2.merge([b, b, r + 50])
    cv2.imshow('merge_image', merge_image)
    cv2.imshow('original', image)
    cv2.waitKey(0)


def averaging_blurring():
    image = cv2.imread('images/test.jpg')
    img_blur_3 = cv2.blur(image, (3, 3))
    img_blur_7 = cv2.blur(image, (7, 7))
    img_blur_11 = cv2.blur(image, (11, 11))
    cv2.imshow('3x3', img_blur_3)
    cv2.imshow('7x7', img_blur_7)
    cv2.imshow('11x11', img_blur_11)
    cv2.waitKey(0)


# Блюрринг изображения
def gaussian_blurring():
    image = cv2.imread('images/test.jpg')
    img_blur_3 = cv2.GaussianBlur(image, (3, 3), 0)
    img_blur_7 = cv2.GaussianBlur(image, (7, 7), 0)
    img_blur_11 = cv2.GaussianBlur(image, (11, 11), 0)
    cv2.imshow('3x3', img_blur_3)
    cv2.imshow('7x7', img_blur_7)
    cv2.imshow('11x11', img_blur_11)
    cv2.waitKey(0)


# Блюрринг при помощи медиан изображения
def median_blurring():
    image = cv2.imread('images/test.jpg')
    img_blur_3 = cv2.medianBlur(image, 3)
    img_blur_7 = cv2.medianBlur(image, 7)
    img_blur_11 = cv2.medianBlur(image, 11)
    cv2.imshow('3', img_blur_3)
    cv2.imshow('7', img_blur_7)
    cv2.imshow('11', img_blur_11)
    cv2.waitKey(0)


splitting_and_merging()
