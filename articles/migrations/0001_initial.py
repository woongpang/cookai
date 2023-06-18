# Generated by Django 4.2.2 on 2023-06-16 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(default="", max_length=30)),
                ("content", models.TextField(default="", max_length=500)),
                ("update_at", models.DateTimeField(auto_now=True)),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("recipe", models.TextField(max_length=500)),
                ("image", models.URLField(blank=True, null=True)),
            ],
            options={
                "db_table": "Article",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=10)),
                ("info", models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ingredient_name", models.CharField(max_length=100)),
                (
                    "ingredient_info",
                    models.TextField(default=[], max_length=100, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RecipeIngredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ingredient_quantity", models.IntegerField(default=[])),
                ("ingredient_unit", models.CharField(default=[], max_length=100)),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="articles.article",
                    ),
                ),
                (
                    "ingredient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="articles.ingredient",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IngredientLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("link", models.URLField(blank=True, null=True)),
                ("link_img", models.URLField(blank=True, null=True)),
                (
                    "ingredient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="articles.ingredient",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment", models.TextField(max_length=300)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="articles.article",
                    ),
                ),
            ],
        ),
    ]
