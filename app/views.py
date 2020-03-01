# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from django.shortcuts import render
from .models import Countries, Reactors
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.db.models import Count,Sum

@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    allcountries = Countries.objects.all()
    allreactors = Reactors.objects.all()
    bigchartquery = Countries.objects.exclude(country = 'World total')\
    .filter(capacity_total__isnull=False).order_by("-capacity_total").values_list('country','reactors')[:10]
    opcountquery = Reactors.objects.values('status').annotate(dcount=Count('status'))
    piechartquery = Countries.objects.exclude(country = 'World total')\
    .filter(capacity_total__isnull=False).values('country','capacity_total')
    yearsQuery = Reactors.objects.values('fgc').annotate(dcount=Sum('rup')).order_by('-fgc')[1:30]
    years = []
    tencountries = []
    tenreactors = []
    opcount = []
    piechartinfo = []
    for i in piechartquery:
        piechartinfo.append(i)

    for status in opcountquery:
        opcount.append(status)

    for country in bigchartquery:
        tencountries.append(country[0])
        tenreactors.append(country[1])
    for year in yearsQuery:
        years.append(year)
    context = {'allcountries': allcountries,
               'allreactors': allreactors,
               'tencountries': tencountries,
               'tenreactors': tenreactors,
               'opcount': opcount,
               'piechartinfo': piechartinfo,
               'years': years
               }
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))

# @login_required(login_url="/login/")
# def index(request):
#     allcountries = Countries.objects.all()
#     context = {
#         'allcountries': allcountries,
#     }
#     return render(request, 'pages/ui-tables.html', context)
#
# @login_required(login_url="/login/")
# def reactortables(request):
#
#     allreactors = Reactors.objects.all()
#     context = {
#         'allreactors': allreactors
#     }
#     return render(request, 'pages/ui-icons.html', context)
