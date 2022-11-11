# 계정정보 불러오기
import mojito

# 게정정보 파일 읽기
with open("../koreainvestment.key") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()
    acc_no = lines[2].strip()

print(key)
print(secret)
print(acc_no)
