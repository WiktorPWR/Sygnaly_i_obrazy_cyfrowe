import numpy as np
import cv2
import math


def bl_resize(original_img, new_h, new_w):
    old_h, old_w, c = original_img.shape
    resized = np.zeros((new_h, new_w, c))
    w_scale_factor = old_w / new_w if new_h != 0 else 0
    h_scale_factor = old_h / new_h if new_w != 0 else 0

    for i in range(new_h):
        for j in range(new_w):
            x = i * h_scale_factor
            y = j * w_scale_factor
            x_floor = math.floor(x)
            y_floor = math.floor(y)
            x_ceil = min(old_h - 1, math.ceil(x))
            y_ceil = min(old_w - 1, math.ceil(y))

            if x_ceil == x_floor and y_ceil == y_floor:
                resized[i, j, :] = original_img[x_floor, y_floor, :]
            elif x_ceil == x_floor:
                q1 = original_img[x_floor, y_floor, :]
                q2 = original_img[x_floor, y_ceil, :]
                resized[i, j, :] = q1 * (y_ceil - y) + q2 * (y - y_floor)
            elif y_ceil == y_floor:
                q1 = original_img[x_floor, y_floor, :]
                q2 = original_img[x_ceil, y_floor, :]
                resized[i, j, :] = q1 * (x_ceil - x) + q2 * (x - x_floor)
            else:
                v1 = original_img[x_floor, y_floor, :]
                v2 = original_img[x_ceil, y_floor, :]
                v3 = original_img[x_floor, y_ceil, :]
                v4 = original_img[x_ceil, y_ceil, :]
                q1 = v1 * (x_ceil - x) + v2 * (x - x_floor)
                q2 = v3 * (x_ceil - x) + v4 * (x - x_floor)
                resized[i, j, :] = q1 * (y_ceil - y) + q2 * (y - y_floor)

    return resized



image = cv2.imread("stalin.png")
resized300x500 = bl_resize(image, 300, 500)
mse_resized300x500 = np.sum((image - resized300x500) ** 2) / float(image.size)
cv2.imwrite("resized300x500.png", resized300x500)

print(mse_resized300x500)