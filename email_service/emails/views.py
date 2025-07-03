from django.shortcuts import render
from django.http import JsonResponse
from .tasks import send_email_task





def test_mail(request):

    send_email_task.delay("task@example.com")
    return JsonResponse({"status":200, "message":"Email task queued!"})








