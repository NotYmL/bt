import time, requests

name = "Bot_name"
token = "User_token"

listofgoodtags = ["9999", "6969", "1000", "0100", "0010", "1337", "1338", "2222", "1010", "1101", "0420", "0069", "6900", "1200", "6969", "0666", "6666", "0333", "3333", "1234", "0001", "1011", "1001", "0202", "0101", "8008", "0808", "0888", "0777", "2992", "9973", "3000", "2000", "1212", "9898", "6060", "6660", "7331",  "1111"]

headers = {
    "accept": "*/*",
    "authorization": token,
    "content-type": "application/json",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1"
}

while 1:
    res1 = requests.post("https://discord.com/api/v9/applications", headers=headers, json={"name":name}) #Make new app
    time.sleep(1)
    
    if(429 == res1.status_code):
        time.sleep(res1.json()['retry_after']+0.5)
        continue

    app = res1.json()["id"]

    res2 = requests.post(f"https://discord.com/api/v9/applications/{app}/bot", headers=headers)         #make new app a BOT

    while(429 == res2.status_code):
        time.sleep(res2.json()['retry_after']+0.5)
        res2 = requests.post(f"https://discord.com/api/v9/applications/{app}/bot", headers=headers)
    
    time.sleep(1)
    
    res3 = requests.get("https://discord.com/api/v9/applications/"+app, headers=headers)                #GET APP INFO
    time.sleep(1)
    
    if(429 == res3.status_code):
        time.sleep(res3.json()['retry_after']+0.5)
        continue

    if str(res3.json()['bot']['discriminator']) in listofgoodtags:                                      #IF TAG NOT SHIT
        break

    res4 = requests.post(f"https://discord.com/api/v9/applications/{app}/delete", headers=headers)      #if tag shit del app and bot
    time.sleep(1)
    
    if(429 == res4.status_code):
        time.sleep(res4.json()['retry_after']+0.5)
        res4 = requests.post(f"https://discord.com/api/v9/applications/{app}/delete", headers=headers)
        continue
    
    time.sleep(30)
