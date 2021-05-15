def extractMarkedText(target_text, compare_text):
    #: 입력된 두개의 인자를 가지고 테이블을 만들기
    width = len(target_text) + 1
    height = len(compare_text) + 1
    # 테이블 초기화 빈값으로 초기화시키기
    table = [''] * width * height

# 테이블 값 불러오기
    def getTable(r, c):
        return table[r * width + c]

#테이블 값 지정하기
    def setTable(r, c, value):
        table[r * width + c] = value

#테이블에 값 넣기
    for i in range(1, height):
        for j in range(1, width):
            #비교값과 같으면
            if target_text[j - 1] == compare_text[i - 1]:
                #대각성 방향의 값에 동일 값 세팅
                #
                value = getTable(i - 1, j - 1) + target_text[j - 1]
                setTable(i, j, value)
                continue
            #
            searched_span_lcs = getTable(i - 1, j)
            text_lcs = getTable(i, j - 1)

            if len(searched_span_lcs) > len(text_lcs):
                setTable(i, j, searched_span_lcs)
            else:
                setTable(i, j, text_lcs)

    return getTable(height - 1, width - 1)

S1 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
S2 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA" 
S3 = "GTCGTCGGAAGCCGGCCGAA"
a = extractMarkedText(S1, S2) 
print("output: ",a)

