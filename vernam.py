CLAVE = "Santiago"


def vernamEncrypt(message):
    messageSplit = [message[i:i+8] for i in range(0, len(message), 8)]
    for idx in range(len(messageSplit)):
        text = messageSplit[idx]
        encrypted_text = ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(text, CLAVE))
        messageSplit[idx] = encrypted_text
    
    return ''.join(messageSplit)

message = input("Ingrese un mensaje: ")

messageEncrypt = vernamEncrypt(message)
messageDecrypt = vernamEncrypt(messageEncrypt)

print(f"Mensaje encriptado: {messageEncrypt}")
print(f"Mensaje desencriptado: {messageDecrypt}")
