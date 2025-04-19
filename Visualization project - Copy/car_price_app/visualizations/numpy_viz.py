import numpy as np
import matplotlib.pyplot as plt
import os
from data_processing import load_and_clean_data

def generate_numpy_plots():
    df = load_and_clean_data('data.csv')
    output_dir = 'static/images/numpy/'
    os.makedirs(output_dir, exist_ok=True)
    
    # Set figure size and style
    plt.style.use('seaborn-v0_8-darkgrid')
    plt.rcParams["figure.figsize"] = (10, 6)
    
    # Plot 1: Price Histogram using NumPy
    plt.figure()
    prices = df['Price'].to_numpy()
    hist, bins = np.histogram(prices, bins=30)
    width = 0.9 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width, color='purple', alpha=0.7)
    plt.title('Price Distribution (NumPy)')
    plt.xlabel('Price (Lacs)')
    plt.ylabel('Frequency')
    plt.savefig(f'{output_dir}price_histogram.png')
    plt.close()
    
    # Plot 2: Distance vs Price Scatter with NumPy
    plt.figure()
    distance = df['Distance'].to_numpy()
    price = df['Price'].to_numpy()
    plt.scatter(distance, price, alpha=0.6, c=price, cmap='viridis')
    plt.colorbar(label='Price (Lacs)')
    plt.title('Distance vs Price (NumPy)')
    plt.xlabel('Distance (Km)')
    plt.ylabel('Price (Lacs)')
    plt.savefig(f'{output_dir}distance_price_scatter.png')
    plt.close()
    
    # Plot 3: Engine Size Heatmap using NumPy
    plt.figure()
    engine = df['Engine'].to_numpy()
    # Create 2D histogram (heatmap) of engine size vs price
    heatmap, xedges, yedges = np.histogram2d(engine, price, bins=20)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    plt.imshow(heatmap.T, extent=extent, origin='lower', aspect='auto', cmap='inferno')
    plt.colorbar(label='Frequency')
    plt.title('Engine Size vs Price Heatmap (NumPy)')
    plt.xlabel('Engine (CC)')
    plt.ylabel('Price (Lacs)')
    plt.savefig(f'{output_dir}engine_price_heatmap.png')
    plt.close()
    
    # Plot 4: Moving Average of Prices by Model Year using NumPy
    plt.figure()
    # Group by model year and calculate mean price
    model_price = df.groupby('Model')['Price'].mean().sort_index()
    years = model_price.index.to_numpy()
    prices = model_price.values
    
    # Calculate moving average with NumPy
    window_size = 3
    weights = np.ones(window_size) / window_size
    price_ma = np.convolve(prices, weights, mode='valid')
    years_ma = years[1:-1]  # Adjust years to match moving average length
    
    plt.plot(years, prices, 'o-', label='Original', alpha=0.6)
    plt.plot(years_ma, price_ma, 'r-', linewidth=2, label=f'{window_size}-Year Moving Avg')
    plt.title('Price Trend by Model Year with Moving Average (NumPy)')
    plt.xlabel('Model Year')
    plt.ylabel('Average Price (Lacs)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.savefig(f'{output_dir}price_moving_avg.png')
    plt.close()
    
    # Plot 5: Price Distribution by Fuel Type using NumPy
    plt.figure()
    fuel_types = df['Fuel Type'].unique()
    x_positions = np.arange(len(fuel_types))
    
    fuel_means = []
    fuel_std = []
    
    for fuel in fuel_types:
        fuel_prices = df[df['Fuel Type'] == fuel]['Price'].to_numpy()
        fuel_means.append(np.mean(fuel_prices))
        fuel_std.append(np.std(fuel_prices))
    
    plt.bar(x_positions, fuel_means, yerr=fuel_std, alpha=0.7, 
            capsize=10, color=plt.cm.Set3(np.linspace(0, 1, len(fuel_types))))
    plt.xticks(x_positions, fuel_types, rotation=45)
    plt.title('Price Mean and Standard Deviation by Fuel Type (NumPy)')
    plt.xlabel('Fuel Type')
    plt.ylabel('Price (Lacs)')
    plt.tight_layout()
    plt.savefig(f'{output_dir}fuel_price_stats.png')
    plt.close()