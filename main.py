import base64

def caesar_decrypt(text, shift):
    """
    Decrypt Caesar cipher by shifting characters backwards
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift backwards (subtract shift value)
            shifted = (ord(char) - start - shift) % 26
            result += chr(start + shifted)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result

def base64_decrypt(text):
    """
    Decode Base64 encoded text
    """
    try:
        # Remove any whitespace and decode
        decoded_bytes = base64.b64decode(text.strip())
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        print(f"Base64 decoding error: {e}")
        return None

def multi_layer_decrypt(encrypted_text):
    """
    Decrypt text with multiple layers:
    1. Caesar cipher shift 10 (decrypt first)
    2. Base64 decode
    3. Caesar cipher shift 13 (decrypt)
    4. Base64 decode (final)
    
    Note: We decrypt in reverse order of encryption
    """
    print(f"Starting decryption of: {encrypted_text}\n")
    
    # Step 1: Decrypt Caesar cipher with shift 10
    step1 = caesar_decrypt(encrypted_text, 10)
    print(f"Step 1 - Caesar decrypt (shift 10): {step1}")
    
    # Step 2: Decode Base64
    step2 = base64_decrypt(step1)
    if step2 is None:
        print("Failed at Base64 decoding step 2")
        return None
    print(f"Step 2 - Base64 decode: {step2}")
    
    # Step 3: Decrypt Caesar cipher with shift 13 (ROT13)
    step3 = caesar_decrypt(step2, 13)
    print(f"Step 3 - Caesar decrypt (shift 13/ROT13): {step3}")
    
    # Step 4: Final Base64 decode
    final_result = base64_decrypt(step3)
    if final_result is None:
        print("Failed at final Base64 decoding step")
        return None
    print(f"Step 4 - Final Base64 decode: {final_result}")
    
    return final_result

//encrypted password : "AFPYWOBECGhgotvc"

if __name__ == "__main__":
    print("=== Multi-Layer Decryption Tool ===\n")
    print("Decryption layers: Caesar(-10) -> Base64 -> Caesar(-13) -> Base64\n")
    
    while True:
        encrypted_text = input("Enter encrypted text to decrypt (or 'quit' to exit): ").strip()
        
        if encrypted_text.lower() == 'quit':
            print("Goodbye!")
            break
        
        if encrypted_text:
            print("\n" + "="*50)
            print("DECRYPTION PROCESS:")
            print("="*50)
            result = multi_layer_decrypt(encrypted_text)
            if result:
                print(f"\n🎉 FINAL DECRYPTED TEXT: {result}")
            else:
                print("\n❌ Decryption failed!")
            print("="*50 + "\n")
        else:
            print("Please enter some text to decrypt.\n")
