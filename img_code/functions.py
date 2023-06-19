from PIL import Image, ImageFilter

def processar_imagem(imagem):
    # Carrega a imagem
    img = Image.open(imagem)

    # Converte a imagem para escala de cinza
    img_cinza = img.convert("L")

    # Redução de ruído utilizando filtro de suavização
    img_suavizada = img_cinza.filter(ImageFilter.SMOOTH)

    # Retorne a imagem processada
    return img_suavizada

if __name__ == "__main__":
    imagem_processada = processar_imagem(r'C:\Users\Cougar_Gamer\Documents\GitHub\ark\img_code\raw_image.jpg')
    imagem_processada.show()
