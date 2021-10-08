from django.shortcuts import render , redirect
from books.forms import BookAdd

# Create your views here.

def add_book(request):
    if request.method=='GET':
        form=BookAdd()
        context={}
        context['form']=form
        return render(request,'add_book.html',context)

    if request.method=="POST":
        form=BookAdd(request.POST)
        if form.is_valid():
            b_name=form.cleaned_data['bookname']
            a_name=form.cleaned_data['author']
            p_name=form.cleaned_data['price']
            a_name=form.cleaned_data['availablility']
            print(b_name,a_name,p_name,a_name)
            return redirect('add_book')
        else:
            return render(request,'add_book.html',{'form':form})

