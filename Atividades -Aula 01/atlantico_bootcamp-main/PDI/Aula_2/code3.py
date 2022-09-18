
from PDI.src.pdi_utils import load_building_image,show_image
building_image = load_building_image()

# Import Gaussian filter
from skimage.filters import gaussian

# Apply filter
gaussian_image1 = gaussian(building_image, 1)
gaussian_image5 = gaussian(building_image, 5)
gaussian_image10 = gaussian(building_image, 10)

# Show original and resulting image to compare
show_image(building_image, "Original")
show_image(gaussian_image1, "Reduced sharpness Gaussian - sigma 1")
show_image(gaussian_image5, "Reduced sharpness Gaussian - sigma 5")
show_image(gaussian_image10, "Reduced sharpness Gaussian - sigma 10")