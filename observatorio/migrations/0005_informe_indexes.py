from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('observatorio', '0004_informe_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informe',
            name='titulo',
            field=models.CharField(max_length=200, db_index=True),
        ),
        migrations.AlterField(
            model_name='informe',
            name='autor',
            field=models.CharField(max_length=100, db_index=True),
        ),
        migrations.AlterField(
            model_name='informe',
            name='resumen',
            field=models.TextField(db_index=True),
        ),
        migrations.AlterField(
            model_name='consultausuario',
            name='termino_buscado',
            field=models.CharField(max_length=100, db_index=True),
        ),
    ]

