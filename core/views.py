from django.shortcuts import render
from core.models import LangchainPgEmbedding
from core.embed import embed_input
from pgvector.django import L2Distance
import uuid
from django.views.decorators.http import require_POST


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



def qa_index(request):
    articles = LangchainPgEmbedding.objects.all()
    context = {'articles' : articles}
    return render(request=request, template_name="core/qa_index.html", context=context)


@require_POST
def submit_question(request):
    prompt = request.POST.get("prompt")
    instruction = request.POST.get("qa-instructions")
    # answer = run_retrieval_qa_pipeline(prompt, instruction)
    # Answers.objects.create(row_id=uuid4(), question=prompt, answer=answer)
    context = { 'question' :  prompt, 'answer' : 'answer'}
    return render(request=request, template_name="core/qa_response.html", context=context)