import math
def lab2rgb(inputColor):
    lab = [inputColor[0],inputColor[1],inputColor[2]]

    y = (lab[0] + 16) / 116
    x = lab[1] / 500 + y
    z = y - lab[2] / 200


    if x ** 3 > 0.008856:
        x = (x ** 3) * 0.95047
    else:
        x = (x - 16/116) / 7.787

    if lab[0] > 7.999:
        y = (y ** 3)
    else:
        y = lab[0] / 903.3

    if z ** 3 > 0.008856:
        z = (z ** 3) * 1.08883
    else:
        z = (z - 16/116) / 7.787

    r = x * 3.2406 + y * -1.5372 + z * -0.4986
    g = x * -0.9689 + y * 1.8758 + z * 0.0415
    b = x * 0.0557 + y * -0.2040 + z * 1.0570

    if r > 0.0031308:
        r = (1.055 * math.pow(r, 1/2.4) - 0.055)
    else:
        r = r * 12.92
    if r > 0.0031308:
        g = (1.055 * math.pow(g, 1/2.4) - 0.055)
    else:
        g = g * 12.92
    if b > 0.0031308:
        b = (1.055 * math.pow(b, 1/2.4) - 0.055)
    else:
        b = b * 12.92


    return [max(0, min(1, r)) * 255,
            max(0, min(1, g)) * 255,
            max(0, min(1, b)) * 255]



print(lab2rgb([60,-50,51]))

