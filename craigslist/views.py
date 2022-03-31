from django.shortcuts import render,redirect

from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')

def allListings(request):

    # if not request.user.is_authenticated:
    #     return redirect('login')

    listings = Listing.objects.all().order_by('-createdAt')
    count = listings.count()
    context={'listings': listings,'count': count}

    return render(request,'craigslist/listing_list.html', context)

def listingDetail(request,pk):
    listing = Listing.objects.get(id=pk)

    return render(request,'craigslist/listing.html',{'listing':listing})



def listingCreate(request):
    
    form = ListingForm()

    if request.method=='POST':
        # Create a form instance with POST data
        form=ListingForm(request.POST)        

        if form and form.is_valid():
            # Create, but don't save the new item instance.
            new_listing=form.save(commit=False)
            #update user for the item
            new_listing.user=request.user
            #save the item to db
            new_listing.save()

        return redirect('listings')
        
    return render(request,'craigslist/listing_form.html',{'form':form})


