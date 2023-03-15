from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from article.models import Auteur, Articles, Category, Comment
from django.forms import TextInput, FileInput, Select, DateTimeInput, Textarea, EmailInput, PasswordInput



choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class BlogForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control','rows':"4"}),
        }
# formulaire pour creer un utilisateurs 

class AuteurForm (forms.ModelForm): 
    class Meta: 
        model = Auteur
        fields = [
                    'status', 
                    'profil']
        widgets = {
            'status': TextInput(attrs={
                'class': "form-control",
                'style': 'margin: 7px;',
                'placeholder': 'Entrez le status de l\'auteur'
                }),
            'profil': FileInput(attrs={
                'class': "form-control", 
                'id': "image", 
                'accept': "image/png, image/jpg, image/jpeg", 
                'style': 'margin: 7px;',
                'placeholder': 'Charger une photo de profil'
                })
        }

# formulaire pour creer un user car auteur herite de 
# la classe user de django 
# le formulaire pour creer un user avec django 
class UserForm (UserCreationForm): 
    password1 = forms.CharField(max_length = 100, label = 'Mot de passe', 
                widget=forms.PasswordInput(attrs={
                    'class': 'form-control', 
                    'id': 'pass',
                    'placeholder': 'entrez votre mot de passe '}))
    password2 = forms.CharField(max_length = 100, label = 'Mot de passe', 
                widget=forms.PasswordInput(attrs={
                    'class': 'form-control', 
                    'id': 'pass1',
                    'placeholder': 'confirmez votre mot de passe'}))
    class Meta: 
        model = User 
        fields = [  'username', 
                    'first_name', 
                    'last_name', 
                    'email', 
                    'password1', 
                    'password2',]
        # les widgets permettent d'ajouter du style au formulaire 
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control", 
                'style': "margin: 7px;", 
                'placeholder': 'entrez votre nom d\'utilisateur'
                }),
            'first_name': TextInput(attrs={
                'class': "form-control", 
                'style': "margin: 7px;", 
                'placeholder': 'entrez votre nom'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control", 
                'style': "margin: 7px;", 
                'placeholder': 'entrez votre prenom'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': "margin: 7px;", 
                'placeholder': 'entrez votre adresse mail'
                }),
        }

# formulaire pour modifier un user 
class UserUpdateForm (forms.ModelForm):
    class Meta: 
        model = User
        fields = [  'username',
                    'first_name',
                    'last_name',
                    'email',]
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control", 
                'style': "margin: 7px;", 
                'placeholder': 'entrez votre nom d\'utilisateur'
                }),
            'first_name': TextInput(attrs={
                'class': "form-control", 
                'style': "margin: 7px;", 
                'placeholder': 'entrez votre nom'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control", 
                'style': "margin: 7px;", 
                'placeholder': 'entrez votre prenom'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': "margin: 7px;", 
                'placeholder': 'entrez votre adresse mail'
                })
        }

# formulaire pour creer un article 
class ArticlesForm (forms.ModelForm): 
    class Meta: 
        model = Articles
        fields = "__all__"
        widgets = {
            'titre': TextInput(attrs={
                'class': "form-control",
                'style': 'margin: 7px;',
                'placeholder': 'Entrez le Titre'
                }),
            'slug': TextInput(attrs={
                'class': "form-control", 
                'style': 'margin: 7px;',
                'placeholder': 'Entrez le slug'
                }), 
            'image': FileInput(attrs={
                'class': "form-control", 
                'style': 'margin: 7px;',
                'placeholder': 'Charger une image',
                'id':"img"
                }), 
            'auteur': Select(attrs={
                'class': "form-control", 
                'style': 'margin: 7px;',
                'placeholder': 'Definissez un auteur auteur'
                }), 
            'date_pub': DateTimeInput(attrs={
                'class': "form-control", 
                'style': 'margin: 7px;',
                'placeholder': 'Date de publication'
                }), 
            'intro': TextInput(attrs={
                'class': "form-control", 
                'style': 'margin: 7px;',
                'placeholder': 'écrire une introduction'
                }),
            'contenu': Textarea(attrs={
                'class': "form-control", 
                'style': 'margin: 7px;',
                'placeholder': 'placez le contenu de l\'artcile '
                }), 
            'statut': Select(attrs={
                'class': "form-control ", 
                'style': 'margin: 7px;',
                'placeholder': 'choisir un statut de publication'
                }),
            'category': Select(choices=choice_list, attrs={
                'class': "form-control", 
                'style': 'margin: 7px;',
                'placeholder': 'choisir une categorie'
                })
        }

# formulaire pour la connexion 
class LoginForm(forms.Form):
    username = forms.CharField(max_length = 100, label = 'nom d\'utilisateur', 
                widget=forms.TextInput(attrs={
                    'class': 'form-control', 
                    'placeholder': 'Enter Your userName'}))  
    password = forms.CharField(max_length = 100, label = 'Mot de passe', 
                widget=forms.PasswordInput(attrs={
                    'class': 'form-control',
                    'id': "pass", 
                    'placeholder': 'please enter password'}))