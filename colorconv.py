import math
import numpy as np
import time


def rgb2lab(rgb):
    RGB = [0, 0, 0]
    for i in range(0, len(rgb)):
        RGB[i] = rgb[i] / 255.0

    X = RGB[0] * 0.4124 + RGB[1] * 0.3576 + RGB[2] * 0.1805
    Y = RGB[0] * 0.2126 + RGB[1] * 0.7152 + RGB[2] * 0.0722
    Z = RGB[0] * 0.0193 + RGB[1] * 0.1192 + RGB[2] * 0.9505
    XYZ = [X, Y, Z]
    XYZ[0] /= 95.045 / 100
    XYZ[1] /= 100.0 / 100
    XYZ[2] /= 108.875 / 100

    L = 0
    for i in range(0, 3):
        v = XYZ[i]
        if v > 0.008856:
            v = pow(v, 1.0 / 3)
            if i == 1:
                L = 116.0 * v - 16.0
        else:
            v *= 7.787
            v += 16.0 / 116
            if i == 1:
                L = 903.3 * XYZ[i]
        XYZ[i] = v

    a = 500.0 * (XYZ[0] - XYZ[1])
    b = 200.0 * (XYZ[1] - XYZ[2])
    Lab = [int(L), int(a), int(b)]
    return Lab


def lab2rgb(lab):
    L = lab[0]
    a = lab[1]
    b = lab[2]
    # d=6.0/29
    epsilon = 0.008856
    k = 0.206893
    d = k
    fy = math.pow((L + 16) / 116.0, 3)
    fx = fy + a / 500.0
    fz = fy - b / 200.0

    fy = (fy) if (fy > epsilon) else (L / 903.3)
    Y = fy
    fy = (math.pow(fy, 1.0 / 3)) if (fy > epsilon) else (7.787 * fy + 16.0 / 116)

    #====================================================XYZ[0]===================================================================================
    fx = fy + a / 500.0
    X = (math.pow(fx, 3.0)) if (fx > k) else ((fx - 16.0 / 116) / 7.787)

    #====================================================XYZ[2]===================================================================================
    fz = fy - b / 200.0
    Z = (math.pow(fz, 3.0)) if (fz > k) else ((fz - 16.0 / 116) / 7.787)

    X *= 0.95045
    Z *= 1.08875
    R = 3.240479 * X + (-1.537150) * Y + (-0.498535) * Z
    G = (-0.969256) * X + 1.875992 * Y + 0.041556 * Z
    B = 0.055648 * X + (-0.204043) * Y + 1.057311 * Z
    #R = max(min(R,1),0)
    #G = max(min(G,1),0)
    #B = max(min(B,1),0)
    RGB = [R, G, B]
    for i in range(0, 3):
        RGB[i] = min(int(round(RGB[i] * 255)), 255)
        RGB[i] = max(RGB[i], 0)
    return RGB

#DRIVER CODE; USE ONE COLOR VECTOR

lab = (rgb2lab([256, 180, 100]))
print(lab)

rgb = (lab2rgb(lab))

print(rgb)
