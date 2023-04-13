from PIL import Image
import os

def sourceGenerator(image_path1, image_path2):
    # Check if the file exists
    if not os.path.isfile(image_path2):
        raise ValueError(f"Error: file {image_path2} not found")
    
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
                
                # Find the pixel in the second image with the same color
                for x2 in range(image2.width):
                    for y2 in range(image2.height):
                        r2, g2, b2, a2 = image2.getpixel((x2, y2))
                        if (r1, g1, b1, a1) == (r2, g2, b2, a2):
                            # Create a new pixel with the position of the first image and the color of the second image
                            new_pixel = (x2, y2, b2, a2)
                            new_image.putpixel((x, y), new_pixel)
                            break

        # Return the new image
        return new_image
    except Exception as e:
        raise ValueError(f"Error: {e}")