from PIL import Image

def embed_lsb_secret(cover_image_path, secret_image_path, output_image_path):
    # Open the cover image and convert it to grayscale
    cover_image = Image.open(cover_image_path).convert('L')

    # Open the secret image and convert it to grayscale if it's not already
    secret_image = Image.open(secret_image_path).convert('L')

    # Ensure both images have the same dimensions
    if cover_image.size != (256, 256) or secret_image.size != (256, 256):
        raise ValueError("Both images must be 256x256 pixels.")

    # Create a new image for the steganographic result
    stego_image = cover_image.copy()

    # Iterate over each pixel in the secret image and embed it into the cover image
    for x in range(256):
        for y in range(256):
            cover_pixel = cover_image.getpixel((x, y))
            secret_pixel = secret_image.getpixel((x, y))

            # Modify the cover pixel's least significant bit to hide the secret pixel
            stego_pixel = cover_pixel & 0xFE | (secret_pixel >> 7)

            # Update the stego image with the modified pixel
            stego_image.putpixel((x, y), stego_pixel)

    # Save the stego image
    stego_image.save(output_image_path)

# Example usage
cover_image_path = "cover.jpeg"  # Replace with your cover image file path
secret_image_path = "secret.jpeg"  # Replace with your secret image file path
output_image_path = "stego_image.png"  # Replace with the desired output file path

embed_lsb_secret(cover_image_path, secret_image_path, output_image_path)