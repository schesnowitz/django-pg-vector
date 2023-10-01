
from django.urls import include, path
from . views import index
app_name = 'core'
urlpatterns = [
    path('', index, name='index')
]
