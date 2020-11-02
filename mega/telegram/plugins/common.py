from pyrogram import filters, emoji
from pyrogram.types import Message
from mega.telegram import MegaDLBot
from mega.database.files import MegaFiles


@MegaDLBot.on_message(filters.command("start", prefixes=["/"]))
async def start_message_handler(c: MegaDLBot, m: Message):
    if len(m.command) > 1:
        if m.command[1].split("-")[0] == 'plf':
            file_id = m.command[1].split("-", 1)[1]
            file_details = await MegaFiles().get_file_by_file_id(file_id)

            if file_details is not None:
                file_message = await c.get_messages(
                    chat_id=file_details['chat_id'],
                    message_ids=file_details['msg_id']
                )

                if str(file_details['file_type'].split("/"))[0].lower() == "video":
                    await m.reply_video(
                        video=file_message.video.file_id,
                        file_ref=file_message.video.file_ref
                    )
                else:
                    await m.reply_document(
                        document=file_message.document.file_id,
                        file_ref=file_message.document.file_ref
                    )
    else:
        await m.reply_text(
            text=f"<b>Hello, My Name Is 𝗠𝗘𝗚𝗔𝗧𝗥𝗢𝗡 (^。^)</b>\n\n<b>I'm A <u>𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗨𝗥𝗟</u> To <u>𝗙𝗜𝗟𝗘</u> Uploading Bot\n\n<b>Send Me Any 𝗗𝗜𝗥𝗘𝗖𝗧 𝗟𝗜𝗡𝗞, Wait For Me To Respond With <u>𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗</u> Or <u>𝗥𝗘𝗡𝗔𝗠𝗘</u> Before Proceeding To Starting Your Download</b></b>\n\n<b>❌ <u>𝗣𝗢𝗥𝗡𝗢𝗚𝗥𝗔𝗣𝗛𝗜𝗖 𝗖𝗢𝗡𝗧𝗘𝗡𝗧𝗦</u> Are Strictly Prohibited & Will Get You Banned Permanently.</b>"
        )
