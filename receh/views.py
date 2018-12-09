from django.shortcuts import render
def index(request):
    temp = open("receh/receh.csv","r").read()
    temp = temp.split(",")
    context = {
    "recehan": temp
    }
    return render(request,"index.html",context)
