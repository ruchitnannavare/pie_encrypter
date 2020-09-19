from dependencies import pi, e, randomizer, encryption_bits, characters


def encrypt(key, e_string):
    key_dict = {}
    if int(str(key)[3]) % 2 == 0:
        schema = e + pi + e
    else:
        schema = pi + e + pi
    randomize = str(key)[4] + schema[key - randomizer: key]
    randomize = int(randomize)
    if int(str(key)[3]) % 2 == 0:
        for alphabet in characters:
            eight_bit_key = schema[key:(key + encryption_bits)]
            int_string = ""
            for key_element in eight_bit_key:
                if int(key_element) % 2 == 0:
                    int_string = int_string + "1"
                else:
                    int_string = int_string + "0"

            key_dict[alphabet] = int_string
            key += encryption_bits + randomize
    else:
        for alphabet in characters:
            eight_bit_key = schema[key:(key + encryption_bits)]
            int_string = ""
            for key_element in eight_bit_key:
                if int(key_element) % 2 != 0:
                    int_string = int_string + "1"
                else:
                    int_string = int_string + "0"

            key_dict[alphabet] = int_string
            key += encryption_bits + randomize



    encrypted_string = ""
    for element in e_string:
        encrypted_string = encrypted_string + key_dict[str(element)]
    return encrypted_string



test_message = input("Type the message to encrypt "
                     "\n(English only, supports all "
                     "\nalphabets, numbers and "
                     "\nsymbols)                  :")
def encrypter():
    try:
        encryption_key = input("Give a six digit numeric only key to encrypt: ")
        int(encryption_key)
        if len(encryption_key) != 6:
            print("Please enter a 6 digit numeric only key")
        else:
            test = encrypt(int(encryption_key), test_message)
            print("Encrypted Message:", test)
            print("Length of the encrypted message: ", len(test))
    except:
        print("Please input numeric only key")
        encrypter()



encrypter()