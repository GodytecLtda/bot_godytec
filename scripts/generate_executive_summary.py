from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/godytec_ghl_clinic_leads.csv")
ROI_REPORT_PATH = Path("analysis/003-campaign-roi-analysis.md")
OUTPUT_PATH = Path("analysis/004-executive-business-summary.md")
DEFAULT_CAMPAIGN_COST_BRL = 1500

CAMPAIGN_COSTS_BRL = {
    "Dental Growth BR - Facebook": 3500,
    "Implantes Agenda Cheia - Google": 4200,
    "Consultorios Premium - LinkedIn": 3000,
    "WhatsApp Automation Sprint": 1800,
    "Webinar Agenda Cheia": 1500,
    "Prospeccao Sudeste": 1200,
    "Reativacao Consultorios": 1000,
}


def money(value: float) -> str:
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def percent(value: float) -> str:
    return f"{value * 100:.2f}%"


def calculate_funnel_indicators(df: pd.DataFrame) -> dict[str, float]:
    total_leads = len(df)
    won_leads = int((df["lead_status"] == "Won").sum())
    lost_leads = int((df["lead_status"] == "Lost").sum())
    open_leads = int(df["lead_status"].isin(["Open", "Nurturing"]).sum())
    conversion_rate = won_leads / total_leads if total_leads else 0

    return {
        "total_leads": total_leads,
        "won_leads": won_leads,
        "lost_leads": lost_leads,
        "open_leads": open_leads,
        "conversion_rate": conversion_rate,
        "potential_monthly_revenue_brl": float(
            df["estimated_monthly_value_brl"].sum()
        ),
        "won_monthly_revenue_brl": float(
            df.loc[df["lead_status"] == "Won", "estimated_monthly_value_brl"].sum()
        ),
        "average_ticket_brl": float(df["estimated_monthly_value_brl"].mean()),
    }


