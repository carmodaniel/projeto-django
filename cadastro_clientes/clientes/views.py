from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Contrato, Servico
from .forms import ClienteForm, BuscaClienteForm, ContratoForm, ServicoForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


@login_required
def cria_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:lista')
    else:
        form = ClienteForm()
    return render(request, 'clientes/form_cliente.html', {'form': form})

@login_required
def atualiza_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes:lista')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/form_cliente.html', {'form': form})

@login_required
def deleta_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes:lista')
    return render(request, 'clientes/confirma_delete.html', {'cliente': cliente})

@login_required
def busca_cliente(request):
    form = BuscaClienteForm(request.GET or None)
    clientes = None
    buscou = False
    if form.is_valid():
        termo = form.cleaned_data.get('termo')
        buscou = True
        if termo:
            clientes = Cliente.objects.filter(
                Q(nome__icontains=termo) | Q(cnpj__icontains=termo)
            )
        else:
            clientes = []
    return render(request, 'clientes/busca_cliente.html', {'form': form, 'clientes': clientes, 'buscou': buscou})

def leia_mais(request):
    return render(request, 'clientes/leia_mais.html')

def lista_contratos(request):
    contratos = Contrato.objects.all()
    return render(request, 'clientes/lista_contratos.html', {'contratos': contratos})

def cria_contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contratos')
    else:
        form = ContratoForm()
    return render(request, 'clientes/form_contrato.html', {'form': form})

def atualiza_contrato(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    if request.method == 'POST':
        form = ContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            form.save()
            return redirect('lista_contratos')
    else:
        form = ContratoForm(instance=contrato)
    return render(request, 'clientes/form_contrato.html', {'form': form})

def deleta_contrato(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    if request.method == 'POST':
        contrato.delete()
        return redirect('lista_contratos')
    return render(request, 'clientes/confirma_delete_contrato.html', {'contrato': contrato})

def lista_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'clientes/lista_servicos.html', {'servicos': servicos})

def cria_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_servicos')
    else:
        form = ServicoForm()
    return render(request, 'clientes/form_servico.html', {'form': form})

def atualiza_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('lista_servicos')
    else:
        form = ServicoForm(instance=servico)
    return render(request, 'clientes/form_servico.html', {'form': form})

def deleta_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        servico.delete()
        return redirect('lista_servicos')
    return render(request, 'clientes/confirma_delete_servico.html', {'servico': servico})
