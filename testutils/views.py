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
    djtext = request.POST.get("text","default")

    # Check checkbox value
    removepunc = request.POST.get("removepunc", "off")   #off means default will not be printed in console
    full_caps = request.POST.get("full_caps", "off")
    new_line_remover = request.POST.get("new_line_remover", "off")
    extra_space_remover = request.POST.get("extra_space_remover", "off")
    char_count = request.POST.get("char_count", "off")
    # print(djtext)
    # print(removepunc)

    # CHeck which checkbox is on
    if removepunc == "on":
        punctuations_list = '''!()-{}[];"'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations_list:
                analyzed = analyzed + char
        params = {"purpose" : "Removed Punctuations from Sentence", "analyzed_text" : analyzed}
        # return render(request, "analyze.html", params)
        djtext = analyzed
    # elif (full_caps == "on"):
    if (full_caps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {"purpose": "Text in Upper Case", "analyzed_text": analyzed}
        # return render(request, "analyze.html", params)
        djtext = analyzed
    if (new_line_remover == "on"):
        analyzed = ""
        for char in djtext :
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {"purpose": "Remove New Line", "analyzed_text": analyzed}
        # return render(request, "analyze.html", params)
        djtext = analyzed
    if (extra_space_remover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {"purpose": "Extra space removed from sentence", "analyzed_text": analyzed}
        # return render(request, "analyze.html", params)
        djtext = analyzed
    if (char_count == 'on'):
        analyzed= 0
        count = 0
        for i in djtext:
            if i!=" ":
                count += 1
        analyzed = analyzed + count
        params = {"purpose": "Counted Characters are, ", "analyzed_text": analyzed}
        # return render(request, "analyze.html", params)

    if (removepunc != "on" and full_caps != "on" and new_line_remover != "on" and extra_space_remover != "on" and char_count != "on"):
        return HttpResponse("Please select operation atleat select one")
    # else:
    #     return HttpResponse("Error")
    return render(request, "analyze.html", params)

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


