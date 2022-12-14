from django.shortcuts import render
# from django.http import HttpResponse
from .forms import CsvModelForm
from .models import Csv
import csv
from polls.models import Sale
# Create your views here.


def upload_file_view(req):
    # return HttpResponse("<h1>Upload File</h1>")
    form = CsvModelForm(req.POST or None, req.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    print(row)
                    # row = "".join(row)
                    # row = row.replace(";", " ")
                    # row = row.split()
                    prod_desc = row[0]
                    cost = float(row[1])
                    date_of_pur = row[2]
                    Sale.objects.create(
                        prod_desc=prod_desc,
                        cost=cost,
                        date_of_pur=date_of_pur
                    )
            obj.activated = True
            obj.save()

    return render(req, 'csvs/upload.html', {'form': form})
