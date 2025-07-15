from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import Profile
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password, UserAttributeSimilarityValidator

# Formulário de cadastro de usuário
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    image = forms.ImageField(required=False, label='Foto de perfil')

    error_messages = {
        'password_mismatch': _('As senhas não coincidem. Por favor, digite a mesma senha nos dois campos.'),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nome de Usuário'
        self.fields['username'].help_text = (
            "Obrigatório. 4 a 30 caracteres. Use apenas letras minúsculas, números, '.', '_' ou '-', sem espaços ou caracteres especiais"
        )
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirmar Senha'
        # Mensagens de ajuda para senha
        self.fields['password1'].help_text = _(
            '<ul style="margin: 8px 0 0 0; padding-left: 18px; color: #555; font-size: 0.97em;">'
            '<li>Não pode ser muito parecida com suas outras informações pessoais.</li>'
            '<li>Deve conter pelo menos 8 caracteres.</li>'
            '<li>Não pode ser uma senha muito comum.</li>'
            '<li>Não pode ser composta apenas por números.</li>'
            '</ul>'
        )
        self.fields['password2'].help_text = _('Digite a mesma senha novamente para confirmação.')

    def clean_username(self):
        import re
        username = self.cleaned_data.get('username', '')
        # Regex explicação:
        # ^[a-z0-9](?!.*[._-]{2})[a-z0-9._-]{2,28}[a-z0-9]$
        # - Começa com letra minúscula ou número
        # - 2 a 28 caracteres intermediários (permitidos: a-z, 0-9, ., _, -), sem dois seguidos de . _ ou -
        # - Termina com letra minúscula ou número
        # - Total: 4 a 30 caracteres
        pattern = r'^(?=.{4,30}$)(?![._-])(?!.*[._-]{2})[a-z0-9]+([._-]?[a-z0-9]+)*$'
        if not re.match(pattern, username):
            raise forms.ValidationError(
                "Nome de usuário inválido.\n\nRegras:\n- Use apenas letras minúsculas (a-z), números (0-9), ponto (.), underline (_) ou hífen (-).\n- Não utilize espaços ou caracteres especiais.\n- O nome deve ter entre 4 e 30 caracteres.\n- Não pode começar ou terminar com ponto, underline ou hífen.\n- Não pode conter dois pontos, underlines ou hífens seguidos."
            )
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        username = self.cleaned_data.get('username')
        if password1 and username:
            try:
                validate_password(password1, user=None, password_validators=[
                    UserAttributeSimilarityValidator(user_attributes=['username'], max_similarity=0.7)
                ])
            except forms.ValidationError as e:
                messages = []
                for msg in e.messages:
                    if 'too similar to the username' in msg.lower():
                        messages.append('A senha é muito parecida com o nome de usuário.')
                    else:
                        messages.append(msg)
                raise forms.ValidationError(messages)
        return password1

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            # Salva a imagem de perfil se fornecida
            image = self.cleaned_data.get("image")
            if image:
                from .models import Profile
                profile, created = Profile.objects.get_or_create(user=user)
                profile.image = image
                profile.save()
        return user

# Formulário de login (pode usar o padrão do Django)
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Nome do Usuário")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].label = 'Nova Senha'
        self.fields['new_password2'].label = 'Confirmar Nova Senha'
        self.fields['new_password1'].help_text = (
            '<ul style="margin: 8px 0 0 0; padding-left: 18px; color: #555; font-size: 0.97em;">'
            '<li>Não pode ser muito parecida com suas outras informações pessoais.</li>'
            '<li>Deve conter pelo menos 8 caracteres.</li>'
            '<li>Não pode ser uma senha muito comum.</li>'
            '<li>Não pode ser composta apenas por números.</li>'
            '</ul>'
        )
        self.fields['new_password2'].help_text = 'Digite a mesma senha novamente para confirmação.'