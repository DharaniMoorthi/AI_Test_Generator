from openai import OpenAI
client = OpenAI(api_key="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

prompt = """

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

output=(response.choices[0].message.content)

print(output)

with open("test_cases.txt", "w", encoding="utf-8") as file:
    file.write(output)

    print("Test cases have been written to test_cases.txt")

    