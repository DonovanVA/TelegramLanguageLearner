import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import pandas as pd
from dotenv import load_dotenv
from telethon import TelegramClient
from lib.paths import get_prev_path
from lib.pandas_database_functions import createReplaceCSV
import asyncio
async def getMessages(df, me, users: [str], relationship: str,client):
    for user in users:
        async for message in client.iter_messages(user):
            # Append the message to the DataFrame.
            df = df.append({'id': message.id,'user_id':me.id, 'sender_id': message.sender_id, 'receiver_id': message.peer_id.user_id, 'receiver_name': user, 'text': message.text,'relationship':relationship, 'type': type,'date':message.date}, ignore_index=True)
    return df

async def main():
    datasets_folder = 'datasets'
    raw_messages_file_path = os.path.join(get_prev_path(__file__), datasets_folder, 'raw_messages.csv')
    load_dotenv()
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')
    username = os.getenv('USERNAME')

    if f"{username}.session" in os.listdir():
        os.remove(f"{username}.session")
    
    client = TelegramClient(username, api_id, api_hash)
    await client.start()
    client.connect()

    arrayOfFriends = [] ## <- pass in ur telehandle array of friends here eg: ['FriendA','FriendB',...], array cannot be empty
    df = pd.DataFrame(columns=['id', 'user_id', 'sender_id', 'receiver_id', 'receiver_name', 'text', 'relationship', 'type', 'date'])

    me = await client.get_me()
    df = await getMessages(df, me, arrayOfFriends, 'FRIEND',client)
    createReplaceCSV(df,raw_messages_file_path)
    # Further operations with the retrieved messages or dataframe
    
# Run the event loop to execute the async code
asyncio.run(main())
