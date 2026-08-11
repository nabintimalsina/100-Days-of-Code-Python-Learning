import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Enter the text: \n").lower()
shift = int(input("Enter the shift number: \n"))

def encode(text, shift):  #(nabin, 3)
    cipher_text = ""  #declare string variable to store the encoded text
    for letter in text: #iterate through each letter in the text -> nabin
        if letter in alphabet: #n in alphabet b in alphabet a in alphabet b in alphabet i in alphabet n in alphabet
            position = alphabet.index(letter) # n positoin, a position, b position, i position
            new_position = (position + shift) % 26  # new position = (13 + 3) % 26 = 16, (0 + 3) % 26 = 3, (1 + 3) % 26 = 4, (8 + 3) % 26 = 11, (13 + 3) % 26 = 16
            cipher_text += alphabet[new_position]  # modulus helps to find the remaining position in the alphabet list.
        else:
            cipher_text += letter
    print(f"The encoded text is: {cipher_text}")

def decode(text, shift):
    plain_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += letter
    print(f"The decoded text is: {plain_text}")

encode(text, shift) if direction == "encode" else decode(text, shift)



