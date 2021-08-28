from telethon import TelegramClient


api_id = 00000 # api_id here
api_hash = 'HASH HERE'
target_group = "" # Target group id


client = TelegramClient('User parser', api_id, api_hash)
client.start()

with open("tele_ids.txt", "a") as file_:
   for user in client.iter_participants(target_group):
       if user.username == None:
           pass
       else:
           print(user.username)
           file_.write(user.username + "\n")
client.disconnect()