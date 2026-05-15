from openai import OpenAI
client = OpenAI(api_key="")
prompt= """

Generate test cases for a login page with:
- username
- password
- login button

Include:
- positive test cases
- negative test cases
"""


response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    
    {"role": "user", "content": "prompt"}

  ]
)

print(response.choices[0].message.content)

