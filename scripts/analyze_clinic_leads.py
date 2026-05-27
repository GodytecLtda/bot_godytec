from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/godytec_ghl_clinic_leads.csv")
OUTPUT_PATH = Path("analysis/001-clinic-leads-funnel-summary.md")


def money(value: float) -> str:
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def percent(value: float) -> str:
    return f"{value:.2f}%"


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    total_leads = len(df)
    won_leads = int((df["lead_status"] == "Won").sum())
    lost_leads = int((df["lead_status"] == "Lost").sum())
    open_leads = int(df["lead_status"].isin(["Open", "Nurturing"]).sum())

    conversion_rate = (won_leads / total_leads) * 100 if total_leads else 0

    potential_revenue = float(df["estimated_monthly_value_brl"].sum())
    won_revenue = float(
        df.loc[df["lead_status"] == "Won", "estimated_monthly_value_brl"].sum()
    )
    avg_ticket = float(df["estimated_monthly_value_brl"].mean())
    avg_score = float(df["lead_score"].mean())
    avg_probability = float(df["probability_to_close"].mean() * 100)

    pipeline_summary = df["pipeline_stage"].value_counts()
    source_summary = df["lead_source"].value_counts()
    campaign_summary = df["campaign_name"].value_counts().head(10)
    city_summary = df["city"].value_counts().head(10)
    lost_reason_summary = (
        df.loc[df["lead_status"] == "Lost", "lost_reason"].value_counts()
    )

    priority_table = (
        df.loc[df["lead_status"].isin(["Open", "Nurturing"])]
        .sort_values(
            by=["lead_score", "probability_to_close", "estimated_monthly_value_brl"],
            ascending=[False, False, False],
        )
        .head(10)
    )

    report = []
    report.append("# Análise 001 — Funil Comercial Godytec")
    report.append("")
    report.append("## Dataset")
    report.append("")
    report.append(f"Arquivo analisado: {DATA_PATH}")
    report.append("")
    report.append("## Resumo Executivo")
    report.append("")
    report.append("| Métrica | Valor |")
    report.append("|---|---:|")
    report.append(f"| Total de leads | {total_leads} |")
    report.append(f"| Leads ganhos | {won_leads} |")
    report.append(f"| Leads perdidos | {lost_leads} |")
    report.append(f"| Leads abertos/nutrição | {open_leads} |")
    report.append(f"| Taxa de conversão | {percent(conversion_rate)} |")
    report.append(f"| Receita mensal potencial | {money(potential_revenue)} |")
    report.append(f"| Receita mensal ganha | {money(won_revenue)} |")
    report.append(f"| Ticket médio estimado | {money(avg_ticket)} |")
    report.append(f"| Lead score médio | {avg_score:.2f} |")
    report.append(f"| Probabilidade média de fechamento | {percent(avg_probability)} |")
    report.append("")
    report.append("## Leads por etapa do pipeline")
    report.append("")
    for stage, count in pipeline_summary.items():
        report.append(f"- {stage}: {count}")
    report.append("")
    report.append("## Leads por origem")
    report.append("")
    for source, count in source_summary.items():
        report.append(f"- {source}: {count}")
    report.append("")
    report.append("## Top 10 campanhas")
    report.append("")
    for campaign, count in campaign_summary.items():
        report.append(f"- {campaign}: {count}")
    report.append("")
    report.append("## Top 10 cidades")
    report.append("")
    for city, count in city_summary.items():
        report.append(f"- {city}: {count}")
    report.append("")
    report.append("## Motivos de perda")
    report.append("")
    for reason, count in lost_reason_summary.items():
        report.append(f"- {reason}: {count}")
    report.append("")
    report.append("## Top 10 leads para priorização comercial")
    report.append("")
    report.append(
        "| Clínica | Cidade | Estado | Etapa | Valor Mensal | Score | Prob. Fechamento | Próximo Follow-up |"
    )
    report.append("|---|---|---|---|---:|---:|---:|---|")
    for _, row in priority_table.iterrows():
        report.append(
            "| "
            f"{row['clinic_name']} | "
            f"{row['city']} | "
            f"{row['state']} | "
            f"{row['pipeline_stage']} | "
            f"{money(float(row['estimated_monthly_value_brl']))} | "
            f"{row['lead_score']} | "
            f"{percent(float(row['probability_to_close']) * 100)} | "
            f"{row['next_follow_up_date']} |"
        )
    report.append("")
    report.append("## Interpretação inicial")
    report.append("")
    report.append(
        f"A Godytec possui {total_leads} leads B2B simulados no funil comercial para consultórios odontológicos."
    )
    report.append(
        f"A taxa de conversão simulada é de {percent(conversion_rate)}, com {won_leads} leads ganhos."
    )
    report.append(
        f"A receita mensal potencial é de {money(potential_revenue)}, enquanto a receita mensal já ganha é de {money(won_revenue)}."
    )
    report.append(
        "As próximas análises devem comparar origem, campanha, etapa do pipeline e qualidade dos leads para identificar onde a Godytec deve concentrar esforço comercial."
    )
    report.append("")

    OUTPUT_PATH.write_text("\n".join(report), encoding="utf-8")
    print(f"Analysis report generated: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
