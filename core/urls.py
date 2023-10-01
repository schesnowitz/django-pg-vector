
from django.urls import include, path
from . views import index, qa_index, submit_question
app_name = 'core'
urlpatterns = [
    path('', qa_index, name='qa_index'),
    path('submit/   ', submit_question, name='submit_question')
]
