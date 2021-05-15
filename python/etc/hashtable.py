class CloseHash:
    # hash table 생성하기
    def __init__(self,table_size):
        self.size = table_size
        self.hash_table = [0 for a in range(self.size)]
    
    # 키값 구하기
    def getKey(self,data):
        self.key = ord(data[0])
        return self.key
    
    #키를 해시로 변환
    def hashFunction(self, key):
        return key % self.size

    #  hash table 주소 생성하기
    def getAddress(self, key):
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address

    #테이블에 저장하기
    def save(self, key, value):
        #주소 생성하기
        hash_address = self.getAddress(key)
        # 값 저장하기
        self.hash_table[hash_address] = value
    
    #테이블에서 데이터 불러오기
    def read(self, key):
        hash_address = self.getAddress(key)
        return self.hash_table[hash_address]

    #값 삭제하기
    def delete(self, key):
        #해시 테이블 주소 받기
        hash_address = self.getAddress(key)
        if self.hash_table[hash_address] != 0:
            self.hash_table[hash_address] = 0
            return True
        else:
            return False
