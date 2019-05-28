from django.shortcuts import render
 
def check_code(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)