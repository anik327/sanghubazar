# Generated by Django 4.1.1 on 2022-10-10 14:15

from django.db import migrations, models
import store.validators


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_category_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='store/images/products', validators=[store.validators.validate_file_size]),
        ),
    ]