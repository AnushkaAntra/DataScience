def isPerfectSquare(n):
    for i in range(1, n+1):
        if(i*i == n):
            return True
    return False

def sumOfDigits(n):
    sum = 0
    while(n != 0):
        digit = n%10
        sum += digit
        n //= 10
    return sum


def main():
    r = int(input("enter the range: "))
    for i in range(1, r+1):
        if(isPerfectSquare(i) and sumOfDigits(i) < 10):
            print(i, end = " ")
                
main()