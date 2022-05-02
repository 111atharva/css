import math

def stringifylist(arr):
    stng=""
    for i in arr:
        stng+=str(i)
    return stng

def transencrypt(msg):
    t1=[]
    t2=[]
    flag=True
    for val in msg:
        if flag:
            t1.append(val)
            flag=False
        else:
            t2.append(val)
            flag=True
    return stringifylist(t1)+stringifylist(t2)

def transdecrypt(msg):
    d_text=''
    half_len=math.ceil(len(msg)/2)
    half_len1=msg[0:half_len]
    half_len2 = msg[half_len:len(msg)]
    vari=0
    for letter in half_len2:
        d_text+=half_len1[vari]+letter
        vari+=1
    if len(half_len1)>len(half_len2):
        d_text+=half_len1[vari]
    return d_text

msg=str(input("Enter string here(alphabets only):"))
encrypted_text=transencrypt(msg)
print(f'Encrypted text:{encrypted_text}')
decrypted_text=transdecrypt(encrypted_text)
print(f'Decrypted text:{decrypted_text}')