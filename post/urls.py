from django.urls import path

from .views import post_pdf

app_name = 'posts'

urlpatterns = [
    path('<int:id>/', post_pdf, name='post_receipt'),
]
