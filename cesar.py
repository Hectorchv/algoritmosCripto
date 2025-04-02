
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
K = 3

def encrypt(message):

    encryptMessage = ""
    for char in message:
        index = ALPHABET.index(char)
        newchar = ALPHABET[(index+K)%len(ALPHABET)]
        encryptMessage = encryptMessage + newchar
        
    return encryptMessage

def decrypt(encryptMessage):

    decryptMessage = ""

    for char in encryptMessage:
        index = ALPHABET.index(char)
        newchar = ALPHABET[(index-K)%len(ALPHABET)]
        decryptMessage = decryptMessage + newchar
    
    return decryptMessage

encryptMessage = encrypt(input("Ingrese un mensaje: "))
print(f"Mensaje encriptado: {encryptMessage}")
decryptMessage = decrypt(encryptMessage)
print(f"Mensaje desencriptado: {decryptMessage}")

