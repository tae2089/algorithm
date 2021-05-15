
#n = 탑의 번호 , from_pos = 현 위치 to_pos = 가고 싶은 위치, aux_pos = 거쳐지나가는 위치
def hanoi(n,from_pos,to_pos,aux_pos):
    if n == 1:
        print(from_pos,"->",to_pos)
        return 
    
    hanoi(n-1,from_pos,aux_pos,to_pos)
    print(from_pos,"->",to_pos)
    hanoi(n-1,aux_pos,to_pos,from_pos)

def main():
    hanoi(4,1,3,2)

if __name__ == '__main__':
    main()
    