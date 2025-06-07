from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('observatorio', '0008_remove_perfilusuario_documento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medioamigo',
            name='autor',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medioamigo',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
