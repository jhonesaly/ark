# Projeto Ark

Envolve vários softwares de automação

## Ark Storage

### Leitor de código de barras

Para entender o funcionamento do código de barras:

https://www.youtube.com/watch?v=1uJttCNfjLA&list=TLPQMTUwNjIwMjOD4DZFD-VJkw&index=2&ab_channel=IntegrandoConhecimento

#### Algoritmo img_to_code

- Início do algoritmo
- Leia a imagem capturada do código de barras.
- Processamento da imagem:
  - Converta a imagem para escala de cinza.
  - Aplique técnicas de pré-processamento, como redimensionamento, ajuste de contraste, remoção de ruído, se necessário.
- Identificação do código de barras:
  - Utilize uma biblioteca de processamento de código de barras, como a biblioteca pyzbar.
  - Aplique a função de decodificação para identificar o código de barras na imagem processada.
  - Extraia o valor do código de barras decodificado.
- Verificação do código de barras:
  - Verifique se o código de barras é válido e está presente no banco de dados.
  - Se o código de barras não for válido ou não estiver no banco de dados, exiba uma mensagem de erro adequada ao usuário.
- Fim do algoritmo

#### Autenticação

https://isbnsearch.org/isbn/9786555521689
