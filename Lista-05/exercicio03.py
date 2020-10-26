def gama1p8():
    matrix = img.load()
    gama = 1.8

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = int((matrix[i, j][0] / 255) ** gama * 255)
            g = int((matrix[i, j][1] / 255) ** gama * 255)
            b = int((matrix[i, j][2] / 255) ** gama * 255)
            matrix[i, j] = (r, g, b)

    img.save('images/gama1p8.jpg')
    print('Gama 1.8 criada.')

def gama0p3():
    matrix = img.load()
    gama = 0.3

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = int((matrix[i, j][0] / 255) ** gama * 255)
            g = int((matrix[i, j][1] / 255) ** gama * 255)
            b = int((matrix[i, j][2] / 255) ** gama * 255)
            matrix[i, j] = (r, g, b)
    
    img.save('images/gama0p3.jpg')
    print('Gama 0.3 criada.')


if __name__ == "__main__":
        from PIL import Image
        img = Image.open('images/paisagem-natural.jpg')

        gama1p8()
        gama0p3()
    
