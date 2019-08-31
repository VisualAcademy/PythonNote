#[?] 컬렉션 형태의 데이터를 특정 키 값으로 그룹화 

# 그룹 알고리즘(Group Algorithm): 특정 키 값에 해당하는 그룹화된 합계 리스트 만들기

# 테스트용 레코드 클래스
class Record():
    def __init__(self, name, quantity):
        self.name = name # 상품명
        self.quantity = quantity # 수량 

def main():
    #[1] Input
    records = [ Record("RADIO", 3), Record("TV", 1), Record("RADIO", 2), Record("DVD", 4) ] # 입력 데이터
    groups = [] # 출력 데이터 
    N = len(records) # 의사코드

    #[2] Process: GROUP 알고리즘(SORT -> SUM -> GROUP)
    #[A] 그룹 정렬: SORT - Selection Sort 
    for i in range(N - 1):
        for j in range(i + 1, N):
            if (records[i].name > records[j].name):
                temp = records[i]
                records[i] = records[j]
                records[j] = temp # SWAP

    #[B] 그룹 소계: GROUP
    subtotal = 0 # 소계
    for i in range(N):
        subtotal = subtotal + records[i].quantity # 같은 상품명의 수량을 누적(SUM) 
        #[!] 다음 레코드가 없거나, 현재 레코드와 다음 레코드가 다르면 저장 
        if ((i + 1) == N or records[i].name != records[i + 1].name):
            # (한 그룹의 키(Key) 지정, 소계)
            groups.append(Record(records[i].name, subtotal)) # 하나의 그룹 저장
            subtotal = 0 # 하나의 그룹이 완료되면 소계 초기화

    #[3] Output
    print("[1] 정렬된 원본 데이터:")
    for r in records:
        print(f"{r.name.rjust(6)} - {r.quantity}")

    print("[2] 이름으로 그룹화된 데이터:")
    for g in groups:
        print(f"{g.name.rjust(6)} - {g.quantity}")

if __name__ == "__main__":
    main()
