from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', UploadCSVView.as_view()),
    path('records/', NormalizedRecordsView.as_view()),
    path('approve/<int:pk>/', ApproveRecordView.as_view()),
    path('failed-records/', FailedRecordsView.as_view()),
]