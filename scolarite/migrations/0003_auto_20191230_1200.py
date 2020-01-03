# Generated by Django 2.2.7 on 2019-12-30 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolarite', '0002_auto_20191228_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255)),
                ('mot_de_passe', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('Etudiant', 'Etudiant'), ('Enseignant', 'Enseignant'), ('Charge de scolarite', 'Charge de scolarite')], max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='label',
            new_name='type',
        ),
    ]