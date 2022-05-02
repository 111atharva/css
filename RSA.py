#2 prime numbers seleteced
#n =P*Q

#e not factor of n
# #1<e<theta(n)

#e&n are public

#theta(n)=(P-1)*(Q-1)
#d is private key
#d=(k*theta(n)+1)/e
#k is some integer
# encrypted data = (data^e)mod(n)
# decrptyed text = (enrypted text^d)mod(n)
# 2 prime numbers
print("Print Prime Number P")
P=int(input())
print("Print Prime Number Q")
Q=int(input())
n=P*Q
T=(P-1)*(Q-1)
def gcd(a,b):
    while 1==1:
        temp=a%b
        if temp==0:
            return b
        a=b
        b=temp
e=2

while(e<T):
    if gcd(e,T)==1:
        break
    else:
        e+=1
print(f"\npublic key=({e},{n})")

#msgsize=len(str(n))
#print(f'\n\nEnter Your message(smaller Than: {msgsize} Digits) (Numberic value only: I.E H=7; I=8 hence HI = 78)')

#Encrypt HI i.e H=7, i=8
print("ENTER TEXT: ")
msg = int(input())
print(f"Msg Text={msg}")
c=pow(msg,e)%n
print(f"Encrypted Text={c}\n")
def findd(T,e):
    k=0
    while(1==1):
        d=(1+(k*T))/e
        print(f"k={k} d={d}")
        if int(d)== d :
            print(f"\nK is equal to:{k}\n")
            return d

        k+=1
d=findd(T,e)
print(f"\n\nprivate key=({d},{n})")
d_msg=pow(c,int(d))%n
print(f"Decrypted Text={d_msg}")

