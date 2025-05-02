from skimage import data

# Carrega as imagens pré-existentes do módulo skimage.data
coffee_image = data.coffee()
coins_image = data.coins()

# Mostra a forma de cada imagem
print("Forma de coffee_image:", coffee_image.shape)
print("Forma de coins_image:", coins_image.shape)

# Verifica se são coloridas (3 canais) ou em escala de cinza
def verificar_canais(imagem):
    if len(imagem.shape) == 2:
        return "Escala de cinza"
    elif len(imagem.shape) == 3 and imagem.shape[2] == 3:
        return "Colorida (RGB)"
    else:
        return "Formato desconhecido"

print("coffee_image é:", verificar_canais(coffee_image))
print("coins_image é:", verificar_canais(coins_image))
