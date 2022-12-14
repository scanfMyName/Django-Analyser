from django.urls import path, re_path
from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:question_id>/', views.detail, name="detail"),
    path('<int:question_id>/results/', views.results, name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote"),
    # re_path(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
    path('upload/', views.UploadFileView.as_view(), name='upload-file')
]