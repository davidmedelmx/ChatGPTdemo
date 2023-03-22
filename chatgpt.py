import os
import openai
openai.organization = "org-"
openai.api_key = "sk-"

while True:
    prompt = input("\nCuál es tu pregunta?: ")
    if prompt == "exit":
        break
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=2048,
    )
    print(response.choices[0].text)