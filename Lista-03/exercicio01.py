'''
Negativo de uma imagem
  É um filtro que, nas imagens em escala de cinza, transforma o que é branco em preto,
  e o que é preto fica branco, ou seja, é o netativo da intensidade.
  Nas imagens coloridas também funcionam da mesma forma, onde cada cor irá ter sua cor
  negativa correspondente.
  
'''

# Letra A: Faça um código para gerar o negativo de uma imagem colorida.
def negativoColorida():
    img = Image.open('images/paisagem.jpg')
    matriz = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = 255 - matriz[i, j][0]
            g = 255 - matriz[i, j][1]
            b = 255 - matriz[i, j][2]
            matriz[i, j] = (r, g, b)

    img.save('images/01/negativoPaisagem.jpg')
    print('Imagem gerada')

# Letra B: Faça um código para gerar o negativo de uma imagem em escala de cinza.
def negativoCinza():
    img = Image.open('images/bichano.jpg')
    matriz = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = 255 - matriz[i, j][0]
            g = 255 - matriz[i, j][1]
            b = 255 - matriz[i, j][2]
            matriz[i, j] = (r, g, b)

    img.save('images/01/negativoBichano.jpg')
    print('Imagem gerada')


if __name__ == "__main__":
    from PIL import Image

    negativoColorida()
    negativoCinza()

