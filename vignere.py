from itertools import starmap, cycle

# vignere_ cipher

def vigenere_cipher(passed_key, msg, crypto, text_type):
    text = msg
    key = passed_key

    def encrypt(message, key):
        message = filter(str.isalpha, message.upper())

        def enc(c, k):
            return chr(((ord(k) + ord(c) - 2 * ord('A')) % 26) + ord('A'))
        return ''.join(starmap(enc, zip(message, cycle(key))))

    def decrypt(message, key):

        def dec(c, k):
            return chr(((ord(c) - ord(k) - 2 * ord('A')) % 26) + ord('A'))
        return ''.join(starmap(dec, zip(message, cycle(key))))

    encr = encrypt(text, key)
    decr = decrypt(encr, key)

    if crypto == 'Encryption' and text_type == 'Plaintext':
        return 'Original: ' + text + '\nEncrypted: ' + encr
    elif crypto == 'Decryption' and text_type == 'Cipher text':
        return 'Original: ' + text + '\nDecrypted: ' + decr
    else:
        return 'Please select the proper text type.'