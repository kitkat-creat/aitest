import openai
import gradio



def askGPT(text):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.6,
        max_tokens = 150,
    )
    ChatGPT_reply = response.choices[0].text
    return ChatGPT_reply



demo = gradio.Interface(fn=askGPT, inputs = "text", outputs = "text", title = "Medical Notes Classifer")

demo.launch(share=True)