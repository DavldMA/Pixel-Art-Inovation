from PIL import Image

def colorizeResult(image_path1, image_path2):
    try:
        # Load the images
        image1 = Image.open(image_path1)
        image2 = Image.open(image_path2)

        # Create a new empty image with the same size as the first image
        new_image = Image.new('RGBA', image1.size)

        # Iterate over each pixel in the first image
        for x in range(image1.width):
            for y in range(image1.height):
                
                r1, g1, b1, a1 = image1.getpixel((x, y))
                r2, g2, b2, a2 = image2.getpixel((r1, g1))

                if r1 == g1 == b1 == 0:
                    # Use invisible pixel
                    new_image.putpixel((x, y), (r1, g1, b1, a1))

                else:
                    # Use the pixel color from the second image
                    new_image.putpixel((x, y), (r2, g2, b2, a1))

        # Return the new image
        return new_image
    except Exception as e:
        raise ValueError(f"Error: {e}")