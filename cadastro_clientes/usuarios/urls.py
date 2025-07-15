from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path("cadastro/", views.cadastro_view, name="cadastro"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("perfil/", views.perfil_view, name="perfil"),
    path("gerenciar/", views.gerenciar_usuarios, name="gerenciar"),
    path("bloquear/<int:user_id>/", views.bloquear_usuario, name="bloquear_usuario"),
    path("desbloquear/<int:user_id>/", views.desbloquear_usuario, name="desbloquear_usuario"),
    path("resetar-senha/<int:user_id>/", views.resetar_senha_usuario, name="resetar_senha_usuario"),
    path("deletar/<int:user_id>/", views.deletar_usuario, name="deletar_usuario"),
]