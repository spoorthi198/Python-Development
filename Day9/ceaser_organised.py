alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Combine the encrypt() and decrypt() functions into a single function called caesar().
def cipher(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift_amount
            end_text += alphabet[new_position]

        else:
            new_position = position - shift_amount
            end_text += alphabet[new_position]

    print(f"The {cipher_direction}d text is {end_text}")


#  Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

cipher(start_text=text, shift_amount=shift, cipher_direction=direction)