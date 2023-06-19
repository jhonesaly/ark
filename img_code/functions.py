from PIL import Image, ImageFilter
from pyzbar.pyzbar import decode

def processar_imagem(imagem):
    # Carrega a imagem
    img = Image.open(imagem)

    # Converte a imagem para escala de cinza
    img_cinza = img.convert("L")

    # Redução de ruído utilizando filtro de suavização
    img_suavizada = img_cinza.filter(ImageFilter.SMOOTH)

    # Retorne a imagem processada
    return img_suavizada

def ler_codigo_de_barras(imagem):
    # Carrega a imagem
    img = Image.open(imagem)
    
    # Decodifica os códigos de barras presentes na imagem
    codigos = decode(img)
    
    if len(codigos) > 0:
        # Retorna a sequência numérica do primeiro código de barras encontrado
        return codigos[0].data.decode('utf-8')
    
    # Caso nenhum código de barras seja encontrado, retorna None
    return None

if __name__ == "__main__":
    imagem_processada = processar_imagem(r'C:\Users\Cougar_Gamer\Documents\GitHub\ark\img_code\raw_image.jpg')
    imagem_processada.show()

    cod_barras = ler_codigo_de_barras(r'C:\Users\Cougar_Gamer\Documents\GitHub\ark\img_code\raw_image.jpg')
    print(cod_barras)
