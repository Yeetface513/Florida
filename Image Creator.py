import os
# you need to download the openai library first using python -m pip install openai 
import openai

PROMPT = input("enter a prompt you want the ai to generate here \n")

openai.api_key = ("enter your api key here") # get your api key from the open ai website

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
)

print(response["data"][0]["url"]) # go to the url to get your image!
