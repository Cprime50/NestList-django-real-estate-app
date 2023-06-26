from django.shortcuts import render, redirect
from .models import Listing, Category
from .forms import ListingForm
from accounts.models import Account

# Create your views here.

def listings(request):
    lists = Listing.objects.filter(is_sold=False)[0:6]
    return render (request,'catalog/frontpage.html', {'lists':lists})

def listing_retrieve(request, pk):             #Retrieve data of listing based on primary key of that data     #primary key is a special key used to identify each record in a database table 
    list_retrieve = Listing.objects.get(id=pk)                 #Here we ae saying that each record has a unique id which is the primary key associated with it eg 1 , 2 , 3
    next_id = id + 1

    # Use a filter operation so if there is no item with this pk it won't fail but will return an empty queryset
    next = Listing.objects.filter(pk=next_id)
    # Check the next step pk has a DB entry and set it to None if it doesn't exist
    if next.count() == 0:
        next_id = None
    return render(request, 'catalog/list_retrieve.html', {'list_retrieve':list_retrieve})

def listing_create(request):            #Create data, using forms the 'ListingForm' we already defined in our forms.py users can insert data into our model 'Listing'

    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ListingForm() 
    return render(request, 'catalog/listing_create.html', {'form':form})

def listing_update(request, pk):                #To update a listing we have to get an instance of an aready existing listing, select a record to update based o its primary key
    list_update = Listing.objects.get(id=pk)            
    form = ListingForm(instance=list_update)   #Instance method is important too tell django we are updating a record or listing and  not just creating a new one             

    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    return render(request, 'catalog/listing_update.html', {'form':form})

def listing_delete(request, pk):
    list_delete = Listing.objects.get(id=pk)
    list_delete.delete()
    return redirect('/')

