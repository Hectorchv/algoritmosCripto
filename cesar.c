#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<locale.h>
#include<wchar.h>

#define SIZE_OF_ALPHABET 27
#define K 3
#define MAX_LENGTH 1024

const char *alphabet = "ABCDEFGHIJKLMN\xD1OPQRSTUVWXYZ";

int getIndex(char letter)
{
    int index;

    if (letter == -61)
        index = 14;
    else
    {
        for (index = 0; index < SIZE_OF_ALPHABET; index++)
        {
            if(letter == alphabet[index])
                break;
        }
    }
    return index;
    
}

char *encrypt(char *message)
{
    char *encryptMessage = malloc(sizeof(char) * MAX_LENGTH);
    char letter;
    for (int i = 0; i < strlen(message) - 1; i++)
    {
        letter = alphabet[((getIndex(message[i]) + K)%(SIZE_OF_ALPHABET-1))];
        if (letter == -47)
        {
            strcat(encryptMessage, "Ñ");
            i++;
        }
        else
            encryptMessage[i] = letter;
    }
    
    printf("\n");
    return encryptMessage;
}

char *decrypt(char *encryptMessage)
{
    char *decryptMessage = malloc(sizeof(char) * MAX_LENGTH);
    char letter, letter2;
    int a = 0;
    for (int i = 0; i < strlen(encryptMessage) - 1; i++)
    {
        letter2 = encryptMessage[i+a];
        letter = alphabet[((getIndex(letter2) - K)%(SIZE_OF_ALPHABET-1))];
        if (letter == -47) //Si la letra es Ñ
        {
            strcat(decryptMessage, "Ñ");
            i++;
        }
        if (letter == 'L')
        {
            a++;
        }
        else
            decryptMessage[i] = letter;

    }
    
    printf("\n");
    return decryptMessage;
}

int main(int argc, char **argv)
{
    setlocale(LC_CTYPE, "en_US.UTF-8");

    //char alphabet2[] = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ";

    char message[MAX_LENGTH];
    char encryptMessage[MAX_LENGTH];
    char decryptMessage[MAX_LENGTH];
    

    printf("Ingrese el mensaje a cifrar: ");
    fgets(message, sizeof(message), stdin);

    strcpy(encryptMessage, encrypt(message));
    printf("Mensaje encriptado: %s\n", encryptMessage);

    strcpy(decryptMessage, decrypt(encryptMessage));
    printf("Mensaje desencriptado: %s", decryptMessage);

    return 0;
}