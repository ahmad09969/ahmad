from django.shortcuts import render

def test(q):
    return render(q , 'mainsite/index.html')
