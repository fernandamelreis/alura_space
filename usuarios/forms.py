from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Maria da Silva"
            }
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control", 
                "placeholder": "Digite a sua senha"
            }
        ) 
    )
    
class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Maria da Silva"
            }
        )
    )
    
    email = forms.EmailField(
        label="Cadastre um e-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: mariasilva@email.com"
            }
        )
    )
    senha_1 = forms.CharField(
        label="Cadastre uma senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control", 
                "placeholder": "Digite a sua senha"
            }
        ) 
    )
    senha_2 = forms.CharField(
        label="Confirme a sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control", 
                "placeholder": "Digite a sua senha novamente"
            }
        ) 
    )