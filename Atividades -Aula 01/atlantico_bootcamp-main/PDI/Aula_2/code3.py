
from PDI.src.pdi_utils import load_building_image,show_image
building_image = load_building_image()

# Import Gaussian filter
from skimage.filters import gaussian

# Apply filter
gaussian_image = gaussian(building_image, 1)

# Show original and resulting image to compare
show_image(building_image, "Original")
show_image(gaussian_image, "Reduced sharpness Gaussian")