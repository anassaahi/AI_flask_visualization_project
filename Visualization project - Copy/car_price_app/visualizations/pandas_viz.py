import pandas as pd
import matplotlib.pyplot as plt
import os
from data_processing import load_and_clean_data

def generate_pandas_plots():
    df = load_and_clean_data('data.csv')
    output_dir = 'static/images/pandas/'
    os.makedirs(output_dir, exist_ok=True)
    
    # Set style
    plt.style.use('ggplot')
    plt.rcParams["figure.figsize"] = (10, 6)
    
    # Plot 1: Price Distribution (Pandas Histogram)
    plt.figure()
    df['Price'].plot.hist(bins=30, color='blue', alpha=0.7)
    plt.title('Price Distribution (Pandas)')
    plt.xlabel('Price (Lacs)')
    plt.ylabel('Count')
    plt.savefig(f'{output_dir}price_distribution.png')
    plt.close()
    
    # Plot 2: Model Year Distribution (Pandas Bar Plot)
    plt.figure()
    df['Model'].value_counts().sort_index().plot.bar(color='green')
    plt.title('Cars per Model Year (Pandas)')
    plt.xlabel('Model Year')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.savefig(f'{output_dir}model_distribution.png')
    plt.close()
    
    # Plot 3: Scatter Matrix (Pandas)
    plt.figure()
    pd.plotting.scatter_matrix(df[['Price', 'Distance', 'Engine']], 
                             alpha=0.5, 
                             figsize=(12, 12),
                             diagonal='hist')
    plt.suptitle('Scatter Matrix (Pandas)')
    plt.savefig(f'{output_dir}scatter_matrix.png')
    plt.close()
    
    # Plot 4: Fuel Type Distribution (Pandas Pie Chart)
    plt.figure()
    df['Fuel Type'].value_counts().plot.pie(autopct='%1.1f%%', 
                                          colors=['#66b3ff','#99ff99','#ffcc99'],
                                          startangle=90)
    plt.title('Fuel Type Distribution (Pandas)')
    plt.ylabel('')
    plt.savefig(f'{output_dir}fuel_type_pie.png')
    plt.close()
    
    # Plot 5: Average Price by Transmission (Pandas Groupby Plot)
    plt.figure()
    df.groupby('Transmission Type')['Price'].mean().plot.bar(color=['#ff9999','#66b3ff'])
    plt.title('Average Price by Transmission (Pandas)')
    plt.xlabel('Transmission Type')
    plt.ylabel('Average Price (Lacs)')
    plt.savefig(f'{output_dir}avg_price_transmission.png')
    plt.close()