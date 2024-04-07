# File is created manually by Sunny
from django.http import HttpResponse
from django.shortcuts import render

# COde for video 6 learning url.py and views.py and anchor tag
# def index(request):
#     return HttpResponse('''<h1>Hello</h1> <a href="https://getbootstrap.com/docs/5.3/examples/sign-in/"> Sunny's World </a>''')
#
# def about(request):
#     return HttpResponse("About")

def index(request):
    # return HttpResponse("Home Page")
    params = {"Name" : "Sunny", "Place" : "Moon"}
    return render(request, "index.html", params)

def analyze(request):
    # Get the Text
    djtext = request.GET.get("text","default")

    # Check checkbox value
    removepunc = request.GET.get("removepunc", "off")   #off means default will not be printed in console
    full_caps = request.GET.get("full_caps", "off")
    new_line_remover = request.GET.get("new_line_remover", "off")
    extra_space_remover = request.GET.get("extra_space_remover", "off")
    char_count = request.GET.get("char_count", "off")
    print(djtext)
    print(removepunc)

    # CHeck which checkbox is on
    if removepunc == "on":
        punctuations_list = '''!()-{}[];"'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations_list:
                analyzed = analyzed + char
        params = {"purpose" : "Removed Punctuations from Sentence", "analyzed_text" : analyzed}
        return render(request, "analyze.html", params)
    elif (full_caps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {"purpose": "Text in Upper Case", "analyzed_text": analyzed}
        return render(request, "analyze.html", params)
    elif (new_line_remover == "on"):
        analyzed = ""
        for char in djtext :
            if char != "\n":
                analyzed = analyzed + char
        params = {"purpose": "Remove New Line", "analyzed_text": analyzed}
        return render(request, "analyze.html", params)
    elif (extra_space_remover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {"purpose": "Extra space removed from sentence", "analyzed_text": analyzed}
        return render(request, "analyze.html", params)
    elif (char_count == 'on'):
        analyzed= 0
        count = 0
        for i in djtext:
            if i!=" ":
                count += 1
        analyzed = analyzed + count
        params = {"purpose": "Counted Characters are, ", "analyzed_text": analyzed}
        return render(request, "analyze.html", params)
    else:
        return HttpResponse("Error")

def dashboard(request):
    return render(request, "dashboard.html")

# def removepunc(request):
#     djtext = request.GET.get('text', 'default7')
#     # return HttpResponse('''removepunc <a href = "/"> Go Back to Home Page </a>''')
#     print(djtext)
#     return HttpResponse("remove punc")
#
# def capitalizefirst(request):
#     return HttpResponse("capitalizefirst")
#
# def newlineremove(request):
#     return HttpResponse("newlineremove")
#
# def spaceremove(request):
#     return HttpResponse("spaceremove")
#
# def charcount(request):
#     return HttpResponse("charcount")


