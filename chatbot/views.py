from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
from django.conf import settings

# Configure the OpenAI API client
client = OpenAI(api_key=settings.API_KEY)

def ask_openai(prompt):
    try:
        # Make the API call with the correct parameters
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,  # Adjust the max tokens based on your requirements
            temperature=0.7  # Adjust the temperature based on your requirements
        )
        # Return the response text
        return response.choices[0].message['content']
    except Exception as e:
        # Handle any errors that may occur
        return f"Error: {str(e)}"

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            response_text = ask_openai(message)
            return JsonResponse({'message': message, 'response': response_text})
        else:
            return JsonResponse({'error': 'No message provided'}, status=400)
    return render(request, 'chatbot.html')
