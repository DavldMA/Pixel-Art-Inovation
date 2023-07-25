from PIL import Image

def colorizeResult(image_path1, image_path2):
    try:
        image1 = Image.open(image_path1)
        image2 = Image.open(image_path2)

        new_image = Image.new('RGBA', image1.size)
        for x in range(image1.width):
            for y in range(image1.height):
                
                r1, g1, b1, a1 = image1.getpixel((x, y))
                r2, g2, b2, a2 = image2.getpixel((r1, g1))

                if r1 == g1 == b1 == 0:
                    new_image.putpixel((x, y), (r1, g1, b1, a1))

                else:
                    new_image.putpixel((x, y), (r2, g2, b2, a1))

        return new_image
    except Exception as e:
        raise ValueError(f"Error: {e}")
