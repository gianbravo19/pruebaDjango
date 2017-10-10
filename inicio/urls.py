from django.conf.urls import url
import views

#DONT CHANGE THE URL NAMES AND THE FULL URL BECAUSE THERE ARE SOMES URLS USING TEXTUAL INFORMATION (NO REFERENCES)

app_name = 'inicio'

urlpatterns = [

    url(r'$', views.index_view, name="index"),

]

