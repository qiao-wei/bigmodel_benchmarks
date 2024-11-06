def completions(url):
    # 调用openai的completions接口获取
    import openai
    openai.api_key = 'your-api-key'
    response = openai.Completion.create(
         engine="text-davinci-003",
         prompt=url,
         max_tokens=150
    )
    return response.choices[0].text.strip()

def chat(url):
    # 调用openai的chat接口获取
    import openai
    openai.api_key = 'your-api-key'
    response = openai.ChatCompletion.create(
           model="gpt-3.5-turbo",
           messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": url}
                 ]
    ) 
    return response.choices[0].message.content.strip()
