from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('observatorio', '0003_informe_palabras_clave_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='informe',
            name='palabra_clave',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='informe',
            name='fecha_publicacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='informe',
            name='contenido',
        ),
    ]
