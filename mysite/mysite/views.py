from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from mysite.forms import ContactForm


def hello(request):
    return HttpResponse("Hello world")


def my_homepage_view(request):
    return HttpResponse("Welcome to my homepage")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send_mail(
            #     cd['subject'],
            #     cd['message'],
            #     cd.get('email', 'noreply@example.com'),
            #     ['siteowner@example.com'],
            # )
            # return HttpResponseRedirect('/contact/thanks/')
            return render(request, 'contact_results.html', {'contact_info': cd})
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render(request, 'contact_form.html', {'form': form})


def debug(request):
    return HttpResponse("Debug!")


def page(request, num="1"):
    return HttpResponse("This is the page of %s" % num)
