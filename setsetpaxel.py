import requests, json
def login(username, password):
    url = "https://api.paxel.co/apg/api/v1/login"

    payload = "{\"username\":\"%s\",\"password\":\"%s\"}"%(username, password)
    headers = {
    'accept': 'application/json, text/plain, */*',
    'x-player': '9d035d57-b329-43eb-a4e6-fb184601c0fc',
    'Content-Type': 'application/json',
    'Host': 'api.paxel.co',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.12.1'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    jsonq = json.loads(response.text.encode('utf8'))
    return jsonq
def payment(token, nom, bank):
    url = "https://api.paxel.co/apg/api/v1/payment/midtrans/charge"

    payload = "{\"amount\":%s,\"bank_name\":\"%s\"}"%(nom, bank)
    headers = {
    'accept': 'application/json, text/plain, */*',
    'authorization': 'Bearer %s'%(token),
    'x-player': '9d035d57-b329-43eb-a4e6-fb184601c0fc',
    'Content-Type': 'application/json',
    'Host': 'api.paxel.co',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.12.1'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    jsonq = json.loads(response.text.encode('utf8'))
    return jsonq
data = input("Masukkan Data (Contoh 0812342:p44sWORD): ")
split = data.split(":")
masuk = login(split[0], split[1])
if masuk["code_message"] == "Login Success":
    token = masuk["data"]["api_token"]
    nominal = int(input("Masukkan Nominal: "))
    print("Pilih Bank Pembayaran:\n1. BNI\n2. Permata\n3. BCA\n4. Mandiri")
    bank = int(input("Masukkan Kode Bank: "))
    if bank == 1:
        kode = "bni"
    elif bank == 2:
        kode = "permata"
    elif bank == 3:
        kode = "bca"
    elif bank == 4:
        kode = "mandiri"
    bayar = payment(token, nominal, kode)
    #print(bayar)
    if bayar["code"] == 200:
        print("Silahkan Bayar ke Rekening %s %s Sejumlah %s "%(kode, bayar["data"]["va_number"], nominal))
    else:
        print(bayar)
else:
    print(masuk["code_message"])
