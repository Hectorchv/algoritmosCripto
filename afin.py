MESSAGES = ["555","688","1920","2025","2002"]


X = 1
B = 7

X2 = 1 

ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']


def afinCrypt(message):
    messageSplit = [d for d in message]

    for idx in range(len(messageSplit)):
        char = messageSplit[idx]
        index = (X*ALPHABET.index(char)+B)%37
        newChar = ALPHABET[index]
        messageSplit[idx] = newChar
        
    return ''.join(messageSplit)

def afinDecrypt(messageCrypt):
    messageSplit = [d for d in messageCrypt]

    for idx in range(len(messageSplit)):
        char = messageSplit[idx]
        index = (X2*(ALPHABET.index(char)-B))%37
        newChar = ALPHABET[index]
        messageSplit[idx] = newChar
        
    return ''.join(messageSplit)

for message in MESSAGES:

    messageCrypt = afinCrypt(message)
    messageDecrypt = afinDecrypt(messageCrypt)

    print(f"Mensaje a antes de procesar: {message}")
    print(f"Mensaje cifrado: {messageCrypt}")
    print(f"Mensaje descifrado: {messageDecrypt}")



