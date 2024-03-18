from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    """
    Encrypts the given image using a simple pixel manipulation technique.
    
    Args:
        image_path: Path to the input image file.
        key: Encryption key (integer).
    
    Returns:
        encrypted_image: Encrypted image as a NumPy array.
    """
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Apply encryption to each pixel
    encrypted_image_array = (img_array + key) % 256
    
    return encrypted_image_array

def decrypt_image(encrypted_image_array, key):
    """
    Decrypts the given encrypted image using the provided key.
    
    Args:
        encrypted_image_array: NumPy array of the encrypted image.
        key: Encryption key (integer).
    
    Returns:
        decrypted_image: Decrypted image as a NumPy array.
    """
    # Apply decryption to each pixel
    decrypted_image_array = (encrypted_image_array - key) % 256
    
    return decrypted_image_array

def save_image(image_array, output_path):
    """
    Saves the given image array as an image file.
    
    Args:
        image_array: NumPy array of the image.
        output_path: Path to save the output image file.
    """
    # Create an image from the array
    img = Image.fromarray(image_array.astype(np.uint8))
    img.save(output_path)
    print("Image saved successfully!")

def main():
    # Input image and encryption key
    image_path = input("Enter the path to the image file: ")
    key = int(input("Enter the encryption key (integer): "))
    
    # Encrypt the image
    encrypted_image_array = encrypt_image(image_path, key)
    
    # Save the encrypted image
    encrypted_output_path = "encrypted_image.png"
    save_image(encrypted_image_array, encrypted_output_path)
    print("Image encrypted and saved as:", encrypted_output_path)
    
    # Decrypt the image
    decrypted_image_array = decrypt_image(encrypted_image_array, key)
    
    # Save the decrypted image
    decrypted_output_path = "decrypted_image.png"
    save_image(decrypted_image_array, decrypted_output_path)
    print("Image decrypted and saved as:", decrypted_output_path)

if __name__ == "__main__":
    main()
