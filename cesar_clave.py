
# Clave completando con el abecedario
# Clave CHAVEZMEJIA

ALPHABET1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
ALPHABET2 = ['C','H','A','V','E','Z','M','J','I','B','D','F','G','K','L','N','Ñ','O','P','Q','R','S','T','U','W','X','Y']

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

encryptMessage = encrypt(input("Ingrese un mensaje: "))
print(f"Mensaje encriptado: {encryptMessage}")
decryptMessage = decrypt(encryptMessage)
print(f"Mensaje desencriptado: {decryptMessage}")
