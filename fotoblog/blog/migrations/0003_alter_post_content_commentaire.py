# Generated by Django 5.0.7 on 2024-09-27 23:25

import django.db.models.deletion
import markdownx.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_post_delete_article_delete_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='blog.post')),
            ],
        ),
    ]
