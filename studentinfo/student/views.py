from django.shortcuts import render

# Create your views here.
def create(request):
    f = open("data.json","w")

    f.write()
    f.close()


    return render(request, "create.html", )

#def display(request):





#def update(request):






#def delete(request):






