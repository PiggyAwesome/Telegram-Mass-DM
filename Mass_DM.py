from telethon import TelegramClient, events

api_id = 00000 # api_id here
api_hash = 'HASH HERE'
message = ""

file_ = open("tele_ids.txt", "r")
ids = file_.read()
ids = ids.splitlines()


try:


 with TelegramClient('MassDM', api_id, api_hash) as client:
     for line in ids:
        response = client.send_message(line, message)
        print(response)
     client.disconnect()

except Exception as err:
    print(err)