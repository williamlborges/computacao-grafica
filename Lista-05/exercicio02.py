from PIL import Image

img = Image.open('images/paisagem-natural.jpg')

matrix = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = 255 - matrix[i, j][0]
        g = 255 - matrix[i, j][1]
        b = 255 - matrix[i, j][2]
        matrix[i, j] = (r, g, b)

img.save('images/paisagemNegativo.jpg')
print('Imagem criada.')