def filtroBlur():
    blurFilter = img.filter(ImageFilter.BLUR)
    blurFilter.save('images/naturezaBlur.jpg')
    print('Filtro Blur aplicado.')
    # O filtro Blur borra a imagem.

def filtroContour():
    contourFilter = img.filter(ImageFilter.CONTOUR)
    contourFilter.save('images/naturezaContour.jpg')
    print('Filtro Contour aplicado.')

def filtroDetail():
    detailFilter = img.filter(ImageFilter.DETAIL)
    detailFilter.save('images/naturezaDetail.jpg')
    print('Filtro Detail aplicado.')
    # O filtro Detail destaca os detalhes de uma imagem.

def filterEdgeEnhance():
    edgeEnhanceFilter = img.filter(ImageFilter.EDGE_ENHANCE)
    edgeEnhanceFilter.save('images/naturezaEdgeEnhance.jpg')
    print('Filtro Edge Enhance aplicado.')
    # O filtro Edge Enhance destaca as bordas de uma imagem.

def filterEdgeEnhanceMore():
    edgeEnhanceMoreFilter = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    edgeEnhanceMoreFilter.save('images/naturezaEdgeEnhanceMore.jpg')
    print('Filtro Edge Enhance More aplicado.')
    # O filtro Edge Enhance More é uma aplicação maior do Edge Enhance,
    # destacando ainda mais as bordas da imagem.

def filterEmboss():
    embossFilter = img.filter(ImageFilter.EMBOSS)
    embossFilter.save('images/naturezaEmboss.jpg')
    print('Filtro Emboss aplicado.')
    # O filtro Emboss destaca os relevos da imagem

def filterFindEdges():
    findEgesFilter = img.filter(ImageFilter.FIND_EDGES)
    findEgesFilter.save('images/naturezaFindEdges.jpg')
    print('Filtro Find Edges aplicado.')


def filterSharpen():
    sharpenFilter = img.filter(ImageFilter.SHARPEN)
    sharpenFilter.save('images/naturezaSharpen.jpg')
    print('Filtro Sharpen aplicado.')
    # O filtro Sharpen melhora a nitidez da imagem.

def filterSmooth():
    smoothFilter = img.filter(ImageFilter.SMOOTH)
    smoothFilter.save('images/naturezaSmooth.jpg')
    print('Filtro Smooth aplicado.')
    # O filtro Smooth suaviza a imagem.

def filterSmoothMore():
    smoothFilterMore = img.filter(ImageFilter.SMOOTH_MORE)
    smoothFilterMore.save('images/naturezaSmoothMore.jpg')
    print('Filtro Smooth More aplicado.')
    # O filtro Smooth More aumenta um pouco mais a suavidade da imagem. 
   

if __name__ == "__main__":
    from PIL import Image, ImageFilter

    # Abrindo a imagem a ser trabalhada
    img = Image.open('images/natureza.jpg')

    filtroBlur()
    filtroContour()
    filtroDetail()
    filterEdgeEnhance()
    filterEdgeEnhanceMore()
    filterEmboss()
    filterFindEdges()
    filterSharpen()
    filterSmooth()
    filterSmoothMore()