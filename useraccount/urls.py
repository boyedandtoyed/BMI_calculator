from django.urls import path
<<<<<<< HEAD
from useraccount.views import login_view, register_view, logout_view
=======
from useraccount.views import login_view, register_view, logout_view, send_suggestions, update_view
>>>>>>> e3fe231 (height bug correction)

app_name = 'user'

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
<<<<<<< HEAD
=======
    path('send/', send_suggestions, name="send-suggestions"),
    path('update/', update_view, name="update"),
>>>>>>> e3fe231 (height bug correction)
]