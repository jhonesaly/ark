import cv2

# Processamento da imagem

import cv2

def processar_imagem(imagem):
    # Converte a imagem para escala de cinza
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Redução de ruído utilizando filtro bilateral
    imagem = cv2.bilateralFilter(imagem, 9, 75, 75)

    # Retorne a imagem processada
    return imagem
