from tkinter import filedialog, Tk
import tkinter.messagebox as messagebox
import shutil

def ask_replace_image(image_path):
    try:
        # check if the existing image should be replaced
        replace = messagebox.askyesno("Replace Image", f"Do you want to replace the existing image at {image_path}?")

        # if the user chooses to replace the image, select a new image and copy it
        if replace:
            # create a file dialog to select the new image
            root = Tk()
            root.withdraw()
            new_image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("PNG Files", "*.png")])

            # copy the selected image to the destination folder
            if new_image_path:
                shutil.copy(new_image_path, image_path)

        return image_path if not replace else new_image_path
    
    except Exception as e:
        raise ValueError(f"Error: {e}")