from django import forms
from .models import Cliente, Contrato, Servico

ESTADOS_BR = [
    ('', 'Selecione o estado'),
    *[(uf, uf) for uf in [
        'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG',
        'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
    ]]
]

class ClienteForm(forms.ModelForm):
    estado_origem = forms.ChoiceField(
        choices=ESTADOS_BR,
        label='Estado de Origem',
        required=True,
        widget=forms.Select(attrs={'style': 'color:#374151;'}),
        error_messages={'required': 'Selecione o estado de origem.'}
    )
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

    def clean_estado_origem(self):
        estado = self.cleaned_data.get('estado_origem')
        if not estado:
            raise forms.ValidationError('Selecione o estado de origem.')
        return estado

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['cliente', 'numero', 'valor']

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['cliente', 'tipo']

class BuscaClienteForm(forms.Form):
    termo = forms.CharField(label='Nome ou CNPJ', required=False)
