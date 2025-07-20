from django.db import migrations

def limpar_imagem_padrao(apps, schema_editor):
    Profile = apps.get_model('usuarios', 'Profile')
    # Limpa todos os perfis que ainda têm a imagem padrão
    for profile in Profile.objects.all():
        if profile.image and 'default.png' in str(profile.image):
            profile.image = None
            profile.save()

class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.RunPython(limpar_imagem_padrao, reverse_code=migrations.RunPython.noop),
    ] 