from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('observatorio', '0002_medioamigo_medio'),
    ]

    operations = [
        migrations.AddField(
            model_name='informe',
            name='palabras_clave',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='informe',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
