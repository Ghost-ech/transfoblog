from django.shortcuts import render, redirect, HttpResponse
from article.forms import AuteurForm, UserForm, ArticlesForm,  UserUpdateForm, LoginForm, BlogForm
from article.models import Auteur, Articles, Category
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView, ListView


# def home(request):
#     home = Articles.objects.all()
#     context = {'home':home}
#     return render(request, 'home.html', context)
class Home(ListView):
    model = Articles
    template_name = 'home.html'
    queryset = Articles.objects.all()
    paginate_by = 6

class List(ListView):
    model = Articles
    template_name = 'listes_articles.html'
    queryset = Articles.objects.all()
    paginate_by = 6

    #to add block category navbar
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(List, self).get_context_data(*args, **kwargs)
        context ["cat_menu"] = cat_menu
        return context


# Create your views here.
# vue pour creer un utilisateur 
def creer_auteur(request): 
    typeform = "create"
    # form = AuteurForm()
    form = AuteurForm (request.POST, request.FILES)
    user_form = UserForm()
    # pour afficher l'erreur 
    erreur = ''
    err = ''
    if request.method == 'POST': 
        user_form = UserForm (request.POST)
        if user_form.is_valid() and form.is_valid(): 
            # emregistrer un user prealable
            user = user_form.save()
            #user.save()
            
            # mettre l'enregistrement de l'auteur en attente du user
            
            auteur = form.save(commit=False)

            auteur.user = user
            auteur.save()
            
            return redirect('/list_auteur')
        else: 
            erreur = form.errors
            err = user_form.errors
    context = {'form':form, 'erreur':erreur, 'user_form':user_form, 'err': err, 'typeform':typeform}
    return render (request, 'creer_auteur.html', context)

# creer la vue pour afficher la liste des auteurs 
def list_auteur (request): 
    auteur = Auteur.objects.all()
    context = {'auteur':auteur}
    return render (request, "auteur.html", context)

# vue pour modifier un utilisateur 
def modifier_auteur (request, id): 
    typeform = ""
    user = User.objects.get(id=id)
    user_form = UserUpdateForm(instance=user)
    form = AuteurForm(instance=user.Auteur)
    #user_form = UserForm()
    # pour afficher l'erreur 
    erreur = ''
    err = ''
    if request.method == 'POST': 
        user_form = UserUpdateForm (request.POST, instance = user)
        form = AuteurForm (request.POST, request.FILES, instance = user.Auteur)
        if user_form.is_valid and form.is_valid(): 
            # emregistrer un user prealable
            user = user_form.save()
            user.save()

            # mettre l'enregistrement de l'auteur en attente du user
            auteur = form.save(commit=False)

            auteur.user = user
            auteur.save()
            return redirect('/list_auteur')
        else: 
            erreur = form.errors
            err = user_form.errors
    context = {'form':form, 'erreur':erreur, 'user_form':user_form, 'err':err, 'typeform':typeform}
    return render (request, 'creer_auteur.html', context)

# vue pour supprimer un auteur 
def supprimer_auteur (request, id): 
    user = User.objects.get(id=id) 
    user.delete()
    return redirect("/list_auteur")

# fonction pour manipuler les articles 
# creer un article 

def creer_article(request): 
    form_art = ArticlesForm
    erreurs = ""
    if request.method == "POST": 
        form_art = ArticlesForm(request.POST, request.FILES)
        if form_art.is_valid(): 
            form_art.save()
            return redirect ('/list_article_filtre')
        else: 
            erreurs = form_art.errors 
    context = {'form_art': form_art, 'erreurs': erreurs}
    return render (request, 'creer_article.html', context)


# fonction pour afficher la liste des articles 
@login_required
def list_article (request): 
    article = Articles.objects.all()
    context = {'article': article}
    return render (request, "article.html", context)

   

# fonction pour afficher les articles d'un auteur
@login_required 
def list_article_filtre (request): 
    articles = Articles.objects.filter(auteur = request.user)
    context = {'article': articles}
    return render (request, "article.html", context)

# fonction pour modifier un article 
def modifier_article (request, id): 
    article = Articles.objects.get(id = id)
    form_art = ArticlesForm (instance = article)
    erreurs = ''
    if request.method =='POST': 
        form_art = ArticlesForm (request.POST, request.FILES, instance = article)
        if form_art.is_valid():
            form_art.save()
            return redirect('/list_article_filtre')
        else :
            erreurs = form_art.errors  
    context = {'article': article, 'form_art': form_art, 'erreurs': erreurs}        
    return render (request, 'creer_article.html', context)


# supprimer un article
def supprimer_article(request, id): 
    article = Articles.objects.get(id = id)
    article.delete()
    return redirect('/list_article_filtre')


class ArticleDetailView(DetailView):
    model = Articles, Auteur
    template_name = 'article_details.html'

# connexion 
def connexion (request):
    user = UserForm()
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data ['password'],
            )
            if user is not None:
                login(request, user)
                message = f'bonjour {user.username}! vous êtes connecté'
                return redirect('/list_article_filtre')
            else: 
                message = 'Identifants invalides.'
    context = {'form': form, 'message': message}
    return render (request, 'login.html', context)

# vue pour se deconnecter 
def deconnexion (request):
    logout(request)
    return redirect ('/connexion')


def detailView(request, slug):
    post = Articles.objects.get(slug=slug)
    comments = post.comments.all()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.post = post
            form.save()
            return redirect('detailView', slug=post.slug)
    else:
        form = BlogForm()

    content = {
        'article':post,
        'comments':comments,
        'form':form,

    }
    return render(request, 'article_details.html', content)


# début category section
def CategoryView(request, cats):
    category_posts = Articles.objects.filter(category=cats.replace('-',' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-',' '), 'category_posts': category_posts})

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

def list_category (request): 
    category = Category.objects.all()
    context = {'category':category}
    return render (request, "category_list.html", context)

# supprimer une catégorie
def supprimer_categorie(request, id): 
    category = Category.objects.get(id = id)
    category.delete()
    return redirect('/list_category')


    
#  fin category section





















































"""
# vue qui permet la connexion 
def connexion (request): 
    user = UserForm()
    username = request.POST['username']
    password = request.POST['password']
    authenticate(username = username, password=password)
    if user is not None: 
        if user.is_active:
            login(request, user)
            messages.success(request, f'Bienvenue {username}, vous pouvez creer et publier vos articles ici' )
            return redirect('/list_article')
        else : 
            return HttpResponse ('compte inactif!!')
    else :
        return HttpResponse ('compte inexistant !!')







def conne (request): 
    user_form = UserForm(request.POST)
    if request.method == 'POST': 
        user_form = UserForm(request.POST)
        if user_form.is_valid(): 
            user_form.save()
            username = user_form.cleaned_data('username')
            password = user_form.cleaned_data('password1')
            user = authenticate(username=username, password=password)
            login (request, user)
            messages.success(request, f'Bienvenue {username}, vous pouvez creer et publier vos articles ici' )
            
        else: 
            user_form = UserForm(request.POST)
    context = {'user_form': user_form }
    return render (request, 'connexion.html', context)

"""
            
"""
# ceci permet de faire un filtre 
@login_required 
def list_article_filtre (request, id): 
    auteur = User.objects.get(id = id)
    articles = Articles.objects.filter(auteur = auteur)
    context = {'article': articles}
    return render (request, "article.html", context)
"""             

