from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Imovel, Usuario

class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = ['bairro','quadra', 'lado', 'numero', 'focos_encontrados', 'acoes_realizadas']

    def __init__(self, *args, **kwargs):
        super(ImovelForm, self).__init__(*args, **kwargs)

class PesquisaForm(forms.Form):
    quadra = forms.CharField(max_length=100, required=False)
    lado = forms.CharField(max_length=100, required=False)

class UsuarioForm(UserCreationForm):
    nome = forms.CharField(max_length=30, required=True, help_text='Obrigatório.')
    login = forms.CharField(max_length=30, required=True, help_text='Obrigatório.')
    email = forms.EmailField(max_length=60, required=False, help_text='Obrigatório. Forneça um endereço de e-mail válido.')
    telefone = forms.CharField(max_length=14, required=True, help_text='Obrigatório.')
    foto = forms.ImageField(required=False, help_text='Envie uma foto do usuário.', widget=forms.FileInput)

    class Meta:
        model = Usuario
        fields = ('nome', 'login', 'email', 'telefone', 'foto', 'password1', 'password2')
