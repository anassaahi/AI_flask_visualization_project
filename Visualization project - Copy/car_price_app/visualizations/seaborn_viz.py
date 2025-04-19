import seaborn as sns
import matplotlib.pyplot as plt
import os
from data_processing import load_and_clean_data

def generate_seaborn_plots():
    df = load_and_clean_data('data.csv')
    output_dir = 'static/images/seaborn/'
    os.makedirs(output_dir, exist_ok=True)
    
    # Set seaborn style
    sns.set_style("whitegrid")
    plt.rcParams["figure.figsize"] = (10, 6)
    
    # Plot 1: Price Distribution with KDE
    plt.figure()
    sns.histplot(df['Price'], bins=30, kde=True, color='teal')
    plt.title("Price Distribution (in Lacs)")
    plt.xlabel("Price (Lacs)")
    plt.ylabel("Count")
    plt.savefig(f'{output_dir}price_distribution.png')
    plt.close()
    
    # Plot 2: Distance Distribution with KDE
    plt.figure()
    sns.histplot(df['Distance'], bins=30, kde=True, color='orchid')
    plt.title("Distance Driven (in Km)")
    plt.xlabel("Distance (Km)")
    plt.ylabel("Count")
    plt.savefig(f'{output_dir}distance_distribution.png')
    plt.close()
    
    # Plot 3: Price vs Distance by Fuel Type
    plt.figure()
    sns.scatterplot(data=df, x='Distance', y='Price', hue='Fuel Type', alpha=0.7)
    plt.title("Price vs Distance by Fuel Type")
    plt.xlabel("Distance (Km)")
    plt.ylabel("Price (Lacs)")
    plt.legend(title="Fuel Type", bbox_to_anchor=(1.05, 1))
    plt.savefig(f'{output_dir}price_vs_distance.png')
    plt.close()
    
    # Plot 4: Average Price by Fuel Type
    fuel_avg = df.groupby('Fuel Type')['Price'].mean().sort_values()
    plt.figure()
    sns.barplot(x=fuel_avg.index, y=fuel_avg.values, palette='plasma')
    plt.title("Average Price by Fuel Type")
    plt.ylabel("Average Price (Lacs)")
    plt.xlabel("Fuel Type")
    plt.savefig(f'{output_dir}avg_price_fuel.png')
    plt.close()
    
    # Plot 5: Transmission Type Distribution
    plt.figure()
    sns.countplot(data=df, y='Transmission Type', palette='pastel')
    plt.title("Transmission Type Distribution")
    plt.xlabel("Count")
    plt.ylabel("Transmission Type")
    plt.savefig(f'{output_dir}transmission_dist.png')
    plt.close()