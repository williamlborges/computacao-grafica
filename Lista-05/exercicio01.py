from PIL import Image

img = Image.open('images/paisagem-natural.jpg')

matrix = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = matrix[i, j][0]
        g = matrix[i, j][1]
        b = matrix[i, j][2]
        pixel = int((r + g + b) / 3)
        matrix[i, j] = (pixel, pixel, pixel)

img.save('images/paisagemEscalaDeCinza.jpg')

        