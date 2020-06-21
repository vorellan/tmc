from django.shortcuts import render

def post_list(request):
    return render(request, 'tmcapp/post_list.html', {})
