from django.contrib import admin
from .models import DataSet, Data, UserDataCollection, UserDataEmbedding
admin.site.register(Data)
admin.site.register(DataSet) 
admin.site.register(UserDataCollection)
admin.site.register(UserDataEmbedding) 
 
