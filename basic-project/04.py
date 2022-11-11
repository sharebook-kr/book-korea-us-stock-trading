# 현재가 조회
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

balance = broker.fetch_balance()
deposit = int(balance['output2'][0]['dnca_tot_amt'])
print(deposit)

SYMBOL = "005930"
price = broker.fetch_price(symbol=SYMBOL)
curr_price = price['output']['stck_prpr']
print(curr_price)

