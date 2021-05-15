#https: // www.acmicpc.net/problem/16909

def main(num, card_ability):
    result = 0
    re = []
    for j in range(len(card_ability)):
        for k in range(len(card_ability)):
            if j <= k:
                card = card_ability[j:k+1]
                # 리스트를 하나 생성
                # 요소 하나며는 result 0
                if len(card) <= 1:
                    result = 0
                else:
                    a = max(card)
                    b = min(card)
                    result = a-b
                re.append(result)
    print(sum(re))


if __name__ == "__main__":
    main(3, [2, 5, 3])
