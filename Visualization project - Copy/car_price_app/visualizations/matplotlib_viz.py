import matplotlib.pyplot as plt
import os
from data_processing import load_and_clean_data

def generate_matplotlib_plots():
    df = load_and_clean_data('data.csv')
    output_dir = 'static/images/matplotlib/'
    os.makedirs(output_dir, exist_ok=True)
    
    # Set style
    plt.style.use('ggplot')
    plt.rcParams["figure.figsize"] = (10, 6)
    
    # Plot 1: Price Distribution
    plt.figure()
    plt.hist(df['Price'], bins=30, color='blue', alpha=0.7)
    plt.title('Price Distribution (in Lacs)')
    plt.xlabel('Price (Lacs)')
    plt.ylabel('Count')
    plt.savefig(f'{output_dir}price_distribution.png')
    plt.close()
    
    # Plot 2: Distance Distribution
    plt.figure()
    plt.hist(df['Distance'], bins=30, color='green', alpha=0.7)
    plt.title('Distance Driven (in Km)')
    plt.xlabel('Distance (Km)')
    plt.ylabel('Count')
    plt.savefig(f'{output_dir}distance_distribution.png')
    plt.close()
    
    # Plot 3: Engine Size Distribution
    plt.figure()
    plt.hist(df['Engine'], bins=30, color='red', alpha=0.7)
    plt.title('Engine Size (in CC)')
    plt.xlabel('Engine (CC)')
    plt.ylabel('Count')
    plt.savefig(f'{output_dir}engine_distribution.png')
    plt.close()
    
    # Plot 4: Price vs Distance
    plt.figure()
    plt.scatter(df['Distance'], df['Price'], alpha=0.5)
    plt.title('Price vs Distance')
    plt.xlabel('Distance (Km)')
    plt.ylabel('Price (Lacs)')
    plt.savefig(f'{output_dir}price_vs_distance.png')
    plt.close()
    
    # Plot 5: Fuel Type Distribution
    fuel_counts = df['Fuel Type'].value_counts()
    plt.figure()
    plt.pie(fuel_counts, labels=fuel_counts.index, autopct='%1.1f%%')
    plt.title('Fuel Type Distribution')
    plt.savefig(f'{output_dir}fuel_type_pie.png')
    plt.close()