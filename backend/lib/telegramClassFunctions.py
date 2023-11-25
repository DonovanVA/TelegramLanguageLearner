async def getMessages(df,me, users: [str], relationship: str,client):
   
    for user in users:
        async for message in client.iter_messages(user):

            # Classify the message.
            type = 'text'

            # Append the message to the DataFrame.
            df = df.append({'id': message.id,'user_id':me.id, 'sender_id': message.sender_id, 'receiver_id': message.peer_id.user_id, 'receiver_name': user, 'text': message.text,'relationship':relationship, 'type': type,'date':message.date}, ignore_index=True)

            print(message)


    return df


async def getProfile(json_file_path,client):
    # Getting information about yourself
    me = await client.get_me()
    user_info = {
    'id': me.id,
    'is_self': me.is_self,
    'contact': me.contact,
    'username': me.username,
    'mutual_contact': me.mutual_contact,
    'deleted': me.deleted,
    'bot': me.bot,
    'bot_chat_history': me.bot_chat_history,
    'bot_nochats': me.bot_nochats,
    'verified': me.verified,
    'restricted': me.restricted,
    'min': me.min,
    'bot_inline_geo': me.bot_inline_geo,
    'support': me.support,
    'scam': me.scam,
    'apply_min_photo':me.apply_min_photo,
    'fake': me.fake,
    'bot_attach_menu':me.bot_attach_menu,
    'premium':me.premium,
    'attach_menu_enabled':me.attach_menu_enabled,
    'bot_can_edit':me.bot_can_edit,
    'close_friend':me.close_friend,
    'stories_hidden':me.stories_hidden,
    'stories_unavailable': me.stories_unavailable,
    'access_hash': me.access_hash,
    'first_name': me.first_name,
    'last_name':me.last_name,
    'username': me.username,
    'phone':me.phone,
    # Add other fields you want to save here
}