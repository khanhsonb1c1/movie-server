from django.db import models

class Post(models.Model): 
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    # hiển thị tên record = title ( trên django admin )
    def __str__(self):
        return self.title
    
    