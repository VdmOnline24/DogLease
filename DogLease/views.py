from django.shortcuts import render

__all__=[
    'homepagefunc',
]
# Homepage func
def homepagefunc(request, pk=None):
    #form = TrainForm()
    #qs=Train.objects.all()
    #lst = Paginator(qs, 3)
    #page_number = request.GET.get('page')
    #page_obj = lst.get_page(page_number)
    #context = {'page_obj':page_obj}#, 'form':form}
    return render(request,'homepage.html')#,context)