from openai import OpenAI
client = OpenAI(
    api_key = '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'
    )

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {"role": "system", "content": "You are a poetic assistant."},
    {"role": "user", "content": "겨울에 대한 시를 써줘. json"}
  ],
  response_format={"type": "json_object"}
)

print(completion.choices[0].message.content)
