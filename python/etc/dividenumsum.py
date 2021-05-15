def main():
    n = 12
    cnt = 0
    for i in range(1,n+1):
        if (n % i) == 0:
            cnt+=i
    print(cnt)


if __name__ == "__main__":
    main()
