# main.py
import pandas as pd
import os
from mecoda_minka import get_obs, get_dfs
from utils import (
    get_main_metrics,
    build_monthly_metrics,
    get_taxon_counts,
    get_new_species_photo_snapshot,
    plot_monthly_metrics,
    plot_top_species,
    get_heatmap,
    get_minka_docx
)

figures_path = os.path.join('figures')

monthly_metrics_path = 'data/monthly_metrics.csv'
observations_path = 'data/observations.csv'
new_species_path = 'data/new_species_photo.csv'
taxon_counts_path = 'data/taxon_counts.csv'

# DATA LOADING

df_monthly = pd.read_csv(monthly_metrics_path)
df_new_species = pd.read_csv(new_species_path)
df_taxon_count = pd.read_csv(taxon_counts_path)
df_observations = pd.read_csv(observations_path)

PROJECT_ID = 264
LAST_DAYS = 30    

observations = get_obs(id_project=264, grade="research")
df_obs, df_photos = get_dfs(observations)

# MAIN METRICS
get_main_metrics(PROJECT_ID)

# MONTHLY METRICS
df_monthly = build_monthly_metrics(PROJECT_ID)

# TAXON_COUNT
get_taxon_counts()

# NEW SPECIEES PHOTOS
df_new_species = get_new_species_photo_snapshot(df_obs, df_photos, LAST_DAYS)

# PLOT MONTHLY METRICS
for column in ['observations', 'observers', 'identifiers', 'species']:
    plot_monthly_metrics(df_monthly, column)

# PLOT TAXON RANKS
for rank in ['kingdom', 'phylum', 'class', 'family', 'species']:
    plot_top_species(df_taxon_count, rank)

# PLOT HEATMAPS
for taxon in [None, 'Animalia', 'Aves', 'Plantae', 'Fungi']:
    get_heatmap(taxon)

# GENERACIÓN INFORME 
get_minka_docx()

print("Proceso completado. Informe generado en 'informe_mensual_minka.docx'")