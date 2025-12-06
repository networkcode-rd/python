# Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    final_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            final_text += letter
        else:
            new_position = alphabet.index(letter) + shift_amount
            shifted_position = new_position % len(alphabet)
            final_text += alphabet[shifted_position]

    print(f" Here is the encoded result: {final_text}")

need_to_continue = True

while need_to_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to continue again. Else type 'no'.\n").lower()
    if restart == "no":
        need_to_continue = False
        print("Good Luck!")
