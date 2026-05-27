# Bot Godytec - GoHighLevel Dental Leads Analytics

## Visao Geral

Este projeto simula uma operacao de analise de dados para a Godytec usando um cenario baseado em GoHighLevel.

A primeira fase analisa o pipeline B2B da Godytec para captar consultorios odontologicos como clientes.

## Objetivo

Criar um ambiente de estudo de analise de dados no VS Code, usando dados fake e versionados, para simular uma operacao real de CRM.

O projeto permite praticar:

- criacao de dataset fake;
- analise exploratoria de dados;
- analise de funil comercial;
- geracao de relatorios em Markdown;
- geracao de graficos com Python;
- versionamento com Git e GitHub;
- organizacao por Spec Driven Development.

## Dataset

Arquivo principal:

data/godytec_ghl_clinic_leads.csv

O dataset possui 100 leads B2B simulados.

Cada linha representa um consultorio odontologico que entrou no pipeline comercial da Godytec.

## Perguntas de Negocio

Este projeto busca responder:

1. Quantos leads existem no pipeline?
2. Em quais etapas os leads estao concentrados?
3. Quantos leads foram ganhos?
4. Quantos leads foram perdidos?
5. Qual e a taxa de conversao?
6. Qual e a receita mensal potencial?
7. Qual e a receita mensal ganha?
8. Quais canais geram mais leads?
9. Quais campanhas geram mais oportunidades?
10. Quais motivos explicam as perdas?
11. Quais leads devem ser priorizados comercialmente?

## Estrutura do Projeto

bot_godytec/
- data/
  - godytec_ghl_clinic_leads.csv
- analysis/
  - 001-clinic-leads-funnel-summary.md
  - charts/
- scripts/
  - analyze_clinic_leads.py
  - generate_clinic_leads_charts.py
- specs/
  - 001-godytec-ghl-clinic-leads-dataset/
- requirements.txt
- README.md

## Como Rodar no VS Code

Ativar ambiente virtual:

.\.venv\Scripts\Activate.ps1

Instalar dependencias:

pip install -r requirements.txt

Gerar relatorio analitico:

python "scripts\analyze_clinic_leads.py"

Gerar graficos:

python "scripts\generate_clinic_leads_charts.py"

## Metricas Geradas

O projeto calcula:

- total de leads;
- leads ganhos;
- leads perdidos;
- leads abertos ou em nutricao;
- taxa de conversao;
- receita mensal potencial;
- receita mensal ganha;
- ticket medio estimado;
- lead score medio;
- probabilidade media de fechamento;
- leads por etapa do pipeline;
- leads por origem;
- top campanhas;
- top cidades;
- motivos de perda;
- top leads para priorizacao comercial.

## Graficos Gerados

Os graficos ficam em:

analysis/charts/

Graficos atuais:

- leads_by_pipeline_stage.png
- leads_by_source.png
- revenue_by_pipeline_stage.png
- top_campaigns_by_leads.png
- lost_reasons.png

## Fluxo de Versionamento

Branches principais:

- main: versao estavel
- dev: desenvolvimento integrado
- work-2026-05-27-versionamento: branch de trabalho atual

Fluxo recomendado:

work branch -> dev -> main

## Status Atual

Implementado:

- dataset fake com 100 leads;
- documentacao SDD da Spec 001;
- ambiente Python;
- analise com pandas;
- relatorio Markdown;
- graficos PNG com matplotlib;
- versionamento no GitHub.

Proximos passos possiveis:

- criar dashboard em HTML;
- criar analise mais profunda por campanha;
- criar analise de ROI simulado;
- criar dataset B2C de pacientes;
- integrar depois com Power BI PBIP.
