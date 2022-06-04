"""
    Django is based on MVT
    (Model View And Template Architecture)

    A software design pattern or a software to design web application

    Three parts
    Model: Interface of data , responsible to maintain data

    Views: User Interface , that browser renders,consists of javascript,html and css

    Templates: starting html codes to get syntax,A template is rendered with a context. 
    Rendering replaces variables with their values, which are looked up in the context, and executes tags

    CSRF Tokens:cross site request forgery , server side application , to protect from malicious activities

"""



from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,"textutilities.html")
    
    #content={
    #    "Msg":"Good to see you",
    #    "Days":["Mon","Tue","Wed","Thurs"],
    #    "fname":"Nimisha",
    #    "lname":"Gupta"
    #    }
    
    #return HttpResponse('''<a href='/home' style="margin-right:20px">Home</a>
    #                    <a href='/about' style="margin-right:20px">About Us</a>
    #                    <a href='https://www.instagram.com' style="margin-right:20px">Instagram</a>
    #                    <a href='https://www.facebook.com' style="margin-right:20px">Facebook</a>''')#or use + " " 


def home(request):
    return HttpResponse("Welcome to home page")


def about(request):
    return HttpResponse("About this website")

def removepunc(inputtext):
    punc='''~!@#$%^&*()_+}{|:"?><,./;'[]=-\`}'''
    analyzed=""
    for char in inputtext:
        if char not in punc:
            analyzed+=char
    return analyzed
    
def capitalize(inputtext):
    analyzed=""
    for char in inputtext:
        analyzed+=char.upper()
    return analyzed

def removespace(inputtext):
    analyzed=""
    n=len(inputtext)
    for i in range(0,n):
        if not(inputtext[i]==" " and inputtext[i+1]==" "):
            analyzed+=inputtext[i]
    return analyzed


def analyzer(request):
    inputtext=request.POST.get("text","default")
    lists=list()
    rpunc=request.POST.get("rpunc","off")
    if rpunc=="on":
        inputtext=removepunc(inputtext)
        lists.append("Remove Punctuations")
    cap=request.POST.get("capitalize","off")
    if cap=="on":
        inputtext=capitalize(inputtext)
        lists.append("Capitalize Text")
    rspace=request.POST.get("rspace","off")
    if rspace=='on':
        inputtext=removespace(inputtext)
        lists.append("Remove Space")

    user_text={
        'Task':lists,
        'AnalyzedText':inputtext
        }

    return render(request,"analyzedText.html",user_text)