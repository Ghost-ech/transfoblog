# Generated by Django 4.1.4 on 2022-12-27 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
                ('profil', models.ImageField(blank=True, default='pp.jpg', upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Auteur', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Auteur',
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, default='test.png', upload_to='')),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('contenu', models.TextField()),
                ('statut', models.IntegerField(choices=[(0, 'Brouillon'), (1, 'publie')], default=0)),
                ('categorie', models.IntegerField(choices=[(0, 'genie logiciel'), (1, 'infrastructure reseau'), (2, 'solution cloud'), (3, 'cyber securite')])),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='auteur', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_pub'],
            },
        ),
    ]