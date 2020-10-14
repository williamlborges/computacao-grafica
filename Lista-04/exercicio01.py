from PIL import Image, ImageFilter

original = Image.open('images/original.jpeg')

# Criandos os kernels
filtro_1 = ImageFilter.Kernel((3, 3), (1, 0, -1, 0, 0, 0, -1, 0, 1), 1, 0)
filtro_2 = ImageFilter.Kernel((3, 3), (0, 1, 0, 1, -4, 1, 0, 1, 0), 1, 0)
filtro_3 = ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8, -1, -1, -1, -1), 1, 0)

# Aplicando os kernels na imagem
image_1 = original.filter(filtro_1)
image_2 = original.filter(filtro_2)
image_3 = original.filter(filtro_3)

# Salvando as imagens
image_1.save('images/imagem1.jpeg')
image_2.save('images/imagem2.jpeg')
image_3.save('images/imagem3.jpeg')

print('Os três filtros foram aplicados com sucesso!')