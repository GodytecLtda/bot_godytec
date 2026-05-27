# Spec 004 - Executive Business Summary

## Contexto

O projeto bot_godytec ja possui uma esteira de analise de dados para o pipeline B2B da Godytec.

O projeto ja contem:

- dataset fake com 100 leads B2B de consultorios odontologicos;
- analise geral do funil comercial;
- graficos do funil;
- dashboard HTML automatico;
- analise de ROI simulado por campanha;
- pipeline runner em Python.

Agora a Godytec precisa transformar as analises tecnicas em uma narrativa executiva para tomada de decisao.

## Objetivo

Criar um relatorio executivo de negocio que explique os principais resultados da analise de forma clara para um gestor da Godytec.

O relatorio deve responder:

1. O que esta acontecendo no funil comercial?
2. Qual e o tamanho da oportunidade de receita?
3. Quais campanhas estao performando melhor?
4. Quais campanhas precisam de revisao?
5. Quais acoes a Godytec deveria tomar agora?
6. Quais riscos aparecem nos dados?
7. Quais proximos passos sao recomendados?

## Arquivos esperados

Criar o script:

scripts/generate_executive_summary.py

Criar o relatorio Markdown:

analysis/004-executive-business-summary.md

Opcionalmente, atualizar o dashboard HTML para citar o relatorio executivo, mas somente se isso for simples e seguro.

## Dados de entrada

O script deve usar os arquivos e dados existentes:

data/godytec_ghl_clinic_leads.csv
analysis/003-campaign-roi-analysis.md

O script pode calcular novamente os indicadores diretamente do CSV, usando pandas.

## Conteudo obrigatorio do relatorio executivo

O relatorio deve conter as seguintes secoes:

1. Resumo executivo
2. Diagnostico do funil comercial
3. Receita potencial e receita ganha
4. Performance das campanhas
5. Campanhas recomendadas para investimento
6. Campanhas recomendadas para revisao
7. Riscos e pontos de atencao
8. Recomendacoes praticas para a Godytec
9. Proximos passos sugeridos

## Indicadores obrigatorios

O relatorio deve apresentar:

- total de leads;
- leads ganhos;
- leads perdidos;
- leads abertos ou em nutricao;
- taxa de conversao geral;
- receita mensal potencial;
- receita mensal ganha;
- ticket medio;
- melhor campanha por ROI estimado;
- melhor campanha por receita ganha;
- melhor campanha por receita potencial;
- campanhas com menor ROI estimado.

## Regras de linguagem

O relatorio deve ser escrito para uma pessoa de negocio, nao para um programador.

Usar linguagem clara, objetiva e executiva.

Evitar excesso de termos tecnicos.

O tom deve ser consultivo, como se a Godytec estivesse apresentando a analise para um decisor interno.

## Regras tecnicas

1. O script deve ler o CSV existente.
2. O script nao deve alterar o dataset.
3. O script nao deve alterar arquivos PBIP.
4. O script deve gerar o relatorio Markdown automaticamente.
5. O script deve criar a pasta analysis se ela nao existir.
6. O script deve ser executado pelo pipeline runner.
7. O script deve funcionar no Windows com o ambiente virtual do projeto.
8. O relatorio deve ser gerado em UTF-8.

## Atualizacao do pipeline runner

Atualizar:

scripts/run_analysis_pipeline.py

Para executar tambem:

scripts/generate_executive_summary.py

A ordem sugerida deve ser:

1. analyze_clinic_leads.py
2. generate_clinic_leads_charts.py
3. generate_html_dashboard.py
4. analyze_campaign_roi.py
5. generate_executive_summary.py
6. validar todos os arquivos esperados

## Saidas esperadas

Depois de rodar:

python "scripts\run_analysis_pipeline.py"

Deve existir:

analysis/004-executive-business-summary.md

E o pipeline deve continuar validando as saidas anteriores.

## Criterios de aceite

A implementacao sera aceita se:

1. O arquivo scripts/generate_executive_summary.py existir.
2. O arquivo analysis/004-executive-business-summary.md existir.
3. O relatorio trouxer uma narrativa executiva clara.
4. O relatorio apresentar recomendacoes praticas.
5. O pipeline runner executar o novo script.
6. O comando python "scripts\run_analysis_pipeline.py" terminar com sucesso.
7. Nenhum arquivo PBIP for alterado.
8. O dataset nao for alterado.
9. O git status ficar limpo apos commit e push.

## Fora de escopo

Nao implementar nesta spec:

- integracao com API real do GoHighLevel;
- modelo preditivo;
- dashboard Power BI;
- dataset de pacientes;
- envio automatico por email;
- relatorio PDF.
