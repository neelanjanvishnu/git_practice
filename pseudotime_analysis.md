# Pseudotime Trajectory Analysis for scRNA-seq

This document outlines steps to perform pseudotime trajectory analysis on a single-cell RNA-seq dataset using R and the `Monocle3` package.

## 1. Pre-processing
1. Load your gene expression matrix and cell metadata.
2. Create a `cell_data_set` object.
3. Normalize and preprocess the data (e.g., using `log_normalize` and `preprocess_cds`).
4. Perform dimensionality reduction (PCA, UMAP).

```R
library(monocle3)
# assume `expr_matrix`, `cell_metadata`, and `gene_annotation` loaded
cds <- new_cell_data_set(expr_matrix,
                         cell_metadata = cell_metadata,
                         gene_metadata = gene_annotation)
cds <- preprocess_cds(cds, num_dim = 50)
cds <- reduce_dimension(cds)
cds <- cluster_cells(cds)
cds <- learn_graph(cds)
```

## 2. Ordering cells
Identify root or starting cells and order cells along trajectories.

```R
# choose cells that represent the start of differentiation
cds <- order_cells(cds, root_cells = c("cell_id1", "cell_id2"))
```

## 3. Visualize pseudotime

```R
plot_cells(cds, color_cells_by = "pseudotime")
```

This will color the UMAP plot by pseudotime values, showing the progression of cells along inferred trajectories.

## 4. Differential expression along pseudotime
Use `graph_test` or `fit_models` to find genes whose expression changes over pseudotime.

```R
pseudotime_de <- graph_test(cds, neighbor_graph="principal_graph")
```

## 5. Save results
Save pseudotime values and plots for downstream analysis or visualization.
