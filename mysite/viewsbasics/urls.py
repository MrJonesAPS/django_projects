from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'viewsbasics'
urlpatterns = [
    path('', TemplateView.as_view(template_name='viewsbasics/index.html')),
    path('funktionally', views.funktionally),
    path('danger', views.danger),
    path('safer', views.safer),
    path('prettyurldata/<thing>', views.prettyurldata),
    path('bounce', views.bounce),
    path('icecream', views.Icecream.as_view()),
    path('icecream/<flavor>', views.Icecream.as_view()),
    path('bmi/<weight>/<height>', views.Bmi.as_view())
]    
