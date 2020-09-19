from dependencies import pi, e, randomizer, encryption_bits, characters


def decrypt(key, d_string):
    decrypt_dic = {}
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

            decrypt_dic[int_string] = alphabet
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

            decrypt_dic[int_string] = alphabet
            key += encryption_bits + randomize

    decrypt_string = ""
    dec_pos = 0
    dec_list = []
    dec_no = len(d_string) / encryption_bits
    for dec_ele in range(int(dec_no)):
        dec_list.append(d_string[dec_pos:dec_pos + encryption_bits])
        dec_pos += encryption_bits

    for element in dec_list:
        decrypt_string = decrypt_string + decrypt_dic[element]

    return decrypt_string

def decrypting():
    try:
        test = input("Please enter message to be decrypted here : ")
        decryption_key = input("Give a numeric only key to decrypt: ")
        print("Decrypting...")
        print("Decrypted message:", decrypt(int(decryption_key), test))
        print("Decryption successful!")
    except:
        print("Sorry! Wrong key entered.")
        warning = input("Do you want to try again? Y/N ")
        if str(warning).upper() == "Y":
            decrypting()
        else:
            exit()

decrypting()