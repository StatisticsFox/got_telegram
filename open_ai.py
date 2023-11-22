from openai import OpenAI
import telegram
import schedule
import time
import datetime
import pytz

token = "6801716374:AAHf9y6oCdGKPLRvXG3vHvNNgVSIoZxhPWA"
public_chat_name = '@OS_kgu'

client = OpenAI(
    api_key = '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'
    )

def chatGPT(input_string):
    # completion = client.chat.completions.create(
    #     model="gpt-3.5-turbo-1106",
    #     messages=[
    #         {"role": "system", "content": "안녕하세요 척척박사 입니다. 무엇을 도와드릴까요?"},
    #         {"role": "user", "content": f"{input_string}. json"}
    #     ],
    #     response_format={"type": "json_object"}
    # )
    # bot = telegram.Bot(token=token)
    # bot.sendMessage(chat_id=public_chat_name, text= completion.choices[0].message.content)

    error = "결제를 하지 않았습니다ㅠㅠㅠ"
    return error

chatGPT('안녕')