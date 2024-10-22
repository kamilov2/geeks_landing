import requests
import hashlib
import time

username = "moydinovam"
secret_key = "71c9539d0c3b44dcf1144fc76ea43861"
service_id = 1
phone_number = "998902113123"
message_text = "testoviy zor oxshadi oson ekan"
sms_id = 101

utime = int(time.time())
token_str = f"TransmitSMS {username} {secret_key} {utime}"
token = hashlib.md5(token_str.encode('utf-8')).hexdigest()

headers = {
    "X-Access-Token": token,
    "Content-Type": "application/json"
}

data = {
    "utime": utime,
    "username": username,
    "service": {
        "service": service_id
    },
    "message": {
        "smsid": sms_id,
        "phone": phone_number,
        "text": message_text
    }
}

url = "https://routee.sayqal.uz/sms/TransmitSMS"
while True:
    response = requests.post(url, json=data, headers=headers)

    print(f"Статус-код: {response.status_code}")
    print(f"Ответ: {response.json()}")
