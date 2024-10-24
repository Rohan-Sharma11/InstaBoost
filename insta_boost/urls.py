from django.contrib import admin
from django.urls import path
from insta_boost import views
from .views import logout_view
from .views import signup_view,  forgot_password_view, reset_password_view, logout_view


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('',views.home_view, name = 'home'),
    path('follow/',views.BotRequestView, name = 'follow'),
    path('like/',views.BotLikeView, name = 'like'),
    path('comment/',views.BotCommentView, name = 'comment'),
    path('success/',views.SuccessView, name = 'success'),
    path('logout/', logout_view, name='logout'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('reset-password/', views.reset_password_view, name='reset_password'),

]
