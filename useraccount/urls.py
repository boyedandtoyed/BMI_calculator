from django.urls import path
from useraccount.views import login_view, register_view, logout_view, send_suggestions, update_view
app_name = 'user'

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('send/', send_suggestions, name="send_suggestions"),
    path('update/', update_view, name="update"),
    # path('confirmation_page', send_confirmation, name="confirm"),
]