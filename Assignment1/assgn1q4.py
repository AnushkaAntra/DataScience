import random
import string

def generate_passwor(n):
    str1 = string.ascii_uppercase + string.ascii_lowercase + string.digits
    res = ""
    for i in range(0, n+1):
        idx = random.choice(str1)
        res += idx
     
    return res

def main():
    n = int(input("enter the length of the passwords: "))
    m = int(input("enter the no of passwords: "))
    
    for i in range(1, m+1):
        print(f"password {i}: {generate_passwor(n)}")
        
main()
    