from django.core.mail import send_mail
from django.shortcuts import render


# Create your views here.
from BikeRental.settings import EMAIL_HOST_USER, EMAIL_RECIPIENT
from rental.models import BikeCategory, Bike, News


def index(request):
    categories = BikeCategory.objects.filter(published='P')
    bikes = Bike.randomized.get_queryset(3)
    news = News.latest.get_queryset(3)

    if request.method == 'POST':
        # Send mail
        subject = 'New rental request from '+ request.POST['Name']
        message = f"Name: {request.POST['Name']}\nFrom: {request.POST['Email']}\nMessage: {request.POST['Message']}"

        send_mail(subject=subject,
                  message=message,
                  from_email=EMAIL_HOST_USER,
                  recipient_list=EMAIL_RECIPIENT,
                  fail_silently=True
                  )

        return render(request, 'rental/index.html', context={'cats': categories,
                                                             'bikes': bikes,
                                                             'news': news,
                                                             'Name': request.POST['Name'],
                                                             })
    else:
        return render(request, 'rental/index.html', context={'cats': categories, 'bikes': bikes, 'news': news})
