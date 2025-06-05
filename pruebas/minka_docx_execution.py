# main.py
import pandas as pd
import os
from mecoda_minka import get_obs, get_dfs
from pruebas.utils import (
    get_main_metrics,
    build_monthly_metrics,
    get_taxon_counts,
    get_new_species,
    download_photos,
    get_photos_new_species,
    get_new_species_photo_snapshot, 
    plot_monthly_metrics,
    plot_top_species,
    plot_new_species,
    get_heatmap,
    get_minka_docx
)

PROJECT_ID = 264

if __name__ == '__main__':
    # Crear directorios necesarios
    os.makedirs("data", exist_ok=True)
    os.makedirs("figures", exist_ok=True)

    # Obtener datos iniciales
    observations = get_obs(id_project=PROJECT_ID, grade="research")
    df_obs, df_photos = get_dfs(observations)
    
    # Guardar observaciones y fotos
    df_obs.to_csv("data/observations.csv", index=False)
    df_photos.to_csv("data/photos.csv", index=False)

    # Generar métricas
    get_main_metrics(PROJECT_ID)
    df_monthly = build_monthly_metrics(PROJECT_ID)
    get_taxon_counts()
    get_new_species(df_obs, 30)
    #download_photos(df_photos,'minka_photos')
    df_new_species = pd.read_csv("data/new_species_photos.csv")
    download_photos(df_new_species, 'minka_photos_new_species')
    get_photos_new_species(df_new_species, df_photos)
    df_new_species = get_new_species_photo_snapshot(df_obs, df_photos, 30)


    # Cargar datos generados
    df_monthly = pd.read_csv("data/monthly_metrics.csv")
    df_taxon_count = pd.read_csv("data/taxon_counts.csv")
    df_main_metrics = pd.read_csv("data/main_metrics.csv")
    
    df_observations = pd.read_csv("data/observations.csv")

    # Generar gráficos
    for column in ['observations', 'observers', 'identifiers', 'species']:
        plot_monthly_metrics(df_monthly, column)

    for rank in ['kingdom', 'phylum', 'class', 'family', 'species']:
        plot_top_species(df_taxon_count, rank)

    for taxon in [None, 'animalia', 'aves', 'plantae', 'fungi']:
        get_heatmap(taxon)

    plot_new_species(df_new_species)

    # Generar informe
    get_minka_docx()

    print("Proceso completado. Informe generado en 'informe_mensual_minka.docx'")