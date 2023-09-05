from easygui import buttonbox, multpasswordbox
from vignere import  vigenere_cipher
from affine import affine_cipher

title = "Encryption and Decryption Manager"


def main():
    msg1 = "Hello, please pick a cryptosystem."
    crypto_choices = ["Encryption", "Decryption"]
    crypto_mode = buttonbox(msg1, title, choices=crypto_choices)

    msg2 = "Please pick a crypto mode to use."
    cryptosystem_choicess = ["Affine Cipher", "Vigenere Cipher"]
    cryptosystem_mode = buttonbox(msg2, title, choices=cryptosystem_choicess)

    msg3 = "Would you like plaintext or cipher text?"
    text_choices = ["Plaintext", "Cipher text"]
    text_mode = buttonbox(msg3, title, choices=text_choices)

    msg4 = "Please enter your text and key."
    if cryptosystem_mode == 'Affine Cipher':
        field_names = ["Text", "A", "B"]
        field_values = multpasswordbox(msg4, title, field_names)
        # make sure that none of the fields was left blank
        while 1:
            if field_values is None:
                break
            errmsg = ""
            for i in range(len(field_names)):
                if field_values[i].strip() == "":
                    errmsg = errmsg + ('"%s" is a required field.\n\n' % field_names[i])
            if errmsg == "":
                break  # no problems found
            field_values = multpasswordbox(errmsg, title, field_names, field_values)

        my_text = field_values[0]
        a = field_values[1]
        b = field_values[2]
        print("[Affine Cipher]")
        print('%s message' % (crypto_mode.title()))
        print(affine_cipher(a, b, my_text, crypto_mode, text_mode))

    elif cryptosystem_mode == 'Vigenere Cipher':
        field_names = ["Text", "Key"]
        field_values = multpasswordbox(msg4, title, field_names)
        # make sure that none of the fields was left blank
        while 1:
            if field_values is None:
                break
            errmsg = ""
            for i in range(len(field_names)):
                if field_values[i].strip() == "":
                    errmsg = errmsg + ('"%s" is a required field.\n\n' % field_names[i])
            if errmsg == "":
                break  # no problems found
            field_values = multpasswordbox(errmsg, title, field_names, field_values)

        my_text = field_values[0]
        my_key = field_values[1]
        print("[Vigenere Cipher]")
        print('%s message' % (crypto_mode.title()))
        print(vigenere_cipher(my_key, my_text, crypto_mode, text_mode))


if __name__ == '__main__':
    main()