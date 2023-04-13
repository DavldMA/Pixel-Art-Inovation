from sourceCreator import sourceGenerator
from general import ask_replace_image
from colorizer import colorizeResult
from colorama import Fore, Style
from tqdm import tqdm
import sys
import os

# Get the folders paths
try:
    if os.path.exists("PixelArt"):
        inputFolder = "PixelArt/input/"
        outputFolder = "PixelArt/output/"
    else:
        inputFolder = "input/"
        outputFolder = "output/"
except Exception as e:
    print(Fore.RED + Style.BRIGHT + "The folders does not exist or aren't on the right place." + Style.RESET_ALL)

skinsFolder = inputFolder + "Skins/" # Different Skins texture
overlayPath = inputFolder + 'Overlay/' # Model with UV Map colors
mapPath = inputFolder + 'MAP/imgMap.png' # UV Map in 2d
sourcePath = inputFolder + 'Source/imgSource.png' # Is auto generated

try:
    mapPath = ask_replace_image(mapPath)

    # Get the total number of iterations
    total_iterations = len(os.listdir(skinsFolder)) * len(os.listdir(overlayPath))

    # Loop through all the skins and overlays
    with tqdm(total=total_iterations, desc="Processing") as pbar:
        print("\n")

        # Create a list to hold image errors
        image_errors = []

        for skin_file in os.listdir(skinsFolder):
            # check if the file is a PNG image
            if not skin_file.endswith(".png"):
                continue

            # construct the paths to the input and output skins
            skin_path = skinsFolder + skin_file
            skin_name = os.path.splitext(skin_file)[0]

            for overlay_file in os.listdir(overlayPath):
                # check if the file is a PNG image
                if not overlay_file.endswith(".png"):
                    continue

                # construct the paths to the input and output overlays
                overlay_path = overlayPath + overlay_file
                overlay_name = os.path.splitext(overlay_file)[0]
                output_path = outputFolder + skin_name + '_' + overlay_name + '.png'

                try:
                    # generate the source image and colorize it
                    sourceImage = sourceGenerator(overlay_path, mapPath)
                    sourceImage.save(sourcePath)
                    colorizedImage = colorizeResult(sourcePath, skin_path)
                    colorizedImage.save(output_path)

                except Exception as e:
                    # Append the error to the image_errors list
                    image_errors.append(overlay_file)
                    continue

                # increment the progress bar
                pbar.update(1)

        # Check if there were any errors
        if image_errors:
            print(Fore.RED + Style.BRIGHT + "Errors occurred while processing the following images:")
            for error in image_errors:
                print(f"- {error}")
            print(Style.RESET_ALL)
        else:
            print(Fore.GREEN + Style.BRIGHT + "All Images Saved Successfully" + Style.RESET_ALL)

except Exception as e:
    sys.exit(1)
