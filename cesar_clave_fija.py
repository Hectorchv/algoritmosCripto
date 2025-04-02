
# Clave completando con el abecedario
# Clave ARIDO

ALPHABET2 = ['A','R','I','D','O']
ALPHABET1 = ['E','X','I','T','O']

def encrypt(message):

    encryptMessage = ""
    for char in message:
        index = ALPHABET1.index(char)
        newchar = ALPHABET2[(index)]
        encryptMessage = encryptMessage + newchar
        
    return encryptMessage

def decrypt(encryptMessage):

    decryptMessage = ""

    for char in encryptMessage:
        index = ALPHABET2.index(char)
        newchar = ALPHABET1[index]
        decryptMessage = decryptMessage + newchar
    
    return decryptMessage

encryptMessage = encrypt(input("Mensaje: "))
print(f"Mensaje encriptado: {encryptMessage}")
decryptMessage = decrypt(encryptMessage)
print(f"Mensaje desencriptado: {decryptMessage}")
