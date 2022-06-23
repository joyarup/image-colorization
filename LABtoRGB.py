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

    

print(lab2rgb([100,100,100]))

