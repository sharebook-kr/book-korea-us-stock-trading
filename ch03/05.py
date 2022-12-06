import mojito
import pprint

f = open("../koreainvestment.key")
lines = f.readlines()
key = lines[0].strip()
secret = lines[1].strip()
acc_no = lines[2].strip()
f.close()

broker = mojito.KoreaInvestment(
    api_key=key,
    api_secret=secret,
    acc_no=acc_no
)

resp = broker.fetch_price("005930")
print("Open : ", resp['output']['stck_oprc'])
print("High : ", resp['output']['stck_hgpr'])
print("Low  : ", resp['output']['stck_lwpr'])
print("Close: ", resp['output']['stck_prpr'])