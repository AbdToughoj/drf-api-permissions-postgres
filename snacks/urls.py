from django.urls import path
from .views import SnackListView, SnackDetailView,  PostListView, PostDetailView

urlpatterns = [
   
    path('', SnackListView.as_view(), name= 'snack_list'),
    path('<int:pk>/',SnackDetailView.as_view(), name= 'snack_detail'),
    path('post/', PostListView.as_view(), name= 'post_list'),
    path('post/<int:pk>/',PostDetailView.as_view(), name= 'post_detail')
]