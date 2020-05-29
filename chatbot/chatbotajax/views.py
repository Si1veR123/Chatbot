from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .response import find_response

# Create your views here.
def chatbot(request):
    return render(request, 'chatbotajax/chatbot.html')

@csrf_exempt
def chatbotapi(request):
    if request.method == "POST":
        recv_message = request.read().decode(request.encoding)
        return JsonResponse({"reply": find_response(recv_message)})
    else:
        return redirect(chatbot)
