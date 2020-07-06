from django.shortcuts import render
from collections import Counter

# Create your views here.

def main(request):
    return render(request, 'main.html')

def result(request):
    text_content = request.GET['totaltext']
    word_list=text_content.split()
    counter=Counter(word_list)
    return render(request, 'result.html',{'total_content': text_content, 'total': len(word_list), 'counter': counter.items()})