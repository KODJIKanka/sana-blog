from ..blog import models

def article_processor(request,id):
    article = models.Post.objects.get(id=id)
    return {'article' : article}