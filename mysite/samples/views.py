from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import render


# Create your views here.

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s. </body></html>" % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s. </body></html>" % (offset, dt)
    return HttpResponse(html)


'''
chap 6 Form
'''


def current_url_view_good(request):
    return HttpResponse("Welcome to the page at %s" % request.path)


# GOOD (VERSION 1)
def ua_display_good1(request):
    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = 'unknown'
    return HttpResponse("Your browser is %s" % ua)


# GOOD (VERSION 2)
def ua_display_good2(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Your browser is %s" % ua)


# Show All request.META
def display_meta(request):
    dict_values = request.META.items()
    values = sorted(dict_values)
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


'''
chap 7
'''


def index(request):
    return HttpResponse('Index Page')


def archive(request):
    return HttpResponse('Archive Page')


def page(request, num="1"):
    return HttpResponse("This is the page of %s" % num)


def fixed_year(request, year):
    return HttpResponse("The year should be fixed in %s." % year)


def about(request, reviewid=0):
    if reviewid == 1:
        person = 'me'
    elif reviewid == 2:
        person = 'you'
    elif reviewid == 3:
        person = 'he/she'
    else:
        person = 'someone'
    return HttpResponse("Say something about %s." % person)


def year_archive(request, year):
    # return HttpResponse("In %s, %s is published." % (year, foo))
    return render(request, '07_review_year_archive.html', {'year_list': year})


def redirect_to_year(request):
    # ...
    year = 2012
    # ...
    return HttpResponseRedirect(reverse('reviews-year-archive', args=(year,)))


def show_namespace(request):
    return render(request, '07_show_namespace.html')
