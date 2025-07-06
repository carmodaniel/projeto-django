from django import forms
from .models import Cliente, Contrato, Servico

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cnpj', 'estado_origem', 'situacao']

    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj']
        if len(cnpj) != 14 or not cnpj.isdigit():
            raise forms.ValidationError("CNPJ deve ter 14 dígitos numéricos.")
        qs = Cliente.objects.filter(cnpj=cnpj)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Cliente com este CNPJ já existe")
        return cnpj

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['cliente', 'numero', 'valor']

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['cliente', 'tipo']

class BuscaClienteForm(forms.Form):
    #nome = forms.CharField(max_length=100, required=False)
    #cnpj = forms.CharField(max_length=14, required=False)
    termo = forms.CharField(label='Nome ou CNPJ', required=False)
