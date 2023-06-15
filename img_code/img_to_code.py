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

# teste local
if __name__ == "__main__":

    # Carregue a imagem capturada do código de barras
    imagem = cv2.imread(r"C:\Users\Cougar_Gamer\Documents\GitHub\ark\img_code\raw_image.jpg")

    # Chame a função de processamento de imagem
    imagem_processada = processar_imagem(imagem)

    # Redimensione a janela de exibição
    cv2.namedWindow("Imagem Processada", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Imagem Processada", 960, 540)

    # Exiba a imagem original e a imagem processada para comparação (opcional)
    cv2.imshow("Imagem Processada", imagem_processada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
