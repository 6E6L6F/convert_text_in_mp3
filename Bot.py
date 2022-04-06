##############################
#       @e_l_f_6_6_6         #
#    @elf_security_cyber     #
##############################

import gtts
from pyrogram import *
import random
app = Client(
    session_name='Elf_Bot',
    api_hash='',
    api_id='',
    bot_token='',
)
def Voice(text , lang , n ):
    try:
        tts = gtts.gTTS(text, lang=lang)
        tts.save(str(n)+"_File.mp3")
    except:
       print('Error')

@app.on_message()
async def Bot(Client  , message):
        Text =  message.text

        if Text == '/start':
            await app.send_message(message.chat.id , f'Welcome Mr.{message.from_user.first_name} To Bot Convert Text In Mp3')

        if Text == '/lang':
            await app.send_chat_action(message.chat.id, "typing")
            await app.send_message(message.chat.id ,"af : Afrikaans\nsq : Albanian\nar : Arabic\nhy : Armenian\nne : Nepali\nno : Norwegian\nbn : Bengali\npl : Polish\nbs : Bosnian\npt : Portuguese\nca : Catalan\nro : Romanian\nhr : Croatian\nru : Russian\ncs : Czech\nsr: Serbian\nen : English\nes : Spanish,...." )

        if Text.split(':')[0] == '/Voice':
            n = random.randint(0, 6666)
            Voice(Text.split(':')[1] , Text.split(':')[2] , n )
            await app.send_message(message.chat.id, 'Loading..!')
            for i in range(2):
                    for u in ['/', '|', '\\']:
                       await app.send_chat_action(message.chat.id, "typing")
                       await app.edit_message_text(message.chat.id, message.message_id + 1, f'Loading..{u}')
            try:
                await app.send_audio(message.chat.id , str(n)+'_File.mp3',title='Music' )
            except:
                await app.send_message(message.chat.id , 'Error Please Try Later..!')

        if Text == '/Creator':
            await app.send_message(message.chat.id,'Bot Created By >>> @e_l_f_6_6_6 \nMy Channel Telegram >>> @elf_security_cyber')

        if Text == '/help':
            await app.send_message(message.chat.id , '/Voice:[Text]:[lang]\n/Voice:Hello:en')
app.run()
