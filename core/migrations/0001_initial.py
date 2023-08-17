# Generated by Django 2.0.4 on 2023-08-17 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('avaliacao', '0001_initial'),
        ('atracao', '0001_initial'),
        ('endereco', '0001_initial'),
        ('comentario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pontoturistico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('aprovado', models.BooleanField(default=False)),
                ('atracoes', models.ManyToManyField(to='atracao.Atracao', verbose_name='Atrações')),
                ('avaliações', models.ManyToManyField(to='avaliacao.Avaliacao', verbose_name='Avaliações')),
                ('comentarios', models.ManyToManyField(to='comentario.Comentario', verbose_name='Comentários')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endereco.Endereco', verbose_name='Endereço')),
            ],
            options={
                'verbose_name': 'Ponto Turistico',
                'verbose_name_plural': 'Pontos Turisticos',
                'db_table': 'ponto_turistico',
            },
        ),
    ]