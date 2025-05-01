psr = ["홍길동","일지매"]

while True:
    a = int(input())
    if a == 0:
        break
    elif a == 1:
        print(f"현재 프로그래밍 수강 신청자는 {psr}입니다.")
        new_psr = input("추가할 학생 이름: ")
        print(f"{new_psr} 학생의 신청이 완료되었습니다.")
        psr.append(new_psr)
        print(f"현재 이 과목의 최종 신청자는 {psr}입니다.")
    elif a == 2:
        print(f"현재 이 과목의 최종 신청자는 {psr}입니다.")
        del_psr = input("철회할 학생 이름: ")
        psr.remove(del_psr)
        print(f"{del_psr} 학생의 수강 철회가 완료되었습니다.")
        print(f"현재 이 과목의 최종 신청자는 {psr}입니다.")
    elif a == 3:
        print(f"현재 이 과목의 최종 신청자는 {psr}입니다.")
        bef = input("변경 전 이름: ")
        aft = input("변경 후 이름: ")
        idx = psr.index(bef)
        psr[idx] = aft
        print(f"요청 하신대로 {bef}을(를) {aft}(으)로 변경하였습니다.")
        print(f"현재 이 과목의 최종 신청자는 {psr}입니다.")