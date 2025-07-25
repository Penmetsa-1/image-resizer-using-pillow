import os
from PIL import Image

# Input and Output folders
input_folder = "images"
output_folder = "resized"

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Resize configuration
new_size = (300, 300)  # width, height

# Process each image
for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".png", ".jpeg")):
        try:
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            img_resized = img.resize(new_size)
            
            # Save as PNG (optional: change format)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.png")
            img_resized.save(output_path)
            print(f"Resized and saved: {output_path}")
        except Exception as e:
            print(f"Failed to process {filename}: {e}")