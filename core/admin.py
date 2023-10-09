from django.contrib import admin
from . models import LangchainPgCollection, LangchainPgEmbedding
admin.site.register(LangchainPgCollection)
admin.site.register(LangchainPgEmbedding)
