# Tasks — Spec 001: Godytec GoHighLevel Clinic Leads Dataset

## Objetivo

Gerar um dataset fake com 100 leads B2B simulados para representar o pipeline comercial da Godytec captando consultórios odontológicos dentro do GoHighLevel.

Arquivo final esperado:

data/godytec_ghl_clinic_leads.csv

---

## Task 1 — Criar estrutura de pastas

- Criar a pasta data se ela ainda não existir.
- Manter a pasta specs já criada.
- Não alterar arquivos PBIP nesta tarefa.

Critério de aceite:

- A pasta data deve existir no projeto.

---

## Task 2 — Criar dataset CSV

Criar o arquivo:

data/godytec_ghl_clinic_leads.csv

O arquivo deve conter exatamente 100 registros fake de leads B2B.

Critério de aceite:

- O arquivo CSV existe.
- O arquivo possui cabeçalho.
- O arquivo possui exatamente 100 linhas de dados.

---

## Task 3 — Implementar colunas obrigatórias

O CSV deve conter exatamente estas colunas:

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

Critério de aceite:

- Todas as colunas obrigatórias existem.
- Os nomes das colunas estão exatamente iguais aos definidos na spec.

---

## Task 4 — Gerar dados fake realistas

Gerar dados simulados coerentes com o contexto da Godytec.

Os leads devem representar consultórios odontológicos brasileiros, com variação de:

- nomes de clínicas;
- nomes de contatos;
- cidades;
- estados;
- tipos de clínica;
- origem do lead;
- campanhas;
- etapa do pipeline;
- valor mensal estimado;
- score;
- probabilidade de fechamento.

Critério de aceite:

- Os dados parecem realistas.
- Não usar nomes reais de empresas conhecidas.
- Não usar dados pessoais reais.

---

## Task 5 — Aplicar distribuição do pipeline

Distribuir os 100 leads aproximadamente assim:

New Lead: 15
Contacted: 18
Qualified: 16
Meeting Scheduled: 14
Proposal Sent: 12
Negotiation: 8
Won: 10
Lost: 7

Critério de aceite:

- O total deve ser 100.
- A distribuição deve permitir análise de funil no Power BI.

---

## Task 6 — Aplicar regras de consistência

Aplicar estas regras:

- Se pipeline_stage for Won, lead_status deve ser Won.
- Se pipeline_stage for Lost, lead_status deve ser Lost.
- Se pipeline_stage for Lost, lost_reason deve estar preenchido.
- Se pipeline_stage não for Lost, lost_reason deve ficar vazio.
- Se lead_status for Won ou Lost, next_follow_up_date pode ficar vazio.
- created_date deve ser menor ou igual a last_activity_date.
- next_follow_up_date, quando existir, deve ser maior ou igual a last_activity_date.

Critério de aceite:

- Nenhuma regra de consistência deve ser quebrada.

---

## Task 7 — Garantir IDs únicos

Gerar lead_id no formato:

GHL-0001
GHL-0002
GHL-0003

Até:

GHL-0100

Critério de aceite:

- Todos os lead_id são únicos.
- Não existem valores vazios em lead_id.

---

## Task 8 — Validar importação no Power BI

Garantir que o CSV seja simples para importação no Power BI:

- codificação UTF-8;
- separador por vírgula;
- cabeçalho na primeira linha;
- datas em formato YYYY-MM-DD;
- números sem símbolo de moeda;
- probability_to_close como número decimal.

Critério de aceite:

- O arquivo deve abrir corretamente como tabela no Power BI.

---

## Task 9 — Validar o resultado via script ou inspeção

Depois de gerar o CSV, validar:

- quantidade de registros;
- colunas obrigatórias;
- IDs únicos;
- distribuição por pipeline_stage;
- coerência entre pipeline_stage e lead_status;
- coerência de lost_reason;
- coerência básica de datas.

Critério de aceite:

- A validação não deve apontar erros críticos.

---

## Task 10 — Preparar versionamento

Após criar o dataset, verificar:

git status

Depois preparar commit com a mensagem:

Add fake GoHighLevel clinic leads dataset

Critério de aceite:

- O dataset aparece como alteração nova.
- Os arquivos da spec permanecem versionáveis.
- Nenhum arquivo PBIP deve ser alterado nesta spec.

---

## Fora de escopo

Não implementar nesta spec:

- dashboard Power BI;
- medidas DAX;
- dataset de pacientes;
- integração real com GoHighLevel;
- API;
- automações;
- dados reais.
