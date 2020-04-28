from django.db import models
from uuid import uuid4

# Create your models here.
class Note(models.Model):
    # unique identifier
    id = models.UUIDField(primary_key=True, 
    default=uuid4, editable=False)
    # The note object has a title and content
    # CharField is a built in function
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)