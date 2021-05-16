"""
해쉬 구조
Hash Table: 키(Key)에 데이터(Value)를 저장하는 데이터 구조
Key를 통해 바로 데이터를 받아올 수 있으므로, 속도가 획기적으로 빨라짐
파이썬 딕셔너리(Dictionary) 타입이 해쉬 테이블의 예: Key를 가지고 바로 데이터(Value)를 꺼냄
보통 배열로 미리 Hash Table 사이즈만큼 생성 후에 사용 (공간과 탐색 시간을 맞바꾸는 기법)
단, 파이썬에서는 해쉬를 별도 구현할 이유가 없음 - 딕셔너리 타입을 사용하면 됨


해쉬(Hash): 임의 값을 고정 길이로 변환하는 것
해쉬 테이블(Hash Table): 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
해싱 함수(Hashing Function): Key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
해쉬 값(Hash Value) 또는 해쉬 주소(Hash Address): Key를 해싱 함수로 연산해서, 해쉬 값을 알아내고, 이를 기반으로 해쉬 테이블에서 해당 Key에 대한 데이터 위치를 일관성있게 찾을 수 있음
슬롯(Slot): 한 개의 데이터를 저장할 수 있는 공간
저장할 데이터에 대해 Key를 추출할 수 있는 별도 함수도 존재할 수 있음

"""

hash_table = list([0 for i in range(10)])
print(hash_table)

def hash_func(key):
    return key % 5

def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]


data1 = "Andy"
data2 = "Dave"
data3 = "Trump"
data4 = "Anthor"

storage_data('Andy', '01055553333')
storage_data('Dave', '01044443333')
storage_data('Trump', '01022223333')

print(get_data('Andy'))

"""
Chaining 기법 사용해보기
- 개방 해슁 또는 Open Hashing 기법 중 하나: 해쉬 테이블 저장공간 외의 공간을 활용하는 기법
- 충돌이 일어나면, 링크드 리스트라는 자료 구조를 사용해서, 링크드 리스트로 데이터를 추가로 뒤에 연결시켜서 저장하는 기법
"""
