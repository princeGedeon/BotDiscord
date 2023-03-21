import os
import openai


#Mettre votre token
openai.api_key="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"

def generate_prompt(prompt):
    """
    Text to prompt
    :param prompt:
    :return:
    """
    context=f"Ce qui suit est une conversation avec un assistant IA. L'assistant est serviable, créatif, intelligent et très sympathique.\n\nHuman: Bonjour, qui êtes-vous?\nAI: Je suis une IA adapté en Bot par Prince Gédéon. Comment puis-je vous aider aujourd'hui?"
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"{context}\nHuman: {prompt}.\nAI:",
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.6,
      stop=[" Human:", " AI:"]
    )
    #print(response)
    return response['choices'][0]["text"]

