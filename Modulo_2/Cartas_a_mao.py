# Import the morphology module
from skimage import morphology

# Tente usar a função binary_erosion para a operação morfológica
eroded_image_shape = morphology.binary_erosion(upper_r_image)

# Veja os resultados
show_image(upper_r_image, 'Original')
show_image(eroded_image_shape, 'Eroded image')