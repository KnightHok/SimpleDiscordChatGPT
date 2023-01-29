import openai
async def chatgpt():
    return openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_dinosaur(),
        temperature=0.6,
        max_tokens=100,
    )
def generate_dinosaur():
    return """give me a type of fruit and where it originates from with a small passage about its history"""