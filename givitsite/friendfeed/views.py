from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD

def requestItem(request):

    if request.method == 'GET':
        founditems = FoundItem.objects.all()
        return render (request, 'feed.html', {'founds':founditems})

=======
>>>>>>> parent of ce13deb... update changes + add freindfeed
