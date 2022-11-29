from django.urls import re_path
from jea.apps.login.views import *

app_name = 'login'
urlpatterns = [
    # login/
    re_path(r'^$', UserFormView.as_view(), name='loginview'),

    # login/registrar/
    re_path(r'registrar/$', UserRegistrationFormView.as_view(),
        name='registrarview'),

    # login/esqueceu/:
    re_path(r'^esqueceu/$', ForgotPasswordView.as_view(), name='esqueceuview'),

    # login/trocarsenha/:
    re_path(r'^trocarsenha/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)$',
        PasswordResetConfirmView.as_view(), name='trocarsenhaview'),

    # logout
    re_path(r'^logout/$', UserLogoutView.as_view(), name='logoutview'),

    # login/perfil/
    re_path(r'^perfil/$', MeuPerfilView.as_view(), name='perfilview'),

    # login/editarperfil/
    re_path(r'^editarperfil/$', EditarPerfilView.as_view(), name='editarperfilview'),

    # login/usuarios/
    re_path(r'^usuarios/$', UsuariosListView.as_view(), name='usuariosview'),

    # login/usuarios/(id_usuario)
    re_path(r'usuarios/(?P<pk>[0-9]+)/$',
        UsuarioDetailView.as_view(), name='usuariodetailview'),

    # deletar usuario
    re_path(r'deletaruser/(?P<pk>[0-9]+)/$',
        DeletarUsuarioView.as_view(), name='deletarusuarioview'),

    # permissoes usuario
    re_path(r'permissoesusuario/(?P<pk>[0-9]+)/$',
        EditarPermissoesUsuarioView.as_view(), name='permissoesusuarioview'),

    # selecionar empresa
    re_path(r'selecionarempresa/$', SelecionarMinhaEmpresaView.as_view(),
        name='selecionarempresaview'),
]