perm = [4,2,1,3]
perminv = [3,2,4,1]

sust = 1
rounds = 10
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def luciferCrypt(message):
    messageSplit = [message[i:i+8] for i in range(0, len(message), 8)]
    if len(messageSplit[-1]) < 8:
        messageSplit[-1] = f"{messageSplit[-1]:{'X'}<8}"
    print(f"Mensaje con completado con X {''.join(messageSplit)}")
    
    for idx in range(len(messageSplit)):
        element = messageSplit[idx]

        half_a = element[:len(element)//2]
        half_b = element[len(element)//2:]

        for i in range(0,rounds):
            
            tmp = ""

            # Sustitución
            for char in half_a:
                index = ALPHABET.index(char) + sust 
                newchar = ALPHABET[index%len(ALPHABET)]
                tmp = tmp + newchar
            half_a = tmp

            # Permutación
            tmp = ""
            for j in perm:
                tmp = tmp + half_a[j-1]
            half_a = tmp
    
            # Swap
            tmp = half_a
            half_a = half_b
            half_b = tmp
        
        element = half_a + half_b
        messageSplit[idx] = element

    return ''.join(messageSplit) 

def luciferiDecrypt(encryptMessage):

    messageSplit = [encryptmessage[i:i+8] for i in range(0, len(encryptmessage), 8)]
    
    for idx in range(len(messageSplit)):
        element = messageSplit[idx]
        half_a = element[:len(element)//2]
        half_b = element[len(element)//2:]

        for i in range(0,rounds):
            
            tmp = ""
            
            # Swap
            tmp = half_a
            half_a = half_b
            half_b = tmp

            # Permutación
            tmp = ""
            for j in perminv:
                tmp = tmp + half_a[j-1]
            half_a = tmp
            
            # Sustitución
            tmp = ""
            for char in half_a:
                index = ALPHABET.index(char) - sust 
                newchar = ALPHABET[index%len(ALPHABET)]
                tmp = tmp + newchar
            half_a = tmp
           
        element = half_a + half_b
        messageSplit[idx] = element

    return ''.join(messageSplit) 

message = input("Ingrese una cadena: ")
print(f"Mensaje antes de ser procesado: {message}")

encryptmessage = luciferCrypt(message)
decryptmessage = luciferiDecrypt(encryptmessage)

print(f"Mensaje encriptado: {encryptmessage}")
print(f"Mensaje desencriptado: {decryptmessage}")

