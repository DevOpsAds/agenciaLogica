import json
import os

from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponse,JsonResponse,HttpResponseServerError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
def home_page(request):
    # Construindo os caminhos dos arquivos JSON usando a variável de ambiente APP_PATH
    features_file_path = os.path.join(os.environ.get('APP_PATH', '/usr/src/app/'), 'page_structure', 'features_or_services_section.json')
    products_file_path = os.path.join(os.environ.get('APP_PATH', '/usr/src/app/'), 'page_structure', 'product_simple.json')

    # Lendo o JSON do arquivo de recursos ou serviços
    with open(features_file_path) as json_file:
        data = json.load(json_file)

    # Lendo o JSON do arquivo de produtos
    with open(products_file_path) as products_file:
        products_data = json.load(products_file)
        
    # Adicionando um novo campo para cada produto, calculando o atraso
    for i, product in enumerate(products_data["products"]):
        product["delay"] = i * 300

    # Renderizando o template com os dados dos JSONs
    return render(request, 'home_page.html', {'categories': data['categories'], 'products': products_data["products"]})

def about_page(request):
    try:
        # Construindo os caminhos dos arquivos JSON usando a variável de ambiente APP_PATH
        json_file_path = os.path.join(os.environ.get('APP_PATH', '/usr/src/app/'), 'page_structure', 'top_skill_joao.py')
        more_json_file_path = os.path.join(os.environ.get('APP_PATH', '/usr/src/app/'), 'page_structure', 'more_skill_joao.json')
        experiences_json_file_path = os.path.join(os.environ.get('APP_PATH', '/usr/src/app/'), 'page_structure', 'my_experiences_joao.json')

        # Carregar os dados dos arquivos JSON
        with open(json_file_path, "r") as file:
            data = json.load(file)
        with open(more_json_file_path, "r") as more_file:
            more_data = json.load(more_file)
        with open(experiences_json_file_path, "r") as experiences_file:
            experiences_data = json.load(experiences_file)

        # Adicionar os dados ao contexto
        context = {
            "title": "Página Sobre",
            "content": "Bem-vindo à página sobre",
            "top_skills": data["top_skills"],  # Adicione os dados das principais habilidades ao contexto
            "more_skills": more_data["more_skills"],  # Adicione os dados das habilidades adicionais ao contexto
            "experiences": experiences_data["experiences"]  # Adicione os dados das experiências ao contexto
        }

        # Renderizar o template com os dados
        return render(request, "about_page.html", context)
    except FileNotFoundError:
        return HttpResponseServerError("Arquivo JSON não encontrado.")
    except json.JSONDecodeError:
        return HttpResponseServerError("Erro ao decodificar o arquivo JSON.")



def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Página de Contato",
        "content": "Bem-vindo à página de contato",
        "form": contact_form	
    }
    
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Obrigado!"})
    
    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')
    
    return render(request, "contact/view.html", context)