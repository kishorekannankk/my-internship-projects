def caesar_cipher(text, shift):
    """
    Encrypts or decrypts the given text using the Caesar cipher with the specified shift.
    
    :param text: The text to be encrypted or decrypted.
    :param shift: The number of positions to shift the letters.
                  Use a positive number for encryption and a negative number for decryption.
    :return: The encrypted or decrypted text.
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the appropriate case for the letter
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
                
            # Apply the shift and wrap around if needed
            shifted = (ord(char) - base + shift) % 26 + base
            
            # Convert back to a character and append to result
            result += chr(shifted)
        else:
            # For non-alphabetic characters, just append them as they are
            result += char
            
    return result

def main():
    while True:
        print("Choose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher(message, -shift)
            print("Decrypted message:", decrypted_message)
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
