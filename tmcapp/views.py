from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
import urllib.request
import xml.etree.ElementTree as ET

tmc_rate = 0
simple_rate = 0

def post_list(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            process(form)
            return redirect('success')
    else:
        form = PostForm()
    return render(request, 'tmcapp/post_list.html', {'form': form})

def success(request):
    return HttpResponse(simple_rate)

def process(form):
    date_form = form.data['fecha']
    dt = datetime.strptime(date_form,'%Y-%m-%d')
    clean_date = dt.date()
    d1 = datetime(2020, 6, 22)
    d1_date = d1.date()

    baseUrl = 'http://api.sbif.cl/api-sbifv3/recursos_api/tmc/2020?apikey=9c84db4d447c80c74961a72245371245cb7ac15f&formato=xml'
    request = urllib.request.Request(baseUrl)
    response = urllib.request.urlopen(request)
    tree = ET.parse(response)
    rootElem = tree.getroot()
    newroot = rootElem[6]
    
    flag = False

    for child in newroot:
        for newchild in child:
            if (newchild.tag == "{http://api.sbif.cl}Fecha"):
                date_child = newchild.text
                date_str = datetime.strptime(date_child, '%Y-%m-%d')
                date = date_str.date()
                if clean_date > date or clean_date == date :
                    flag = True
            
            if (newchild.tag == "{http://api.sbif.cl}Hasta"):
                until_child = newchild.text
                if until_child:
                    date_str = datetime.strptime(until_child, '%Y-%m-%d')
                    date = date_str.date()
                    if clean_date < date or clean_date == date :
                        flag = True

            if (newchild.tag == "{http://api.sbif.cl}Valor"):
                if flag == True:
                    rate = newchild.text
                    global tmc_rate   
                    tmc_rate = rate
    
    plazo = form.data['plazo']
    monto_uf = form.data['monto_uf']
    global simple_rate
    float_rate = float(tmc_rate)
    parse_rate = (float_rate/100)
    simple_rate = parse_rate * int(plazo) * float(monto_uf)
            

   
    



