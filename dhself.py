n=int(input("Enter first prime number:"))
g=int(input("Enter second prime number:"))
x=int(input("Alice private key::"))
y=int(input("Bob private key::"))

A=pow(g,x)%n
B=pow(g,y)%n
print(f'Alice sends key {A} to Bob.')
print(f'Bob sends key {B} to alice.')
k1=pow(B,x)%n
k2=pow(A,y)%n

print(k1)
print(k2)
