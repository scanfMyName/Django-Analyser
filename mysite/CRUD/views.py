from django.shortcuts import render
from polls.models import Sale
from django.shortcuts import redirect
from csvs.models import Csv
from django.http import HttpResponseRedirect
from django.urls import reverse

import csv
# Create your views here.


def INDEX(request):
    sale = Sale.objects.all()
    context = {
        'sale': sale,
    }
    return render(request, 'CRUD/index.html', context)



def showaCsv(request, id):
    # print(filename)
    csv = Csv.objects.filter(id=id).first()
    filename = csv.file_name.path
    filedata = []
    header=[]
    with open(filename, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    header = row
                    
                else:
                    filedata.append(row)
    context = {
        "filedata":filedata,
        "header":header
    }
    return render(request, 'CRUD/showacsv.html', context)


def showallCSV(request):
    csvs = Csv.objects.all()
    filesdata = []
    for obj in csvs.iterator():
        tmpobj = {
            "filename":obj.file_name,
            "fileUploadDateTime":obj.uploaded,
            "activated":obj.activated,
            "path":obj.file_name.path,
        }
        filesdata.append(tmpobj)
    context = {
        "filesData":filesdata
       
    }
    return render(request, 'CRUD/showallCSV.html',context)


def ADD(request):
    if (request.method == 'POST'):
        print(request)
        prod_desc = request.POST.get('prod_desc')
        cost = request.POST.get('cost')
        date_of_pur = request.POST.get('date_of_pur')

        sale = Sale.objects.create(
            prod_desc=prod_desc,
            cost=cost,
            date_of_pur=date_of_pur
        )

        sale.save()
        return redirect('CRUD:home')
    sale = Sale.objects.all()
    context = {
        'sale': sale,
    }
    return render(request, 'CRUD/index.html', context)


def EDIT(request):

    sale = Sale.objects.all()
    print(type(sale[0].date_of_pur))
    context = {
        'sale': sale,
    }
    return render(request, 'CRUD/index.html', context)


def UPDATE(request, id):
    if (request.method == 'POST'):
        prod_desc = request.POST.get('prod_desc')
        cost = request.POST.get('cost')
        date_of_pur = request.POST.get('date_of_pur')
        sale = Sale(
            id=id,
            prod_desc=prod_desc,
            cost=cost,
            date_of_pur=date_of_pur
        )
        sale.save()
        return redirect('CRUD:home')
    sale = Sale.objects.all()
    context = {
        'sale': sale,
    }
    return render(request, 'CRUD/index.html', context)


def DELETE(request, id):
    sale = Sale.objects.filter(id=id).delete()
    return redirect('CRUD:home')


def UPDATECSV(request, id):
    csv = Csv.objects.filter(id=id).update(activated=True)
    return redirect('CRUD:csvfiles')

def DELETECSV(request, id):
    csv = Csv.objects.filter(id=id).delete()
    return redirect('CRUD:csvfiles')