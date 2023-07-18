from django.shortcuts import render, redirect
from django.http import HttpResponse
from openpyxl import Workbook
from .models import RespostaFormulario

def formulario(request):
    if request.method == 'POST':
        respostas = {
             'equipamento': request.POST.get('equipamento'),
            'qual_linha': request.POST.get('qual_linha'),
            'extensao': request.POST.get('extensao'),
            'extensao_sem_leitura': int(request.POST.get('extensao_sem_leitura', 0) or 0),
            'espacamento_medio': request.POST.get('espacamento_medio'),
            'tipo_dormente': request.POST.get('tipo_dormente'),
            'quantidade_dormentes_intercalados': int(request.POST.get('quantidade_dormentes_intercalados', 0) or 0),
            'tipo_fixacao': request.POST.get('tipo_fixacao'),
            'proporcao_fixacao_mista': request.POST.get('proporcao_fixacao_mista', ''),
            'tdc': request.POST.get('tdc'),
            'concreto': request.POST.get('concreto'),
            'isolado_nao_isol': request.POST.get('isolado_nao_isol'),
            'malha1': int(request.POST.get('malha1', 0) or 0),
            'malha2': int(request.POST.get('malha2', 0) or 0),
            'malha3': int(request.POST.get('malha3', 0) or 0),
            'malha4': int(request.POST.get('malha4', 0) or 0),
            'malha5': int(request.POST.get('malha5', 0) or 0),
            'malha6': int(request.POST.get('malha6', 0) or 0),
            'malha7': int(request.POST.get('malha7', 0) or 0),
            'malha8': int(request.POST.get('malha8', 0) or 0),
            'malha9': int(request.POST.get('malha9', 0) or 0),
            'malha10': int(request.POST.get('malha10', 0) or 0),
            'junta': int(request.POST.get('junta', 0) or 0),
            'guarda': int(request.POST.get('guarda', 0) or 0),
            'solda': int(request.POST.get('solda', 0) or 0),
            'Placa_Falta': int(request.POST.get('Placa_Falta', 0) or 0),
            'Placa_NOK': int(request.POST.get('Placa_NOK', 0) or 0),
            'Tirefond_Falta': int(request.POST.get('Tirefond_Falta', 0) or 0),
            'Tirefond_NOK': int(request.POST.get('Tirefond_NOK', 0) or 0),
            'Furo_NOK': int(request.POST.get('Furo_NOK', 0) or 0),
            'Shoulder_Falta': int(request.POST.get('Shoulder_Falta', 0) or 0),
            'Shoulder_NOK': int(request.POST.get('Shoulder_NOK', 0) or 0),
            'Palmilha_Falta': int(request.POST.get('Palmilha_Falta', 0) or 0),
            'Palmilha_NOK': int(request.POST.get('Palmilha_NOK', 0) or 0),
            'Isolador_Falta': int(request.POST.get('Isolador_Falta', 0) or 0),
            'Isolador_NOK': int(request.POST.get('Isolador_NOK', 0) or 0),
        }
        RespostaFormulario.objects.create(**respostas)
        return redirect('formulario')
    
    return render(request, 'formulario.html')

