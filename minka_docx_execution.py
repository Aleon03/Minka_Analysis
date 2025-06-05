# main.py
import pandas as pd
import os
from mecoda_minka import get_obs, get_dfs
from utils import (
    init_directories,
    get_main_metrics,
    build_monthly_metrics,
    get_taxon_counts,
    get_new_species,
    get_photos_new_species,
    get_new_species_photo_snapshot,
    
    plot_monthly_metrics,
    plot_new_species,
    plot_top_species,
    get_heatmap,
    get_minka_docx
)

def check_file(path):
    if os.path.exists(path):
        print(f" Archivo generado: {path}")
    else:
        print(f" Archivo NO generado: {path}")

if __name__ == '__main__':
    init_directories()

    # Crear directorios necesarios
    os.makedirs("data", exist_ok=True)
    os.makedirs("figures", exist_ok=True)
    os.makedirs("figures/monthly_metrics", exist_ok=True)
    os.makedirs("figures/photos_new_species", exist_ok=True)
    os.makedirs("figures/taxon_plots", exist_ok=True)
    os.makedirs("figures/heatmap_plots", exist_ok=True)
    os.makedirs("minka_photos", exist_ok=True)
    os.makedirs("minka_photos_new_species", exist_ok=True)

    # Obtener datos iniciales
    observations = get_obs(id_project=264, grade="research")
    df_obs, df_photos = get_dfs(observations)
    df_obs.to_csv("data/observations.csv", index=False)
    df_photos.to_csv("data/photos.csv", index=False)

    check_file("data/observations.csv")
    check_file("data/photos.csv")

    get_main_metrics(264)
    check_file("data/main_metrics.csv")

    df_monthly = build_monthly_metrics(264)
    check_file("data/monthly_metrics.csv")

    get_taxon_counts()
    check_file("data/taxon_counts.csv")

    new_spe = get_new_species(df_obs)
    df_new_species = get_new_species(df_obs, last_days=30)
    get_photos_new_species(df_new_species, df_photos)
    check_file("data/new_species_only_photos.csv")

    df_new_species_plot = get_new_species_photo_snapshot(df_obs, df_photos)
    check_file("data/new_species_photo.csv")

    print('\n Generación de datos completada.\n')

    # ------------------------- GRÁFICOS -----------------------------

    print('📊 Inicio creación de gráficos.')

    paths = {
        'monthly': 'data/monthly_metrics.csv',
        'observations': 'data/observations.csv',
        'new_species_only_photos': 'data/new_species_only_photos.csv',
        'new_species_photo': 'data/new_species_photo.csv',
        'taxon_counts': 'data/taxon_counts.csv',
        'main_metrics': 'data/main_metrics.csv'
    }

    # Verifica que todos los archivos existen antes de cargar
    for name, path in paths.items():
        if not os.path.exists(path):
            print(f" FALTA archivo requerido: {path}")
            exit(1)

    # Cargar datos
    df_monthly = pd.read_csv(paths['monthly'])
    df_new_species = pd.read_csv(paths['new_species_only_photos'])
    df_new_species_plot = pd.read_csv(paths['new_species_photo'])
    df_taxon_count = pd.read_csv(paths['taxon_counts'])
    df_observations = pd.read_csv(paths['observations'])
    df_main_metrics = pd.read_csv(paths['main_metrics'])

    plot_monthly_metrics(df_monthly, 'species')
    plot_monthly_metrics(df_monthly, 'observations')
    plot_monthly_metrics(df_monthly, 'observers')
    plot_monthly_metrics(df_monthly, 'identifiers')

    plot_new_species(df_new_species_plot)

    for rank in ['kingdom', 'phylum', 'class', 'species', 'family']:
        plot_top_species(df_taxon_count, rank)

    for taxon in [None, 'plantae', 'fungi', 'animalia', 'aves']:
        get_heatmap(taxon)

    print('\n Gráficos generados correctamente.\n')

    # ------------------------ DOCX -------------------------------

    print('📄 Inicio creación del informe en formato DOCX.')

    try:
        get_minka_docx(df_main_metrics, df_new_species_plot)
        check_file("informe_mensual_minka.docx")
        print('\n Informe en formato DOCX generado correctamente.\n')
    except Exception as e:
        print(f" Error al generar el informe DOCX: {e}")

    print(' Proceso completado.')


    


