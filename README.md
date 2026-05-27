# Bot Godytec - GoHighLevel Dental Leads Analytics

## Status do Projeto

Versao atual: v1.2 - Executive Business Summary

Este projeto simula uma operacao de analise de dados da Godytec usando um cenario baseado em GoHighLevel para captacao de consultorios odontologicos.

O projeto foi desenvolvido com uma abordagem de Spec Driven Development, versionamento Git/GitHub e esteira automatizada de analise em Python.

---

## Visao Geral

A Godytec trabalha com dois pipelines principais:

1. Pipeline B2B da Godytec:
   - objetivo: captar consultorios odontologicos como clientes da Godytec;
   - foco atual deste projeto.

2. Pipeline B2C dos dentistas:
   - objetivo: captar pacientes para os dentistas clientes da Godytec;
   - sera tratado em etapa futura.

Nesta fase, o projeto analisa o funil B2B da Godytec para aquisicao de consultorios odontologicos.

---

## Funcionalidades Implementadas

### Spec 001 - Dataset fake B2B

Criacao de um dataset fake com 100 leads simulados de consultorios odontologicos.

Arquivo principal:

data/godytec_ghl_clinic_leads.csv

O dataset permite analisar:

- etapas do funil comercial;
- origem dos leads;
- campanhas;
- receita potencial;
- receita ganha;
- lead score;
- probabilidade de fechamento;
- motivos de perda.

### Spec 002 - Dashboard HTML automatico

Criacao de dashboard HTML gerado automaticamente a partir do dataset.

Arquivo principal:

dashboard/clinic_leads_dashboard.html

O dashboard apresenta:

- KPIs principais;
- resumo executivo;
- graficos do funil;
- graficos de origem, campanhas, receita e perdas.

### Spec 003 - Campaign ROI Analysis

Criacao da analise de ROI simulado por campanha.

Arquivo principal:

analysis/003-campaign-roi-analysis.md

Graficos principais:

analysis/charts/campaign_roi/

A analise responde:

- quais campanhas geram mais leads;
- quais campanhas geram mais receita potencial;
- quais campanhas geram mais receita ganha;
- quais campanhas possuem maior ROI estimado;
- quais campanhas merecem mais investimento;
- quais campanhas precisam de revisao.

### Spec 004 - Executive Business Summary

Criacao de relatorio executivo para tomada de decisao.

Arquivo principal:

analysis/004-executive-business-summary.md

O relatorio transforma os dados em narrativa de negocio, incluindo:

- diagnostico do funil comercial;
- oportunidade de receita;
- performance das campanhas;
- riscos e pontos de atencao;
- recomendacoes praticas;
- proximos passos sugeridos.

---

## Estrutura do Projeto

bot_godytec/
- data/
  - godytec_ghl_clinic_leads.csv
- analysis/
  - 001-clinic-leads-funnel-summary.md
  - 003-campaign-roi-analysis.md
  - 004-executive-business-summary.md
  - charts/
    - campaign_roi/
- dashboard/
  - clinic_leads_dashboard.html
- scripts/
  - analyze_clinic_leads.py
  - generate_clinic_leads_charts.py
  - generate_html_dashboard.py
  - analyze_campaign_roi.py
  - generate_executive_summary.py
  - run_analysis_pipeline.py
- specs/
  - 001-godytec-ghl-clinic-leads-dataset/
  - 002-auto-generated-html-dashboard/
  - 003-campaign-roi-analysis/
  - 004-executive-business-summary/
- requirements.txt
- README.md

---

## Como Rodar o Projeto no VS Code

### 1. Ativar o ambiente virtual

.\.venv\Scripts\Activate.ps1

### 2. Instalar dependencias

pip install -r requirements.txt

### 3. Rodar a esteira completa de analise

python "scripts\run_analysis_pipeline.py"

Esse comando executa:

1. Analise geral do funil
2. Geracao dos graficos principais
3. Geracao do dashboard HTML
4. Analise de ROI por campanha
5. Geracao do resumo executivo

---

## Principais Saidas Geradas

### Relatorios Markdown

analysis/001-clinic-leads-funnel-summary.md
analysis/003-campaign-roi-analysis.md
analysis/004-executive-business-summary.md

### Dashboard HTML

dashboard/clinic_leads_dashboard.html

### Graficos

analysis/charts/
analysis/charts/campaign_roi/

---

## Indicadores Analisados

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
- performance por campanha;
- ROI estimado por campanha;
- ranking de campanhas;
- recomendacoes executivas.

---

## Fluxo de Versionamento

Branches principais:

- main: versao estavel
- dev: desenvolvimento integrado
- work branches: branches por spec ou tarefa

Tags criadas:

- v1.1 - Campaign ROI Analysis
- v1.2 - Executive Business Summary

Fluxo usado:

work branch -> dev -> main -> tag de release

---

## Estado Atual

A versao v1.2 contem:

- dataset fake B2B;
- pipeline de analise em Python;
- graficos com matplotlib;
- dashboard HTML automatico;
- analise de ROI por campanha;
- relatorio executivo de negocio;
- documentacao SDD;
- versionamento Git/GitHub.

---

## Proximos Passos Possiveis

- Spec 005 - Criar dataset B2C de pacientes para dentistas.
- Spec 006 - Criar dashboard HTML consolidado com funil, ROI e resumo executivo.
- Spec 007 - Criar exportacao PDF do relatorio executivo.
- Spec 008 - Preparar modelo para futura integracao com GoHighLevel real.
