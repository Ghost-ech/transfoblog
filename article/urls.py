# definissons les urls des articles 
from .views import ArticleDetailView, CategoryView, AddCategoryView, detailView, List, Home, list_category
from .models import Category
from . import views 
from django.urls import path, include 
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', Home.as_view(), name = "home"),
    path('detail/<slug:slug>', detailView, name='detailView'),
    path ('listes_articles/', List.as_view(), name = 'listes_articles'),
    path('listes_articles/detail/<slug:slug>', detailView, name='detailView'),
    # url pour les auteurs 
    path ('creer_auteur', views.creer_auteur, name = 'creer'),
    path ('list_auteur', views.list_auteur, name = 'auteur'),
    path ('modifier_auteur/<int:id>', views.modifier_auteur, name = 'modifier'),
    path ('supprimer_auteur/<int:id>', views.supprimer_auteur, name = 'supprimer'),

    # url pour les articles 
    path ('article/<int:id>', ArticleDetailView.as_view(), name='article_detail'),
    path ('creer_article', views.creer_article, name = 'creer_art'),
    path ('list_article', views.list_article, name = 'article'),
    
    #path('list_article', list_article.as_view(), name='article'),
    
    path ('list_article_filtre', views.list_article_filtre, name = 'article_filtre'),
    path ('modifier_article/<int:id>', views.modifier_article, name = 'modifier_art'),
    path ('supprimer_article/<int:id>', views.supprimer_article, name = 'supprimer_art'),

    #url category
    path ('category/<str:cats>/', CategoryView, name='category'),
    path ('category/<str:cats>/detail/<int:id>', detailView, name='category'),
    path ('add_category/', AddCategoryView.as_view(), name='add_category'),
    path ('list_category/', views.list_category, name='liste_categorie'),
    path ('supprimer_categorie/<int:id>', views.supprimer_categorie, name = 'supprimer_cat'),

    # url pour la connexion et la deconexion
    path ('connexion', views.connexion, name = 'connexion'),
    path ('deconnexion', views.deconnexion, name = 'deconnexion'),
    

]

if settings.DEBUG: 
    urlpatterns += static (settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# url de base pour le developpement de app de connexion 
'''
    path("accounts/", include("django.contrib.auth.urls")),
    
'''