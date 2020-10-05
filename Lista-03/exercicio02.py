'''
Correção gama de uma imagem
    É um filtro que, dependendo o valor gama aplicada a essa imagem, 
    ela se torna mais clara, recebendo tons de branco ou mais escura, 
    com tons de preto. Quanto maior o gama aplicado mais escura se 
    tornará a imagem

'''

# Letra A: Use uma imagem em escala de cinza e faça um código para a correção 
# gama desta imagem para os valores de gama 0.25, 0.5, 1, 2, 3.
  
def gama025Cinza():
    img = Image.open('images/xadrez.jpg')
    matriz = img.load()

    gama = 0.25
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = int((matriz[i, j][0]/255) ** gama * 255)
            g = int((matriz[i, j][1]/255) ** gama * 255)
            b = int((matriz[i, j][2]/255) ** gama * 255)
            matriz[i, j] = (r, g, b)
    
    img.save('images/02/xadrez025Cinza.jpg')
    
def gama050Cinza():
    img = Image.open('images/xadrez.jpg')
    matriz = img.load()

    gama = 0.50
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = int((matriz[i, j][0]/255) ** gama * 255)
            g = int((matriz[i, j][1]/255) ** gama * 255)
            b = int((matriz[i, j][2]/255) ** gama * 255)
            matriz[i, j] = (r, g, b)
    
    img.save('images/02/xadrez050Cinza.jpg')

def gama1Cinza():
    img = Image.open('images/xadrez.jpg')
    matriz = img.load()

    gama = 1
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = int((matriz[i, j][0]/255) ** gama * 255)
            g = int((matriz[i, j][1]/255) ** gama * 255)
            b = int((matriz[i, j][2]/255) ** gama * 255)
            matriz[i, j] = (r, g, b)
    
    img.save('images/02/xadrez1Cinza.jpg')

def gama2Cinza():
    img = Image.open('images/xadrez.jpg')
    matriz = img.load()

    gama = 2
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = int((matriz[i, j][0]/255) ** gama * 255)
            g = int((matriz[i, j][1]/255) ** gama * 255)
            b = int((matriz[i, j][2]/255) ** gama * 255)
            matriz[i, j] = (r, g, b)
    
    img.save('images/02/xadrez2Cinza.jpg')

def gama3Cinza():
    img = Image.open('images/xadrez.jpg')
    matriz = img.load()

    gama = 3
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = int((matriz[i, j][0]/255) ** gama * 255)
            g = int((matriz[i, j][1]/255) ** gama * 255)
            b = int((matriz[i, j][2]/255) ** gama * 255)
            matriz[i, j] = (r, g, b)
    
    img.save('images/02/xadrez3Cinza.jpg')

# Letra B: Use uma imagem colorida e faça um código para a correção gama 
# desta imagem para os valores de gama 0.25, 0.5, 1, 2, 3.

def gama025Colorido():
    img = Image.open('images/louroJose.jpg')
    matriz = img.load()

    gama = 0.25
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = int((matriz[i, j][0]/255) ** gama * 255)
            g = int((matriz[i, j][1]/255) ** gama * 255)
            b = int((matriz[i, j][2]/255) ** gama * 255)
            matriz[i, j] = (r, g, b)
    
    img.save('images/02/louro025Colorida.jpg')

def gama050Colorida():
    img = Image.open('images/louroJose.jpg')
    matriz = img.load()

    gama = 0.50
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = int((matriz[i, j][0]/255) ** gama * 255)
            g = int((matriz[i, j][1]/255) ** gama * 255)
            b = int((matriz[i, j][2]/255) ** gama * 255)
            matriz[i, j] = (r, g, b)
    img.save('images/02/louro050Colorido.jpg')

def gama1Colorida():
    img = Image.open('images/louroJose.jpg')
    matriz = img.load()

    gama = 1
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = int((matriz[i, j][0]/255) ** gama * 255)
            g = int((matriz[i, j][1]/255) ** gama * 255)
            b = int((matriz[i, j][2]/255) ** gama * 255)
            matriz[i, j] = (r, g, b)
    img.save('images/02/louro1Colorido.jpg')

def gama2Colorida():
    img = Image.open('images/louroJose.jpg')
    matriz = img.load()

    gama = 2
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = int((matriz[i, j][0]/255) ** gama * 255)
            g = int((matriz[i, j][1]/255) ** gama * 255)
            b = int((matriz[i, j][2]/255) ** gama * 255)
            matriz[i, j] = (r, g, b)
    img.save('images/02/louro2Colorido.jpg')

def gama3Colorida():
    img = Image.open('images/louroJose.jpg')
    matriz = img.load()

    gama = 3
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = int((matriz[i, j][0]/255) ** gama * 255)
            g = int((matriz[i, j][1]/255) ** gama * 255)
            b = int((matriz[i, j][2]/255) ** gama * 255)
            matriz[i, j] = (r, g, b)
    img.save('images/02/louro3Colorido.jpg')


if __name__ == "__main__":
    from PIL import Image

    #Letra A
    gama025Cinza()
    gama050Cinza()
    gama1Cinza()
    gama2Cinza()
    gama3Cinza()
    # ---------------------------------------------------------------
    
    # Letra B
    gama025Colorido()
    gama050Colorida()
    gama1Colorida()
    gama2Colorida()
    gama3Colorida()
    
    # O que se percebe como resultado para valores de gama menores do que 1? 
    # E para valores maiores do que 1?
    '''
    Quando os valores de gama são menores que 1 a imagem tende a ficar cada vez
    mais clara.
    Quando esses valores são maiores que 1 a imagem tende a ficar cada vez mais escura.
    '''

