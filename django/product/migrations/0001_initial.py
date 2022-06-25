# Generated by Django 3.2.13 on 2022-06-18 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/product')),
                ('description', models.TextField(max_length=1000)),
                ('slug', models.SlugField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('is_new', models.BooleanField(default=False)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('stock', models.IntegerField(default=0)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/product')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
    ]