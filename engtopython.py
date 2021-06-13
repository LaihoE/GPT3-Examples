import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
question = input("Question: ")
response = openai.Completion.create(
  engine="davinci",
  prompt=f"Translates English to Python code.\nEng: print hello AI\nPython: print('hello AI')\n###\nEng: create a list \"biglist\" with values 1,2,3\nPython: biglist = [1,2,3]\n###\nEng: create a function \"examplefunction\" that takes inputs \"ID\" and \"age\"\nPython: def examplefunction(ID,age):\n###\nEng: read csv file \"data.csv\" with pandas and assign it to variable df\nPython: df = pd.read_csv(\"data.csv\")\n###\nEng:{question}\nPython:",
  temperature=0,
  max_tokens=30,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["###"]
)
print(response["choices"][0]["text"][1:])