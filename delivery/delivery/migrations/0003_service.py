from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_auto_20220105_0105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
