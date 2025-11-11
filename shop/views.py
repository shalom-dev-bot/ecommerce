from django.shortcuts import render

# Create your views here.
def shop(request, *args, **kwargs):
    '''A view to render the shop homepage'''
    context = {}
    return render(request, 'shop/index.html', context)