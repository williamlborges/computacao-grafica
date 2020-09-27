from PIL import Image # importar a biblioteca Pillow
mode = "RGB"
size = (4, 13)

img = Image.new(mode, size)
matriz = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if i == 0:
            matriz[i, j] = (255, 0, 25)
        elif i == 1:
            matriz[i, j] = (0, 255, 25)
        elif i == 2:
            matriz[i, j] = (90, 10, 90)
        elif i == 3:
            matriz[i, j] = (10, 30, 200)

img.save('imagem03rgb.png')
