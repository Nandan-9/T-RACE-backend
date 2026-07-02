from django.db import models

# Create your models here.





class Botlogs(models.Model):

    update_id = models.CharField(max_length=100,unique=True)
    messsage_id = models.IntegerField(blank=False, null=False)
    message_text = models.CharField(max_length=2000, null=False)
    message_date = models.DateTimeField()
    sender_id = models.IntegerField(null=False,blank=False)
    sender_fist_name = models.CharField(max_length=100,unique=True)
    sender_last_name = models.CharField(max_length=100,unique=True)
    is_sender_bot = models.BooleanField(default=False,null= False,blank=False)
    sender_lang_code = models.CharField(max_length=20, default="en", null= False, blank= False)
    chat_id = models.IntegerField(blank=False, null=False)
    sender_lang_code = models.CharField(max_length=20, default="en", null= False, blank= False)
    chat_type = models.CharField(max_length=20, default="private", null= False, blank= False)


    def __str__(self):
        return self.message_id


    
    
    

    