def calculate_campaign_indicators(df: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for campaign_name, campaign_df in df.groupby("campaign_name"):
        total_leads = len(campaign_df)
        won_leads = int((campaign_df["lead_status"] == "Won").sum())
        cost = CAMPAIGN_COSTS_BRL.get(campaign_name, DEFAULT_CAMPAIGN_COST_BRL)
        won_revenue = float(
            campaign_df.loc[
                campaign_df["lead_status"] == "Won", "estimated_monthly_value_brl"
            ].sum()
        )
        potential_revenue = float(campaign_df["estimated_monthly_value_brl"].sum())
        conversion_rate = won_leads / total_leads if total_leads else 0
        estimated_roi = (won_revenue - cost) / cost if cost else 0

        rows.append(
            {
                "campaign_name": campaign_name,
                "total_leads": total_leads,
                "won_leads": won_leads,
                "potential_monthly_revenue_brl": potential_revenue,
                "won_monthly_revenue_brl": won_revenue,
                "simulated_campaign_cost_brl": cost,
                "conversion_rate": conversion_rate,
                "estimated_roi": estimated_roi,
            }
        )

    return pd.DataFrame(rows)


def campaign_sentence(row: pd.Series) -> str:
    return (
        f"{row['campaign_name']} "
        f"(ROI estimado de {percent(float(row['estimated_roi']))}, "
        f"receita ganha de {money(float(row['won_monthly_revenue_brl']))}, "
        f"receita potencial de {money(float(row['potential_monthly_revenue_brl']))})"
    )


def build_report(df: pd.DataFrame) -> str:
    funnel = calculate_funnel_indicators(df)
    campaigns = calculate_campaign_indicators(df)

    best_roi = campaigns.sort_values("estimated_roi", ascending=False).iloc[0]
    best_won_revenue = campaigns.sort_values(
        "won_monthly_revenue_brl", ascending=False
    ).iloc[0]
    best_potential_revenue = campaigns.sort_values(
        "potential_monthly_revenue_brl", ascending=False
    ).iloc[0]
    investment_recommendations = campaigns.sort_values(
        ["estimated_roi", "won_monthly_revenue_brl", "potential_monthly_revenue_brl"],
        ascending=False,
    ).head(3)
    review_recommendations = campaigns.sort_values(
        ["estimated_roi", "conversion_rate", "won_monthly_revenue_brl"],
        ascending=[True, True, True],
    ).head(3)

    roi_context = (
        f"Esta leitura considera tambem o relatorio de ROI ja gerado em {ROI_REPORT_PATH}."
        if ROI_REPORT_PATH.exists()
        else "Esta leitura recalcula os indicadores executivos diretamente a partir do CSV."
    )

    lines = []
    lines.append("# Resumo Executivo de Negocio - Godytec")
    lines.append("")
    lines.append("## Resumo executivo")
    lines.append("")
    lines.append(
        f"A Godytec possui {funnel['total_leads']} leads B2B simulados no funil comercial, "
        f"com {funnel['won_leads']} leads ganhos, {funnel['lost_leads']} perdidos e "
        f"{funnel['open_leads']} ainda abertos ou em nutricao."
    )
    lines.append(
        f"A conversao geral esta em {percent(float(funnel['conversion_rate']))}. "
        f"A oportunidade mensal mapeada chega a {money(float(funnel['potential_monthly_revenue_brl']))}, "
        f"enquanto a receita mensal ja ganha soma {money(float(funnel['won_monthly_revenue_brl']))}."
    )
    lines.append(roi_context)
    lines.append("")
    lines.append("## Diagnostico do funil comercial")
    lines.append("")
    lines.append(
        "O funil mostra uma base comercial relevante, mas ainda com grande parte das oportunidades em andamento. "
        f"Os {funnel['open_leads']} leads abertos ou em nutricao representam a principal frente de captura de valor no curto prazo."
    )
    lines.append(
        f"Com {funnel['won_leads']} negocios ganhos e ticket medio estimado de {money(float(funnel['average_ticket_brl']))}, "
        "a prioridade deve ser aumentar a velocidade de qualificacao e concentrar o time nas oportunidades com maior chance de fechamento."
    )
    lines.append("")
    lines.append("## Receita potencial e receita ganha")
    lines.append("")
    lines.append(
        f"A receita mensal potencial e de {money(float(funnel['potential_monthly_revenue_brl']))}. "
        f"A receita mensal ganha e de {money(float(funnel['won_monthly_revenue_brl']))}, "
        "o que indica espaco claro para transformar pipeline existente em receita recorrente."
    )
    lines.append(
        "A diferenca entre oportunidade potencial e receita capturada sugere que o maior ganho imediato nao depende apenas de gerar mais leads, "
        "mas de priorizar follow-up, proposta e negociacao nos leads ja existentes."
    )
    lines.append("")
    lines.append("## Performance das campanhas")
    lines.append("")
    lines.append(
        f"A melhor campanha por ROI estimado e {campaign_sentence(best_roi)}."
    )
    lines.append(
        f"A melhor campanha por receita ganha e {campaign_sentence(best_won_revenue)}."
    )
    lines.append(
        f"A melhor campanha por receita potencial e {campaign_sentence(best_potential_revenue)}."
    )
    lines.append("")
    lines.append("| Campanha | Leads | Ganhos | Conversao | Receita Potencial | Receita Ganha | ROI Estimado |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    for _, row in campaigns.sort_values("estimated_roi", ascending=False).iterrows():
        lines.append(
            "| "
            f"{row['campaign_name']} | "
            f"{int(row['total_leads'])} | "
            f"{int(row['won_leads'])} | "
            f"{percent(float(row['conversion_rate']))} | "
            f"{money(float(row['potential_monthly_revenue_brl']))} | "
            f"{money(float(row['won_monthly_revenue_brl']))} | "
            f"{percent(float(row['estimated_roi']))} |"
        )
    lines.append("")
    lines.append("## Campanhas recomendadas para investimento")
    lines.append("")
    for _, row in investment_recommendations.iterrows():
        lines.append(
            f"- {row['campaign_name']}: ampliar investimento de forma controlada, pois combina "
            f"ROI estimado de {percent(float(row['estimated_roi']))} com receita ganha de "
            f"{money(float(row['won_monthly_revenue_brl']))}."
        )
    lines.append("")
    lines.append("## Campanhas recomendadas para revisao")
    lines.append("")
    lines.append("Campanhas com menor ROI estimado:")
    for _, row in review_recommendations.iterrows():
        lines.append(
            f"- {row['campaign_name']}: revisar mensagem, oferta e criterio de qualificacao. "
            f"ROI estimado de {percent(float(row['estimated_roi']))}, conversao de "
            f"{percent(float(row['conversion_rate']))} e receita ganha de "
            f"{money(float(row['won_monthly_revenue_brl']))}."
        )
    lines.append("")
    lines.append("## Riscos e pontos de atencao")
    lines.append("")
    lines.append(
        "- A maior parte dos leads ainda esta aberta ou em nutricao; sem cadencia comercial consistente, parte dessa oportunidade pode esfriar."
    )
    lines.append(
        "- As campanhas possuem custos simulados, portanto a leitura de ROI deve orientar decisao inicial, nao substituir dados financeiros reais."
    )
    lines.append(
        "- Campanhas com alto volume precisam ser avaliadas junto com conversao e receita, para evitar crescimento sem qualidade comercial."
    )
    lines.append("")
    lines.append("## Recomendacoes praticas para a Godytec")
    lines.append("")
    lines.append(
        "- Direcionar o time comercial para os leads abertos com maior valor estimado e maior probabilidade de fechamento."
    )
    lines.append(
        "- Reforcar investimento nas campanhas com melhor ROI, mantendo acompanhamento semanal de receita ganha."
    )
    lines.append(
        "- Revisar campanhas de menor ROI antes de aumentar verba, ajustando publico, mensagem e oferta."
    )
    lines.append(
        "- Criar uma rotina de comparacao entre receita potencial, receita ganha e custo real por campanha."
    )
    lines.append("")
    lines.append("## Proximos passos sugeridos")
    lines.append("")
    lines.append(
        "1. Validar os custos simulados com valores reais de midia, producao e operacao comercial."
    )
    lines.append(
        "2. Priorizar follow-up dos leads abertos e em nutricao com maior ticket estimado."
    )
    lines.append(
        "3. Definir metas semanais por campanha para leads qualificados, propostas enviadas e fechamentos."
    )
    lines.append(
        "4. Atualizar o dataset com novos leads e rodar novamente a esteira para acompanhar evolucao do funil."
    )
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA_PATH)
    OUTPUT_PATH.write_text(build_report(df), encoding="utf-8")

    print(f"Executive business summary generated: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
