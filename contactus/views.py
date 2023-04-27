from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from contactus.forms import ContactForm


# Create your views here.
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact.refresh_from_db()
            contact.email = form.cleaned_data.get("email")
            contact.save()
            #send_email(request)
            return redirect("thanks")
    else:
        form = ContactForm()
    return render(request, "contact/index.html", {"form": form})


def thanks(request):
    return render(
        request,
        "contact/thanks.html",
    )


def send_email(request):
    subject = "Subject of the Email"
    message = "Body of the Email"
    email_from = "Sender Email Address"
    recipient_list = ["vuquangton@gmail.com"]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("Email Sent Successfully")
