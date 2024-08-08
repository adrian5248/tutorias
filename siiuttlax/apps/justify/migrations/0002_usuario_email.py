from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('justify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',  # Ajusta este nombre al modelo correcto
            name='email',
            field=models.EmailField(default='mail@mail.com', max_length=254),
        ),
    ]
