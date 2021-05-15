# 최대공약수
def method(a,b):
    if a>b :
        tmp = a
        a = b
        b = a
    while b>0:
        c = b
        b = a%b
        a = c
    return a

#최소공배수
def dcv(a,b):
    return a*b // method(a,b)

def main():
    answer = method(6,9)
    print(answer)
if __name__ == "__main__":
    main()