from PIL import Image, ImageFilter

# Abrindo imagem original e aplicando Sharpen
def f_sharpen():
    original = Image.open('images/natureza.jpg')
    sharpen = ImageFilter.Kernel((3, 3), (0, -1, 0, -1, 5, -1, 0, -1, 0), 1, 0)
    filtro_sharpen = original.filter(sharpen)
    filtro_sharpen.save('images/filtro_sharpen.jpeg')
    print('\nFiltro sharpen aplicado.')

# Abrindo imagem sharpen criada e aplicando nela o filtro mediana
def boxBlur():
    original = Image.open('images/filtro_sharpen.jpeg')
    mediana = ImageFilter.Kernel((3, 3), (1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9), 1, 0)
    filtro_sharpen_mediana = original.filter(mediana)
    filtro_sharpen_mediana.save('images/filtro_sharpen_mediana.jpeg')
    print('\nMediana aplicado sobre a imagem com sharpen.\n')

if __name__ == "__main__":

    f_sharpen()
    boxBlur()
