from django.shortcuts import render
from core.models import LangchainPgEmbedding
from core.embed import embed_input
from pgvector.django import L2Distance
import uuid


def index(request):

  if request.method == "POST":
    text = request.POST.get('input_text')
    embedding = embed_input(text)
    # embeding_model = LangchainPgEmbedding.objects.create(
    #   uuid=uuid.uuid4(),
    #   embedding=embedding,
    #   document=text,
    # )
    # print(embeding_model.pk)
    document = LangchainPgEmbedding.objects.order_by(
      L2Distance('embedding', embedding)
      ).first()
    context = {
      'text' : text,
      'similar_search_result' : document,
    }
    return render(request=request, template_name='core/results.html', context=context)
  embeddings = LangchainPgEmbedding.objects.all()
  context = {'embeddings' : embeddings}
  return render(request=request, template_name='core/index.html', context=context)