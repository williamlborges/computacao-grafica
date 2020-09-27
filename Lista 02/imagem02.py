from PIL import Image # importar a biblioteca Pillow
mode = "RGB"
size = (4, 7)

img = Image.new(mode, size)
matriz = img.load()

for i in range(1, img.size[0]):
    for j in range(1, img.size[1] - 1):
        if i == 1:
            matriz[i, j] = (200, 200, 200)
        elif i == 2:
            matriz[i, j] = (120, 120, 120)
        elif i == 3:
            matriz[i, j] = (88, 88, 88)

img.save('imagem02Cinza.png')