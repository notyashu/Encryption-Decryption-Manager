# affine cipher 

def affine_cipher(a, b, msg, crypto, text_type):
    text = msg
    KEY = (int(a), int(b), 55)
    DIE = 128

    def encrypt_char(char):
        K1, K2, kI = KEY
        return chr((K1 * ord(char) + K2) % DIE)

    def encrypt(string):
        return "".join(map(encrypt_char, string))

    def decrypt_char(char):
        K1, K2, KI = KEY
        return chr(KI * (ord(char) - K2) % DIE)

    def decrypt(string):
        return "".join(map(decrypt_char, string))

    encr = encrypt(text)
    decr = decrypt(text)

    if crypto == 'Encryption' and text_type == 'Plaintext':
        return 'Original: ' + text + '\nEncrypted: ' + encr
    elif crypto == 'Decryption' and text_type == 'Cipher text':
        return 'Original: ' + text + '\nDecrypted: ' + decr
    else:
        return 'Please select the proper text type.'
    