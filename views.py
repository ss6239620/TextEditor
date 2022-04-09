#its made by myself
from django.http import HttpResponse
from django.shortcuts import render
def home_page(request):
    return render(request,'index.html')
def analyze(request):
    dj=request.GET.get('text')
    if dj=='':
        return HttpResponse('PLEASE ENTER SOME TEXT')
    for_deleter=request.GET.get('deleter','default')
    removepunc=request.GET.get('removepunc','default')
    for_captalize=request.GET.get('captalize','default')
    for_spacermover=request.GET.get('spaceremover','default')
    for_newliner=request.GET.get('newliner','default')
    # for deleter
    analyzed_data=dj.replace(for_deleter,'')
    #for removing punctuation
    if removepunc=='on':
        punc='''!()-[];:'"\,<>=./?@#$%^&*_~'''
        list_punc=[]
        list_punc[:0]=punc
        for i in list_punc:
            analyzed_data=analyzed_data.replace(i,'')
    #for ncaptalization
    if for_captalize=='on':
        analyzed_data=analyzed_data.upper()
    #for spaceremover
    if for_spacermover=='on':
        analyzed_data=analyzed_data.replace(' ','')
    #for newliner
    if for_newliner=='on':
        analyzed_data=analyzed_data.replace('\n',' ')
    if removepunc=='default' and for_captalize=='default' and for_spacermover=='default' and for_newliner=='default' and for_deleter=='':
        return HttpResponse('error')
    param={'var3':dj,'var2':analyzed_data}
    return render(request,'analyze.html',param)