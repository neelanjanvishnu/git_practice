#!/usr/bin/env Rscript

suppressPackageStartupMessages({
  library(ggplot2)
  library(dplyr)
})

# Embedded data for the upregulated pathways and their p-values
pathway_df <- tibble::tibble(
  Pathway = c(
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
    "3-Beta-Hydroxysteroid Dehydrogenase Deficiency"
  ),
  p_value = c(
    0.000661,
    0.00293,
    0.00633,
    0.0139,
    0.0343,
    0.00157,
    0.0085,
    0.00876,
    0.0123,
    0.0137,
    3.21e-05,
    0.00404,
    0.00541,
    0.0118,
    0.044,
    3.02e-06,
    6.05e-06,
    7.11e-06,
    2.39e-05,
    0.000416,
    0.000729,
    0.000862,
    0.00104,
    0.00137,
    3.02e-06,
    3.02e-06,
    3.02e-06,
    3.02e-06,
    3.02e-06
  )
) %>%
  arrange(p_value)

# Determine dynamic x-axis limit consistent with the Python script
x_max <- -log10(min(pathway_df$p_value)) + 1

plot <- ggplot(pathway_df, aes(x = -log10(p_value), y = reorder(Pathway, p_value))) +
  geom_point(color = "red", size = 2) +
  labs(
    x = "-log10(p-value)",
    y = "Pathway",
    title = "Upregulated Pathway Enrichment"
  ) +
  coord_cartesian(xlim = c(0, x_max)) +
  theme_minimal(base_size = 12) +
  theme(
    panel.grid.major.y = element_blank(),
    panel.grid.minor = element_blank()
  )

print(plot)

ggsave(
  filename = "upregulated_pathway_dotplot.svg",
  plot = plot,
  width = 9,
  height = 10,
  dpi = 300,
  units = "in"
)
