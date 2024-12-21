from django.db import models
from markdownx.models import MarkdownxField


class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
        


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name= 'posts')



    def __str__(self) :
        return self.title
    
class Commentaire(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='commentaires')
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Commentaire de {self.author} sur {self.post.title}'



