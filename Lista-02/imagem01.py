def criarBitmap():
    mode = "RGB"
    size = (11, 12)
    color = (255, 255, 255)
    img = Image.new(mode, size, color)
    matriz = img.load()

    
    matriz[5, 0] = (0, 0, 0) # pintando o pixel da linha 0

    # Esse for irá colorir as linhas 1 e 2
    for i in range(2, 0, -1):
        for j in range(3, img.size[0] - 3):
            if i != 1:
                matriz[j, i] = (0, 0, 0)
            elif i == 1 and j < 6:
                matriz[j+1, i] = (0, 0, 0)
            
    # Aqui irá colorir as duas linhas horizontais
    for i in range(2, img.size[0] - 2):
        for j in range(3, img.size[1], 7):
            matriz[i, j] = (0, 0, 0)

    # E aqui as colunas
    for i in range(2, 9, 6):
        for j in range(4, img.size[1] - 1):
            matriz[i, j] = (0, 0, 0)
    
    img.save('imagem01Bitmap.png')
    print('Imagem criada com sucesso!')

if __name__ == "__main__":

    from PIL import Image 

    criarBitmap()