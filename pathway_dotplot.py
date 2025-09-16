import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Embedded data for upregulated pathways and their p-values
DATA = {
    "Pathway": [
        "Signaling by Non-Receptor Tyrosine Kinases",
        "Tryptophan catabolism",
        "Alanine and aspartate metabolism",
        "Metabolism of amino acids and derivatives",
        "Selenoamino acid metabolism",
        "Glycerolipids and glycerophospholipids",
        "Glycerophospholipid biosynthesis",
        "Phosphatidylethanolamine Biosynthesis",
        "Phospholipid metabolism",
        "Phosphatidylcholine Biosynthesis",
        "Transport of nucleotide sugars",
        "Biomarkers for pyrimidine metabolism disorders",
        "Pyrimidine catabolism",
        "Nucleotide catabolism",
        "Pyrimidine metabolism and related diseases",
        "Apparent mineralocorticoid excess syndrome",
        "Defective SLC35A2 causes congenital disorder of glycosylation 2M (CDG2M)",
        "Keratan sulfate biosynthesis",
        "PTK6 Expression",
        "Kennedy pathway from sphingolipids",
        "Synthesis of ceramides and 1-deoxyceramides",
        "Sphingolipid pathway",
        "Sphingolipid metabolism",
        "Sphingolipid metabolism overview",
        "Steroidogenesis",
        "11-beta-hydroxylase deficiency (CYP11B1)",
        "17-alpha-hydroxylase deficiency (CYP17)",
        "21-hydroxylase deficiency (CYP21)",
        "3-Beta-Hydroxysteroid Dehydrogenase Deficiency",
    ],
    "p-value": [
        6.61e-4,
        2.93e-3,
        6.33e-3,
        1.39e-2,
        3.43e-2,
        1.57e-3,
        8.50e-3,
        8.76e-3,
        1.23e-2,
        1.37e-2,
        3.21e-5,
        4.04e-3,
        5.41e-3,
        1.18e-2,
        4.40e-2,
        3.02e-6,
        6.05e-6,
        7.11e-6,
        2.39e-5,
        4.16e-4,
        7.29e-4,
        8.62e-4,
        1.04e-3,
        1.37e-3,
        3.02e-6,
        3.02e-6,
        3.02e-6,
        3.02e-6,
        3.02e-6,
    ],
}


def plot_enriched_categories(df: pd.DataFrame, title: str, filename: str) -> None:
    """Plot a dot plot for the supplied pathway enrichment results."""
    df_sorted = df.sort_values(by="p-value", ascending=True)

    plt.figure(figsize=(9, 10), dpi=300)
    sns.scatterplot(
        y=df_sorted["Pathway"],
        x=-np.log10(df_sorted["p-value"]),
        color="red",
        edgecolor="red",
        s=30,
    )
    plt.xlabel("-log10(p-value)", fontsize=12)
    plt.ylabel("Pathway", fontsize=12)
    plt.title(title, fontsize=14)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=9)
    max_xlim = -np.log10(df_sorted["p-value"].min()) + 1
    plt.xlim(0, max_xlim)
    plt.grid(axis="x", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.savefig(filename, format="svg")
    plt.show()


def main() -> None:
    df_pathways = pd.DataFrame(DATA).dropna(subset=["p-value"])
    plot_enriched_categories(
        df_pathways,
        "Upregulated Pathway Enrichment",
        "upregulated_pathway_dotplot.svg",
    )


if __name__ == "__main__":
    main()
