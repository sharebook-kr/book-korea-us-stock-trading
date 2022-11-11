# 증권사 객체 생성
import mojito

# 게정정보 파일 읽기
with open("../koreainvestment.key") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()
    acc_no = lines[2].strip()

broker = mojito.KoreaInvestment(
    api_key=key,
    api_secret=secret,
    acc_no=acc_no
)
print(broker)