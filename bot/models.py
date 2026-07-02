from django.db import models
from pgvector.django import VectorField
from django.db import models
# Create your models here.





class Botlogs(models.Model):

    update_id = models.CharField(max_length=100, unique=True)
    message_id = models.IntegerField(blank=False, null=False)
    message_text = models.CharField(max_length=2000, null=False)
    message_date = models.DateTimeField()
    sender_id = models.IntegerField(null=False, blank=False)
    sender_first_name = models.CharField(max_length=100)
    sender_last_name = models.CharField(max_length=100)
    is_sender_bot = models.BooleanField(default=False, null=False, blank=False)
    sender_lang_code = models.CharField(max_length=20, default="en", null=False, blank=False)
    chat_id = models.IntegerField(blank=False, null=False)
    chat_type = models.CharField(max_length=20, default="private", null=False, blank=False)
    response_message_text = models.CharField(max_length=2000, null=True, blank=False)

    def __str__(self):
        return str(self.message_id)




class ContextChunk(models.Model):
    content = models.TextField()
    embedding = VectorField(dimensions=1024)      
    created_at = models.DateTimeField(auto_now_add=True)
    
    

    

