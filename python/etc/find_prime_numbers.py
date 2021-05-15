
def isPrime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
        return True

def main():
    n = 10
    answer = []
    for i in range(1,n+1):
        if(isPrime(i)):
            answer.append(i)
    print(answer)

if __name__ == "__main__":
    main()

