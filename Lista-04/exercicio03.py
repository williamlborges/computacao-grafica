from PIL import Image

img = Image.open('images/onça.png')

# Converte a imagem para escala de Cinza
# O parâmetro L representa a conversão para escala de cinza.

img_escala_de_cinza = img.convert('L') 

img_escala_de_cinza.save('images/escalaDeCinza.png')

