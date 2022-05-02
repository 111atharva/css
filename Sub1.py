# caesar
import re


def caesar(string, shift):
    caesar = ''
    for char in string:
        if char == ' ':
            caesar = caesar + char
        elif char.isupper():
            caesar = caesar + chr(((ord(char) - 65) + shift) % 26 + 65)
        elif char.islower():
            caesar = caesar + chr(((ord(char) - 97) + shift) % 26 + 97)
        else:
            caesar = caesar + char
    return caesar


text = input("Enter String : ")
shift = int(input("Enter shift number : "))
print("Caesar Cipher : ", caesar(text, shift))

# multiplicative


def multInverse(num):
    i = 1
    while True:
        temp = ((i*26)+1)/num
        if temp == int(temp):
            return int(temp)
        i += 1


def multEncrypt(msg, key):
    msg = msg.upper()
    msg = re.sub(r'[^A-Z]', '', msg)
    cText = ''
    cList = []
    for letter in msg:
        asciVal = ord(letter)
        cText += chr((((asciVal-65)*key) % 26)+65)
    return cText


def multDecrypt(cText, key):
    cText = cText.upper()
    cText = re.sub(r'[^A-Z]', '', cText)
    dText = ''
    inverseKey = multInverse(key)
    for letter in cText:
        asciVal = ord(letter)-65
        dText += chr((((asciVal)*inverseKey) % 26)+65)
    return dText


print('Key Domain: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25')
key = int(input('Enter One The following Keys: '))
msg = input('\nEnter Message to be encrptyed: ')
cText = multEncrypt(msg, key)
print(f'\ncipher text = {cText}')
dText = multDecrypt(cText, key)
print(f'\nDeciphered text = {dText}')

# affine


def multInverse(num):
    i = 1
    while True:
        temp = ((i*26)+1)/num
    if temp == int(temp):
        return int(temp)
    i += 1


def multEncrypt(msg, key, keyAdd):
    msg = msg.upper()
    msg = re.sub(r'[^A-Z]', '', msg)
    print(msg)
    cText = ''
    cList = []
    for letter in msg:
        asciVal = ord(letter)
        cText += chr(((((asciVal-65)*key)+keyAdd) % 26)+65)
    return cText


def multDecrypt(cText, key, keyAdd):
    cText = cText.upper()
    cText = re.sub(r'[^A-Z]', '', cText)
    dText = ''
    inverseKey = multInverse(key)
    for letter in cText:
        # asciVal=((ord(letter)-65)-keyAdd)%26
        # dText+=chr((((asciVal)*inverseKey)%26)+65)
        dText += chr(((((ord(letter)-65)-keyAdd)*inverseKey) % 26)+65)
    return dText


print('Key Domain: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25')
key = int(input('Enter One The following Keys: '))
keyAdd = int(input('Enter another Numeric Key for addition: '))
msg = input('\nEnter Message to be encrptyed: ')
cText = multEncrypt(msg, key, keyAdd)
print(f'\ncipher text = {cText}')
dText = multDecrypt(cText, key, keyAdd)
print(f'\nDeciphered text = {dText}')

# vignere


def vignereEncrypt(msg, key):
    index = 0
    cText = ''
    for letter in msg:
        num = ord(letter)-65
        newno = (num+(ord(key[index % len(key)])-65)) % 26
        cText += chr(newno+65)
        index += 1
    print(cText)
    return cText


def vignereDecrypt(cText, key):
    index = 0
    dText = ''
    for letter in cText:
        num = ord(letter)-65
        newno = (num-(ord(key[index % len(key)])-65)) % 26
        dText += chr(newno+65)
        index += 1
    print(dText)
    return dText


msg = "hello world"
key = "jash"
msg = re.sub(r'[^A-Z]', '', msg.upper())
key = re.sub(r'[^A-Z]', '', key.upper())
print(msg)
print(key)
cText = vignereEncrypt(msg, key)
vignereDecrypt(cText, key)
