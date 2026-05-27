# Tasks - Spec 003: Campaign ROI Analysis

## Objetivo

Criar uma analise de ROI simulado por campanha para descobrir quais campanhas da Godytec geram mais valor comercial.

A analise deve usar o dataset existente:

data/godytec_ghl_clinic_leads.csv

---

## Task 1 - Criar script de analise de ROI

Criar o arquivo:

scripts/analyze_campaign_roi.py

O script deve:

- ler o CSV existente;
- agrupar dados por campaign_name;
- calcular metricas comerciais por campanha;
- gerar relatorio Markdown;
- gerar graficos PNG;
- criar pastas automaticamente quando necessario.

Criterio de aceite:

- O arquivo scripts/analyze_campaign_roi.py existe.
- O script executa sem erro.

---

## Task 2 - Calcular custos simulados

Criar no script uma tabela interna de custos simulados por campanha.

Custos sugeridos:

- Dental Growth BR - Facebook: 3500
- Implantes Agenda Cheia - Google: 4200
- Consultorios Premium - LinkedIn: 3000
- WhatsApp Automation Sprint: 1800
- Webinar Agenda Cheia: 1500
- Prospeccao Sudeste: 1200
- Reativacao Consultorios: 1000

Para campanhas nao listadas, usar custo padrao de 1500.

Criterio de aceite:

- Toda campanha deve ter um custo associado.
- Nenhuma campanha deve ficar com custo vazio.

---

## Task 3 - Calcular metricas por campanha

Para cada campaign_name, calcular:

- total_leads
- won_leads
- lost_leads
- open_leads
- potential_monthly_revenue_brl
- won_monthly_revenue_brl
- average_ticket_brl
- average_lead_score
- average_probability_to_close
- simulated_campaign_cost_brl
- conversion_rate
- estimated_roi

Criterio de aceite:

- As metricas devem estar presentes no relatorio.
- As formulas devem respeitar requirements.md.

---

## Task 4 - Criar relatorio Markdown

Criar o arquivo:

analysis/003-campaign-roi-analysis.md

O relatorio deve conter:

- resumo executivo;
- ranking de campanhas por ROI;
- ranking por receita ganha;
- ranking por receita potencial;
- ranking por volume de leads;
- interpretacao de melhores campanhas;
- interpretacao de campanhas que precisam de revisao.

Criterio de aceite:

- O arquivo Markdown existe.
- O relatorio apresenta insights compreensiveis para uma pessoa de negocio.

---

## Task 5 - Criar graficos de ROI por campanha

Criar a pasta:

analysis/charts/campaign_roi/

Gerar os seguintes arquivos:

- campaign_leads_count.png
- campaign_potential_revenue.png
- campaign_won_revenue.png
- campaign_conversion_rate.png
- campaign_estimated_roi.png

Criterio de aceite:

- Todos os 5 graficos existem.
- Os graficos abrem corretamente no VS Code.

---

## Task 6 - Atualizar pipeline runner

Atualizar o arquivo:

scripts/run_analysis_pipeline.py

Para incluir:

scripts/analyze_campaign_roi.py

A ordem final deve incluir:

1. scripts/analyze_clinic_leads.py
2. scripts/generate_clinic_leads_charts.py
3. scripts/generate_html_dashboard.py
4. scripts/analyze_campaign_roi.py

Criterio de aceite:

- O comando python "scripts\run_analysis_pipeline.py" executa tudo com sucesso.
- O pipeline valida tambem as saidas da Spec 003.

---

## Task 7 - Garantir que arquivos fora de escopo nao sejam alterados

Nao alterar:

- data/godytec_ghl_clinic_leads.csv
- arquivos PBIP
- arquivos de dataset existente

Criterio de aceite:

- git status nao deve mostrar alteracoes em data/ ou arquivos PBIP.

---

## Task 8 - Validar implementacao

Depois de implementar, rodar:

python "scripts\run_analysis_pipeline.py"

Validar existencia de:

analysis/003-campaign-roi-analysis.md
analysis/charts/campaign_roi/campaign_leads_count.png
analysis/charts/campaign_roi/campaign_potential_revenue.png
analysis/charts/campaign_roi/campaign_won_revenue.png
analysis/charts/campaign_roi/campaign_conversion_rate.png
analysis/charts/campaign_roi/campaign_estimated_roi.png

Criterio de aceite:

- Pipeline termina com sucesso.
- Todos os arquivos esperados existem.

---

## Task 9 - Versionamento

Depois da revisao:

git status
git add
git commit
git push

Mensagem de commit sugerida:

Add campaign ROI analysis

Criterio de aceite:

- O git status fica limpo apos commit e push.
