# Spec 003 - Campaign ROI Analysis

## Contexto

O projeto bot_godytec ja possui uma esteira completa de analise para o pipeline B2B da Godytec:

- dataset fake com 100 leads de consultorios odontologicos;
- analise exploratoria em Python;
- relatorio Markdown;
- graficos PNG;
- dashboard HTML gerado automaticamente;
- pipeline runner.

Agora a Godytec precisa evoluir a analise para entender o desempenho das campanhas comerciais.

A pergunta central desta spec e:

Quais campanhas trazem mais valor comercial para a Godytec?

## Objetivo

Criar uma analise de ROI simulado por campanha, usando o dataset existente:

data/godytec_ghl_clinic_leads.csv

A analise deve agrupar os leads por campaign_name e calcular indicadores de performance comercial.

## Problema de negocio

A Godytec investe em diferentes campanhas para captar consultorios odontologicos.

Exemplos de campanhas:

- Dental Growth BR - Facebook
- Implantes Agenda Cheia - Google
- Consultorios Premium - LinkedIn
- WhatsApp Automation Sprint
- Webinar Agenda Cheia
- Prospeccao Sudeste

A empresa precisa saber:

1. Quais campanhas geram mais leads.
2. Quais campanhas geram maior receita potencial.
3. Quais campanhas geram mais clientes ganhos.
4. Quais campanhas possuem maior taxa de conversao.
5. Quais campanhas possuem melhor ROI estimado.
6. Quais campanhas devem receber mais investimento.
7. Quais campanhas devem ser pausadas ou revisadas.

## Arquivos esperados

Criar o script:

scripts/analyze_campaign_roi.py

Criar o relatorio:

analysis/003-campaign-roi-analysis.md

Criar graficos em:

analysis/charts/campaign_roi/

Graficos esperados:

- campaign_leads_count.png
- campaign_potential_revenue.png
- campaign_won_revenue.png
- campaign_conversion_rate.png
- campaign_estimated_roi.png

## Dados de entrada

Usar o dataset existente:

data/godytec_ghl_clinic_leads.csv

Colunas principais usadas na analise:

- campaign_name
- lead_id
- lead_status
- estimated_monthly_value_brl
- probability_to_close
- lead_score
- pipeline_stage
- lead_source

## Custo simulado por campanha

Como o dataset atual nao possui custo real de campanha, o script deve criar uma tabela interna com custos simulados mensais por campaign_name.

Exemplo:

- Dental Growth BR - Facebook: 3500
- Implantes Agenda Cheia - Google: 4200
- Consultorios Premium - LinkedIn: 3000
- WhatsApp Automation Sprint: 1800
- Webinar Agenda Cheia: 1500
- Prospeccao Sudeste: 1200
- Reativacao Consultorios: 1000

Se alguma campanha do CSV nao estiver na tabela, usar custo padrao de 1500.

## Metricas obrigatorias por campanha

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
- estimated_roi
- conversion_rate

## Formulas

conversion_rate:

won_leads / total_leads

estimated_roi:

(won_monthly_revenue_brl - simulated_campaign_cost_brl) / simulated_campaign_cost_brl

Se simulated_campaign_cost_brl for zero, estimated_roi deve ser zero.

## Regras

1. O script deve ler o CSV existente.
2. O script nao deve alterar o dataset.
3. O script nao deve alterar arquivos PBIP.
4. O script deve gerar um relatorio Markdown.
5. O script deve gerar graficos PNG.
6. O script deve criar as pastas necessarias automaticamente.
7. O script deve usar pandas e matplotlib.
8. Os graficos devem ser salvos em analysis/charts/campaign_roi/.
9. O relatorio deve explicar quais campanhas performaram melhor e pior.
10. O pipeline runner deve ser atualizado para incluir a analise de ROI por campanha.

## Atualizacao do pipeline runner

Atualizar:

scripts/run_analysis_pipeline.py

Para executar tambem:

scripts/analyze_campaign_roi.py

A ordem sugerida deve ser:

1. analyze_clinic_leads.py
2. generate_clinic_leads_charts.py
3. generate_html_dashboard.py
4. analyze_campaign_roi.py
5. validar todos os arquivos esperados

## Criterios de aceite

A implementacao sera aceita se:

1. O arquivo scripts/analyze_campaign_roi.py existir.
2. O arquivo analysis/003-campaign-roi-analysis.md existir.
3. A pasta analysis/charts/campaign_roi existir.
4. Todos os 5 graficos esperados forem gerados.
5. O relatorio apresentar ranking de campanhas.
6. O pipeline runner executar a nova analise.
7. O comando python "scripts\run_analysis_pipeline.py" terminar com sucesso.
8. Nenhum arquivo PBIP for alterado.
9. O git status ficar limpo apos commit e push.

## Fora de escopo

Nao implementar nesta spec:

- dados reais de campanhas;
- integracao com API do GoHighLevel;
- integracao com Facebook Ads ou Google Ads;
- dashboard Power BI;
- dataset de pacientes;
- modelo preditivo avancado.
