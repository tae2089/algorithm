
def solution(n):
    p = n.lower()
    cnt_p = p.count('p')
    cnt_y = p.count('y')
    return cnt_p == cnt_y

def main():
    s = "Pyy"
    print(solution(s))
if __name__ == "__main__":
    main()
