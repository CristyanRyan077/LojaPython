from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import produto, Cliente

def loja_python(request):
    produtos = produto.objects.all()
    return render(request, "Loja.html", {"produtos": produtos})


def ver_estoque(request):
    produtos = produto.objects.all()
    return render(request, "ver_estoque.html", {"produtos": produtos})


def ver_estoque_falta(request):
    produtos = produto.objects.filter(quantidade=0).order_by("-data_modificacao")
    return render(request, "produtos_emfalta.html", {"produtos": produtos})


def ver_menu(request):
    clientes = Cliente.objects.all()
    produtos = produto.objects.all()
    data_modificacao = produto.objects.all().order_by("-data_modificacao")[:5]
    data_criacao = produto.objects.all().order_by("data_criacao")
    produtos_falta = sum(1 for p in produtos if p.quantidade == 0)
    if request.method == "POST":
        return redirect("ver_estoque")
    context = {
        "total_produtos": produto.objects.count(),
        "produtos_emfalta": produtos_falta,
        "clientes": Cliente.objects.count(),
        "data_modificacao": data_modificacao,
        "data_criacao": data_criacao,
    }
    return render(request, "menu.html", context)


def remover_produto(request, id):
    produto_del = get_object_or_404(produto, id=id)
    produto_del.delete()
    return redirect("ver_estoque")


def remover_cliente(request, id):
    cliente_del = get_object_or_404(Cliente, id=id)
    cliente_del.delete()
    return redirect("ver_clientes")


def adicionar_produto(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        quantidade = request.POST.get("quantidade")
        preco = request.POST.get("preco")
        descricao = request.POST.get("descricao")
        imagem = request.FILES.get('imagem')

        produto.objects.create(
            nome=nome.capitalize().strip(),
            quantidade=int(quantidade),
            preco=float(preco),
            descricao=descricao,
            imagem=imagem,
        )
        return redirect("ver_menu")
    return render(request, "adicionar_produto.html")


def adicionar_cliente(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        telefone = request.POST.get("telefone")
        Cliente.objects.create(
            nome=nome.capitalize().strip(),
            telefone=telefone.strip(),
        )
        return redirect("ver_menu")
    return render(request, "adicionar_cliente.html")


def editar_produto(request, id):
    produtos = get_object_or_404(produto, id=id)
    if request.method == "POST":
        produtos.nome = request.POST.get("nome")
        produtos.quantidade = request.POST.get("quantidade")
        produtos.preco = request.POST.get("preco")
        produtos.save()
        return redirect("ver_estoque")
    return render(request, "editar_produto.html", {"produto": produtos})


def editar_cliente(request, id):
    clientes = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        clientes.nome = request.POST.get("nome")
        clientes.telefone = request.POST.get("telefone")
        clientes.save()
        return redirect("ver_clientes")
    return render(request, "editar_cliente.html", {"cliente": clientes})


def ver_clientes(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        telefone = request.POST.get("telefone")
        if nome and telefone:
            Cliente.objects.create(
                nome=nome.capitalize().strip(), telefone=telefone.strip()
            )
            return redirect("ver_clientes")
    clientes = Cliente.objects.all()
    return render(request, "ver_clientes.html", {"clientes": clientes})
