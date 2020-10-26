from math import log
from PIL import Image

img = Image.open('images/paisagem-natural.jpg')
c = 255 / log(255+1, 10)
matrix = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = int(c * log(matrix[i, j][0] + 1, 10))
        g = int(c * log(matrix[i, j][1] + 1, 10))
        b = int(c * log(matrix[i, j][2] + 1, 10))
        matrix[i, j] = (r, g, b)
img.save('images/imagemLogaritmica.jpg')
print('Imagem com transformação logaritmica criada.')