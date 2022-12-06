import mojito

key = "발급받은 API KEY"
secret = "발급받은 API SECRET"
acc_no = "12345678-01"

broker = mojito.KoreaInvestment(
    api_key=key,
    api_secret=secret,
    acc_no=acc_no
)
print(broker)