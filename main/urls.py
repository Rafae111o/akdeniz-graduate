from django.urls import path

from main.views import MainPageView, ContactPageView, PostDetailView, AboutPageView, redirect_to_home, NewsListPageView, \
    FaqPageView, LoginPageView, RegisterPageView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', redirect_to_home),
    path('home/', MainPageView.as_view(), name='index'),
    path('contact/', ContactPageView.as_view(), name='contacts'),
    path('news/<int:id>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('news/', NewsListPageView.as_view(), name='news'),
    path('faq/', FaqPageView.as_view(), name='faq'),
    path('login/', LoginPageView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('register/', RegisterPageView.as_view(), name='register'),
]