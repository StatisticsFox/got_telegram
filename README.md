# got_telegram
## 텔레그램 봇 + ChatGPT 연동 

### 학번: 201911358
### 이름: 최지혁

코드를 보시면 입력값으로 문자열을 받고 그 문자열을 gpt에 전달하는 식으로 코드를 짰습니다. <br>

저는 결재를 하지 않았기애 과제 요구사항에 맞게 주요코드들을 주석처리하고 return 값으로 아무 문자열이나 출력 하였지만, <br> 
만약 결재를 했다면 아래처럼 코드가 나왔을 겁니다. 
```
def chatGPT(input_string):
     completion = client.chat.completions.create(
         model="gpt-3.5-turbo-1106",
         messages=[
             {"role": "system", "content": "안녕하세요 척척박사 입니다. 무엇을 도와드릴까요?"},
             {"role": "user", "content": f"{input_string}. json"}
         ],
         response_format={"type": "json_object"}
     )
     bot = telegram.Bot(token=token)
     bot.sendMessage(chat_id=public_chat_name, text= completion.choices[0].message.content)

chatGPT('겨울에 관련된 시를 써줘')
```
