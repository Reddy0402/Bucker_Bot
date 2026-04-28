import os


new = os.getenv("groq_api_key")

ModelName = "llama3-8b-8192"

print(ModelName)


Messages=[
    {"role":"student", "content":"what do you need"}
]


response = model(
    ModelName,
    Messages
)

print(Messages)