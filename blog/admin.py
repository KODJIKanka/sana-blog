from django.contrib import admin
from blog.models import Category, Post, Commentaire

admin.site.site_header = "sana-blog"
admin.site.site_title = "sana"
admin.site.index_title = "Manageur"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at','category')
    search_fields = ('title',)

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at')

    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Post, PostAdmin)


