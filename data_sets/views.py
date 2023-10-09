from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import UserDataEmbedding, UserDataCollection
from .embedder import embed_input
import uuid
from pgvector.django import L2Distance


def index(request):
    context = {}
    return render(request=request, template_name='data_sets/index.html', context=context)




def create_collection(request):
    if request.method == "POST":
        name = request.POST.get('collection_name') 
        print(name)

        create_collection = UserDataCollection.objects.create(
          uuid=uuid.uuid4(),
          name=name,
        )
        
        

        print(create_collection.name)
        context = {}
        
        return redirect('data_set:show_collection', uuid=create_collection.uuid)
    context = {}
    return render(request=request, template_name='data_sets/create_collection.html', context=context)

# @require_POST
# def create_data_embedding(request, uuid):
#     data_collection = DataCollection.objects.get(uuid=uuid)
#     text = request.POST.get('create_data_embedding')
#     embedding = embed_input(text)
#     print(text)
#     data_embedding = DataEmbedding.objects.create(
#         collection=uuid,
#         embedding=embedding,
#         document=text,
#         )
#     context = {"data_collection" : data_collection}
    
#     return redirect(request.path)
    

def show_collection(request, uuid):
    data_collection = UserDataCollection.objects.get(uuid=uuid)
    if request.method == "POST":
        text = request.POST.get('create_data_embedding')
        embedding = embed_input(text)
        # print(text)

        import uuid
        data_embedding = UserDataEmbedding.objects.create(
            uuid=uuid.uuid4(),
            collection=data_collection,
            embedding=embedding,
            document=text,
        
        )

        context = {"data_collection" : data_collection}
        return render(request=request, template_name='data_sets/show_collection.html', context=context)
    return render(request=request, template_name='data_sets/show_collection.html', context=context)
 

def search_collection(request, uuid):
    data_collection = UserDataCollection.objects.get(uuid=uuid)
    if request.method == "POST":
        search = request.POST.get('search_embeddings')
        embedding = embed_input(search)
        document = UserDataEmbedding.objects.order_by(
        L2Distance('embedding', embedding)
        ).first()
        context = {
        'search' : search,
        'similar_search_result' : document,
        }

        
        return render(request=request, template_name='data_sets/search_collection.html', context=context)
    context = {"data_collection" : data_collection}
    return render(request=request, template_name='data_sets/search_collection.html', context=context)
 

def interact_collection(request, uuid):
    data_collection = UserDataCollection.objects.get(uuid=uuid)
    if request.method == "POST":
        search = request.POST.get('search_embeddings')
        embedding = embed_input(search)
        document = UserDataEmbedding.objects.order_by(
        L2Distance('embedding', embedding)
        ).first()
        documents = UserDataCollection.objects.get(collection=data_collection.uuid)
        print(documents)
        context = {
        'search' : search,
        'similar_search_result' : document,
        'documents' : documents
        }

        
        return render(request=request, template_name='data_sets/interact_collection.html', context=context)
    context = {"data_collection" : data_collection}
    return render(request=request, template_name='data_sets/interact_collection.html', context=context)
 