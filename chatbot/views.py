from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
from django.conf import settings




# Configure the OpenAI API client
client = OpenAI(api_key=settings.API_KEY)


def ask_openai(message):
    response = client.chat.completions.create(model = "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an helpful assistant."},
        {"role": "user", "content": message},
    ])

    answer = response.choices[0].message.content.strip()
    return answer



def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            response_text = ask_openai(message)
            return JsonResponse({'message': message, 'response': response_text})
        else:
            return JsonResponse({'error': 'No message provided'}, status=400)
    return render(request, 'chatbot.html')
