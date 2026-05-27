# Spec 001 — Godytec GoHighLevel Clinic Leads Dataset

## 1. Contexto

A Godytec está simulando uma operação comercial usando GoHighLevel para captar clientes B2B no segmento odontológico.

A empresa possui dois pipelines principais:

1. Pipeline B2B da Godytec:
   - Objetivo: captar consultórios odontológicos como clientes da Godytec.
   - Este é o foco desta spec.

2. Pipeline B2C dos dentistas:
   - Objetivo: captar pacientes para os dentistas clientes.
   - Este pipeline ficará para uma spec futura.

Esta spec cobre apenas o primeiro pipeline: Godytec tentando captar consultórios odontológicos como clientes.

## 2. Objetivo

Criar um dataset fake com 100 leads B2B simulados, representando consultórios odontológicos no pipeline comercial da Godytec dentro do GoHighLevel.

O dataset será usado para estudo de análise de dados no Power BI.

## 3. Arquivo esperado

Criar o arquivo:

data/godytec_ghl_clinic_leads.csv

O arquivo deve ser CSV, com cabeçalho, codificação UTF-8 e separado por vírgula.

## 4. Colunas obrigatórias

O CSV deve conter estas colunas:

lead_id
clinic_name
contact_name
contact_role
email
phone
city
state
clinic_type
team_size
monthly_patient_volume
main_interest
lead_source
campaign_name
pipeline_stage
lead_status
created_date
last_activity_date
next_follow_up_date
estimated_monthly_value_brl
lead_score
probability_to_close
lost_reason
notes

## 5. Regras principais

1. Criar exatamente 100 leads.
2. Cada lead_id deve ser único.
3. Os dados devem ser fake, mas realistas.
4. Não usar empresas reais.
5. Datas devem ser coerentes.
6. created_date deve ficar entre 2026-01-01 e 2026-05-27.
7. last_activity_date deve ser igual ou posterior a created_date.
8. next_follow_up_date deve ficar vazio para leads Won ou Lost.
9. lost_reason deve ser preenchido apenas quando pipeline_stage for Lost.
10. O arquivo deve importar corretamente no Power BI.

## 6. Etapas do pipeline

Usar estas etapas:

New Lead
Contacted
Qualified
Meeting Scheduled
Proposal Sent
Negotiation
Won
Lost

Distribuição sugerida:

New Lead: 15
Contacted: 18
Qualified: 16
Meeting Scheduled: 14
Proposal Sent: 12
Negotiation: 8
Won: 10
Lost: 7

Total: 100 leads.

## 7. Status dos leads

Usar estes status:

Open
Won
Lost
Nurturing

Regras:

- Se pipeline_stage for Won, lead_status deve ser Won.
- Se pipeline_stage for Lost, lead_status deve ser Lost.
- Para as demais etapas, usar Open ou Nurturing.

## 8. Origens dos leads

Usar variações como:

Facebook Ads
Google Ads
Instagram Organic
LinkedIn
Referral
Cold WhatsApp
Website Form
Webinar
Manual Prospecting

## 9. Interesses principais

Usar variações como:

Captação de Pacientes
Automação de WhatsApp
Landing Page
CRM para Clínica
Google Ads
Facebook Ads
Funil de Vendas
Reativação de Pacientes
Agendamento Online

## 10. Métricas que o dataset deve permitir

O dataset deve permitir analisar:

- total de leads;
- leads por etapa;
- taxa de conversão;
- leads por origem;
- leads por campanha;
- leads por cidade e estado;
- receita mensal potencial;
- receita ganha;
- ticket médio;
- lead score médio;
- motivos de perda;
- follow-ups futuros.

## 11. Critérios de aceitação

A implementação será aceita se:

1. O arquivo data/godytec_ghl_clinic_leads.csv existir.
2. O arquivo tiver exatamente 100 registros.
3. Todas as colunas obrigatórias existirem.
4. Os lead_id forem únicos.
5. As regras de status e etapa forem respeitadas.
6. O CSV abrir corretamente no Power BI.
7. O projeto continuar versionável no Git.

## 12. Fora de escopo

Não criar nesta spec:

- dataset de pacientes;
- dashboard Power BI;
- medidas DAX;
- integração real com GoHighLevel;
- dados reais;
- automações de API.

## 13. Instruções para o Codex

Implementar apenas o necessário para gerar o dataset fake desta spec.

Não alterar arquivos PBIP nesta etapa.

Branch atual esperada:

work-2026-05-27-versionamento

Mensagem de commit sugerida:

Add fake GoHighLevel clinic leads dataset spec
