def camadaR():
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = matrix[i, j][0]
            matrix[i, j] = (r, 0, 0)
           
    img.save('images/camada_r.jpg')
    print('Camada R salva.')

def camadaG():
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            g = matrix[i, j][0]           
            matrix[i, j] = (0, g, 0)

    img.save('images/camada_g.jpg')
    print('Camada G salva.')

def camadaB():
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            b = matrix[i, j][1]
            matrix[i, j] = (0, 0, b)

    img.save('images/camada_b.jpg')
    print('Camada B salva.')


if __name__ == "__main__":
    from PIL import Image

    img = Image.open('images/paisagem-natural.jpg')
    matrix = img.load()

    camadaR()
    camadaG()
    camadaB()