from django.urls import path,re_path
from . import views

urlpatterns = [
    path('muban/',views.muban),
    re_path(r'mengban.html/',views.page,name='page'),
    # path('mengban/one/',views.mengban_one),
    # path('mengban/two/',views.mengban_two),
    path('cancel/',views.Cancel),
]
