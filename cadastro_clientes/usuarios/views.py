from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm, CustomAuthenticationForm, CustomSetPasswordForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import SetPasswordForm
from django.shortcuts import get_object_or_404

# Tela de cadastro de usuário
def cadastro_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user)  # Cria perfil automaticamente
            messages.success(request, "Cadastro realizado com sucesso! Faça login.")
            return redirect("usuarios:login")
    else:
        form = CustomUserCreationForm()
    return render(request, "usuarios/cadastro.html", {"form": form})

# Tela de login
def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if hasattr(user, 'profile') and user.profile.is_blocked:
                messages.error(request, "Seu acesso está bloqueado. Procure o administrador do sistema para regularizar o acesso.")
                return render(request, "usuarios/login.html", {"form": form})
            login(request, user)
            return redirect("clientes:lista")  # Redireciona para a listagem de clientes
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = CustomAuthenticationForm()
    return render(request, "usuarios/login.html", {"form": form})

# Logout
def logout_view(request):
    logout(request)
    return redirect("usuarios:login")

@login_required
def perfil_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # Salva a imagem de perfil
            form.save()
            # Atualiza o email do usuário
            user = request.user
            user.email = form.cleaned_data['email']
            user.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('usuarios:perfil')
    else:
        form = ProfileForm(instance=profile, initial={
            'username': request.user.username,
            'email': request.user.email
        })
    return render(request, "usuarios/perfil.html", {"form": form, "profile": profile})

@login_required
def excluir_foto_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if profile.image:
        # Remove o arquivo físico se existir
        profile.image.delete(save=False)
        profile.image = None
        profile.save()
        messages.success(request, "Foto de perfil excluída com sucesso!")
    return redirect('usuarios:perfil')

@user_passes_test(lambda u: u.is_superuser)
def deletar_usuario(request, user_id):
    from django.contrib.auth.models import User
    user = get_object_or_404(User, pk=user_id)
    if user.is_superuser:
        messages.error(request, 'Não é permitido excluir o usuário administrador.')
        return redirect('usuarios:gerenciar')
    user.delete()
    messages.success(request, 'Usuário excluído com sucesso!')
    return redirect('usuarios:gerenciar')

@user_passes_test(lambda u: u.is_superuser)
def gerenciar_usuarios(request):
    from django.contrib.auth.models import User
    users = User.objects.all().select_related('profile')
    return render(request, 'usuarios/gerenciar.html', {'users': users})

@user_passes_test(lambda u: u.is_superuser)
def bloquear_usuario(request, user_id):
    from django.contrib.auth.models import User
    user = get_object_or_404(User, pk=user_id)
    profile, created = Profile.objects.get_or_create(user=user)
    profile.is_blocked = True
    profile.save()
    return redirect('usuarios:gerenciar')

@user_passes_test(lambda u: u.is_superuser)
def desbloquear_usuario(request, user_id):
    from django.contrib.auth.models import User
    user = get_object_or_404(User, pk=user_id)
    profile, created = Profile.objects.get_or_create(user=user)
    profile.is_blocked = False
    profile.save()
    return redirect('usuarios:gerenciar')

@user_passes_test(lambda u: u.is_superuser)
def resetar_senha_usuario(request, user_id):
    from django.contrib.auth.models import User
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = CustomSetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Senha redefinida com sucesso!')
            return redirect('usuarios:gerenciar')
    else:
        form = CustomSetPasswordForm(user)
    return render(request, 'usuarios/resetar_senha.html', {'form': form, 'usuario': user})