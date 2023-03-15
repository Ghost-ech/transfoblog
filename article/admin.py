from django.contrib.admin.decorators import register 
from django.contrib import admin
from . models import Auteur, Articles, Category
# Register your models here.
#admin.site.register(Auteur)
#admin.site. register (Articles)

# affichage d'un auteur dans django admin 
@register (Auteur)
class AuteurAdmin(admin.ModelAdmin): 
    list_display = ('user', 'status', 'profil')
    list_filter = ('user',)
    search_fields = ['user', 'status']

# affichage d'un article dans django admin 
@register (Articles)
class ArticlesAdmin(admin.ModelAdmin): 
    list_display = ('titre', 'slug', 'statut', 'date_pub')
    list_filter = ('statut',)
    search_fields = ['titre', 'contenu']
    prepopulated_fields = {'slug': ('titre',)}

admin.site.register(Category)