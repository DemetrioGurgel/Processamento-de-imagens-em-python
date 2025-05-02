# Import the module
from skimage import morphology

# Obtenha a imagem dilatada
dilated_image = morphology.binary_dilation(world_image)

# Veja os resultados
show_image(world_image, 'Original')
show_image(dilated_image, 'Dilated image')