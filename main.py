from PIL import Image
import os

def convert_png_to_webp(input_folder, output_folder, quality=80, lossless=False):
    # Check if the output folder exists, if not – create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".png"):
            input_file = os.path.join(input_folder, file_name)
            output_file = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.webp")

            try:
                # Open the PNG file
                img = Image.open(input_file)

                # Convert the image to WebP format with the specified quality or lossless setting
                if lossless:
                    img.save(output_file, format='WEBP', lossless=True)
                    print(f"Conversion successful: {output_file} (lossless)")
                else:
                    img.save(output_file, format='WEBP', quality=quality)
                    print(f"Conversion successful: {output_file} with quality {quality}")

            except Exception as e:
                print(f"An error occurred during the conversion of {file_name}: {e}")


# Example usage
input_folder = "input"  # folder with PNG files
output_folder = "output"  # folder for WebP files
convert_png_to_webp(input_folder, output_folder, quality=80, lossless=False)  # Change quality or set lossless=True