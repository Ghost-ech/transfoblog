from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
# creons le modele auteur 

class Auteur (models.Model): 
    user = models.OneToOneField (User, related_name = 'Auteur', on_delete = models.CASCADE)     # user.Auteur renvoie 'instance Auteur associe au user
    status = models.CharField (max_length = 30)
    profil = models.ImageField(blank = True, default = 'pp.jpg')

    class Meta:
        db_table = 'Auteur'
    
    def __str__(self):
        return self.user.username



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article')


# status 
STATUT = (
    (0, "Brouillon"),
    (1, "publie")
)

# choix des categories 

class Articles (models.Model):
    titre = models.CharField(max_length = 100, unique = True)
    intro = models.TextField() 
    slug = models.SlugField(max_length = 100, unique= True)
    category = models.CharField(max_length=255, default='Cloud')
    image = models.ImageField(blank = True, default = 'test.png')
    auteur = models.ForeignKey(User, on_delete = models.DO_NOTHING, related_name = 'auteur')
    date_pub = models.DateTimeField( auto_now_add = True)
    #contenu = models.TextField()
    contenu = RichTextField(blank=True, null=True)
    statut = models.IntegerField(choices = STATUT, default = 0)
    

    class Meta: 
        ordering = ['-date_pub']
    
    def __str__(self): 
        return self.titre


class Comment(models.Model):
    post = models.ForeignKey(Articles, related_name='comments', on_delete=models.CASCADE)
    email = models.EmailField()
    body = models.TextField()
    name = models.CharField(max_length=100, default="inconnu")
    date_added = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_added']