def download_excel(request):
    if request.method == 'POST':
        # Salvar os dados do formulário atual
        respostas = {
             'equipamento': request.POST.get('equipamento'),
            'qual_linha': request.POST.get('qual_linha'),
            'extensao': request.POST.get('extensao'),
            'extensao_sem_leitura': int(request.POST.get('extensao_sem_leitura', 0) or 0),
            'espacamento_medio': request.POST.get('espacamento_medio'),
            'tipo_dormente': request.POST.get('tipo_dormente'),
            'quantidade_dormentes_intercalados': int(request.POST.get('quantidade_dormentes_intercalados', 0) or 0),
            'tipo_fixacao': request.POST.get('tipo_fixacao'),
            'proporcao_fixacao_mista': request.POST.get('proporcao_fixacao_mista', ''),
            'tdc': request.POST.get('tdc'),
            'concreto': request.POST.get('concreto'),
            'isolado_nao_isol': request.POST.get('isolado_nao_isol'),
            'malha1': int(request.POST.get('malha1', 0) or 0),
            'malha2': int(request.POST.get('malha2', 0) or 0),
            'malha3': int(request.POST.get('malha3', 0) or 0),
            'malha4': int(request.POST.get('malha4', 0) or 0),
            'malha5': int(request.POST.get('malha5', 0) or 0),
            'malha6': int(request.POST.get('malha6', 0) or 0),
            'malha7': int(request.POST.get('malha7', 0) or 0),
            'malha8': int(request.POST.get('malha8', 0) or 0),
            'malha9': int(request.POST.get('malha9', 0) or 0),
            'malha10': int(request.POST.get('malha10', 0) or 0),
            'junta': int(request.POST.get('junta', 0) or 0),
            'guarda': int(request.POST.get('guarda', 0) or 0),
            'solda': int(request.POST.get('solda', 0) or 0),
            'Placa_Falta': int(request.POST.get('Placa_Falta', 0) or 0),
            'Placa_NOK': int(request.POST.get('Placa_NOK', 0) or 0),
            'Tirefond_Falta': int(request.POST.get('Tirefond_Falta', 0) or 0),
            'Tirefond_NOK': int(request.POST.get('Tirefond_NOK', 0) or 0),
            'Furo_NOK': int(request.POST.get('Furo_NOK', 0) or 0),
            'Shoulder_Falta': int(request.POST.get('Shoulder_Falta', 0) or 0),
            'Shoulder_NOK': int(request.POST.get('Shoulder_NOK', 0) or 0),
            'Palmilha_Falta': int(request.POST.get('Palmilha_Falta', 0) or 0),
            'Palmilha_NOK': int(request.POST.get('Palmilha_NOK', 0) or 0),
            'Isolador_Falta': int(request.POST.get('Isolador_Falta', 0) or 0),
            'Isolador_NOK': int(request.POST.get('Isolador_NOK', 0) or 0),
        }
        RespostaFormulario.objects.create(**respostas)

    workbook = Workbook()
    worksheet = workbook.active

    # Buscar a última resposta do banco de dados
    resposta = RespostaFormulario.objects.latest('id')

    linha = [
        resposta.equipamento,
        resposta.qual_linha,
        resposta.extensao,
        resposta.extensao_sem_leitura,
        resposta.espacamento_medio,
        resposta.tipo_dormente,
        resposta.quantidade_dormentes_intercalados,
        resposta.tipo_fixacao,
        resposta.proporcao_fixacao_mista,
        resposta.tdc,
        resposta.concreto,
        resposta.isolado_nao_isol,
        resposta.malha1,
        resposta.malha2,
        resposta.malha3,
        resposta.malha4,
        resposta.malha5,
        resposta.malha6,
        resposta.malha7,
        resposta.malha8,
        resposta.malha9,
        resposta.malha10,
        resposta.junta,
        resposta.guarda,
        resposta.solda,
        resposta.Placa_Falta,
        resposta.Placa_NOK,
        resposta.Tirefond_Falta,
        resposta.Tirefond_NOK,
        resposta.Furo_NOK,
        resposta.Shoulder_Falta,
        resposta.Shoulder_NOK,
        resposta.Palmilha_Falta,
        resposta.Palmilha_NOK,
        resposta.Isolador_Falta,
        resposta.Isolador_NOK,
    ]
    worksheet.append(linha)

    # Criar uma resposta de arquivo
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=formulario_respostas.xlsx'

    # Salvar o arquivo Excel no objeto de resposta
    workbook.save(response)

    return response

def proximo_equipamento(request):
    # Lógica para lidar com a ação "Próximo Equipamento"
    # ...
    
    return redirect('formulario')
