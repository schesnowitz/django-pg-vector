from django.db import models

class DataSet(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return f"{self.name}"
    

class Data(models.Model):
    data_set = models.ForeignKey(DataSet, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    content = models.TextField()
    def __str__(self):
        return f"{self.data_set.name} : {self.description}"
    
from django.db import models
from pgvector.django import VectorField

class UserDataCollection(models.Model):
    name = models.CharField(blank=True, null=True)
    cmetadata = models.TextField(blank=True, null=True)  # This field type is a guess.
    uuid = models.UUIDField(primary_key=True)

    # class Meta:
    #     managed = True
    #     db_table = 'data_collection'
    # def __str__(self):
    #     return self.name
    

class UserDataEmbedding(models.Model):
    collection = models.ForeignKey(UserDataCollection, on_delete=models.CASCADE, blank=True, null=True, related_name="embeddings")
    embedding = VectorField(dimensions=1536)  # This field type is a guess.
    document = models.CharField(blank=True, null=True)
    cmetadata = models.TextField(blank=True, null=True)  # This field type is a guess.
    custom_id = models.CharField(blank=True, null=True)
    uuid = models.UUIDField(primary_key=True)

    # class Meta:
    #     managed = True
    #     db_table = 'data_embedding'
    
    