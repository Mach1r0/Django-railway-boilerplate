# Generated by Django 3.2.12 on 2023-11-10 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_compra'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItensCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='core.compra')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core.livro')),
            ],
        ),
    ]
