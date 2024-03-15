from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def index(request):
    if request.method == "POST":
        input_text = request.POST.get('input_text')
        summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        return render(request, 'index.html', {'summary': summary} )
    return render(request, 'index.html' )

