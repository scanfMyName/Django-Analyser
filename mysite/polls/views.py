# from django.http import HttpResponse
# from .models import Question
# from django.shortcuts import get_object_or_404, render
# from django.template import loader
# from django.http import HttpResponse
# from django.contrib import messages
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# import logging
# import csv
# from rest_framework import status
# from django import forms
# from .models import Question, Choice
# from rest_framework import generics
# import io
# import csv
# import pandas as pd
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import FileUploadSerializer, SaveFileSerializer
# from rest_framework.decorators import api_view, renderer_classes
# from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


# class UploadFileView(generics.CreateAPIView):
#     serializer_class = FileUploadSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         file = serializer.validated_data['file']
#         reader = pd.read_csv(file)
#         for _, row in reader.iterrows():
#             new_file = Question(
#                 id=row['id'],
#                 question_text=row['question_text'],
#                 pub_date=row['pub_date'],
#             )
#             new_file.save()
#         return HttpResponse("File uploaded successfully")


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     return HttpResponse("You are looking at the result of question %s", question_id)


# def vote(request, question_id):
#     return HttpResponse("You are going to vote the question %s", question_id)


# def upload_csv(request):
#     data = {}
#     if "GET" == request.method:
#         return render(request, "polls/form.html", data)
#     # if not GET, then proceed
#     try:
#         csv_file = request.FILES["csv_file"]
#         if not csv_file.name.endswith('.csv'):
#             messages.error(request, 'File is not CSV type')
#             return HttpResponseRedirect(reverse("polls:upload_csv"))
#     # if file is too large, return
#         if csv_file.multiple_chunks():
#             messages.error(request, "Uploaded file is too big (%.2f MB)." % (
#                 csv_file.size/(1000*1000),))
#             return HttpResponseRedirect(reverse("polls:upload_csv"))
#         # return show_csv(file_data)
#         file_data = csv_file.read().decode("utf-8")

#         lines = file_data.split("\n")
#         # print(lines)
#         # print(file_data)
#     # loop over the lines and save them in db. If error , store as string and then display
#         n = lines.__len__()
#         i = 0
#         data_dict = {"id": [], "question_text": [], "pub_date": []}
        
#         for line in lines:
#             if i == 0 or i == n-1:
#                 i += 1
#                 continue
#             i += 1
#             fields = line.split(",")

#             # print(fields)
#             data_dict["id"].append(fields[0])
#             data_dict["question_text"].append(fields[1])
#             data_dict["pub_date"].append(fields[2])
#         # data_dict = {}
        
#         data_dict = pd.DataFrame.from_dict(data_dict)
#         # print(data_dict)
#         print(type(csv_file))
#         print(type(data_dict))
#         reader = pd.read_csv(csv_file)
#         for _, row in reader.iterrows():
#             new_file = Question(
#                 id=row['id'],
#                 question_text=row['question_text'],
#                 pub_date=row['pub_date'],
#             )
#             try:
#                 new_file.save()
#             except Exception as e:
#                 logging.getLogger("error_logger").error(
#             "Unable to save file. "+repr(e))
#                 messages.error(request, "Unable to upload file. "+repr(e))
#                 return HttpResponseRedirect(reverse("polls:upload_csv"))
#         return HttpResponse("You have successfully uploaded the file")
#         # try:
#         #     form = forms.EventsForm(data_dict)
#         #     if form.is_valid():
#         #         form.save()
#         #     else:
#         #         logging.getLogger("error_logger").error(form.errors.as_json())
#         # except Exception as e:
#         #     logging.getLogger("error_logger").error(repr(e))
#         #     pass
#     except Exception as e:
#         logging.getLogger("error_logger").error(
#             "Unable to upload file. "+repr(e))
#         messages.error(request, "Unable to upload file. "+repr(e))

#     return HttpResponseRedirect(reverse("polls:upload_csv"))


# def show_csv(request):
#     request_data = request.read().decode("utf-8")
#     print(request_data)
#     reader = csv.DictReader(request)
#     headers = [col for col in reader.fieldnames]
#     out = [row for row in reader]
#     return render(request, 'polls/csv_show.html', {'data': out, 'headers': headers})
# # Create your views here.
