from flask import Flask, render_template
import os
import sys
from pathlib import Path
import pandas as pd
import re
import random

# Add the parent directory to Python path
sys.path.append(str(Path(__file__).parent))

# Initialize Flask app
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/images'

# Data processing functions
def load_and_clean_data(filepath='data.csv'):
    try:
        # Load data
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Data file not found at {filepath}")
            
        df = pd.read_csv(filepath)
        
        # Basic validation
        if df.empty:
            raise ValueError("Loaded an empty DataFrame")
            
        # Clean data
        df = diversify_cities(df)
        df['Distance'] = df['Distance'].apply(clean_mileage)
        df['Price'] = df['Price'].apply(clean_price)
        df['Engine'] = df['Engine'].apply(clean_engine)
        
        return df
        
    except Exception as e:
        print(f"Error in load_and_clean_data: {str(e)}")
        return None

def diversify_cities(df):
    if df is None:
        return None
        
    major_cities = ['Lahore', 'Karachi', 'Islamabad', 'Rawalpindi', 'Faisalabad', 'Multan', 'Peshawar', 'Quetta']
    minor_cities = ['Sialkot', 'Sargodha', 'Hyderabad', 'Gujranwala', 'Bahawalpur', 'Abbottabad', 'Mardan', 'Mirpur', 'Sukkur', 'Swat']
    
    all_cities = major_cities + minor_cities
    weights = [0.35] + [0.08]*(len(major_cities)-1) + [0.02]*len(minor_cities)
    weights = [w/sum(weights) for w in weights]
    
    df['City'] = random.choices(all_cities, weights=weights, k=len(df))
    return df

def clean_mileage(miles):
    try:
        cleaned = re.sub(r'[^\d]', '', str(miles))
        return int(cleaned) if cleaned.isdigit() else 0
    except:
        return 0

def clean_price(price):
    try:
        price = str(price).lower().replace('pkr', '').strip()
        if 'crore' in price:
            return float(re.sub(r'[^\d.]', '', price.replace('crore', '').strip())) * 100
        elif 'lac' in price or 'lacs' in price:
            return float(re.sub(r'[^\d.]', '', price.replace('lacs', '').replace('lac', '').strip()))
        return float(re.sub(r'[^\d.]', '', price))
    except:
        return 0.0

def clean_engine(engine):
    try:
        engine = str(engine).lower().strip()
        if 'cc' in engine:
            return float(re.sub(r'[^\d.]', '', engine.replace('cc', '')))
        elif 'kwh' in engine:
            return float(re.sub(r'[^\d.]', '', engine.replace('kwh', ''))) * 1000
        return float(re.sub(r'[^\d.]', '', engine))
    except:
        return 0.0

# Import only matplotlib visualization
from visualizations.matplotlib_viz import generate_matplotlib_plots
from visualizations.seaborn_viz import generate_seaborn_plots  # Add this line
from visualizations.pandas_viz import generate_pandas_plots
from visualizations.numpy_viz import generate_numpy_plots

def generate_all_visualizations():
    # First verify data loading works
    test_df = load_and_clean_data()
    if test_df is None:
        print("ERROR: Could not load and clean data. Check:")
        print("1. data.csv exists in the project root")
        print("2. The file has valid CSV content")
        print("3. The required columns exist in the data")
        return False
    
    # Generate only matplotlib plots
    try:
        generate_matplotlib_plots()
        generate_seaborn_plots()
        generate_pandas_plots()
        generate_numpy_plots()
        return True
    except Exception as e:
        print(f"Error generating visualizations: {str(e)}")
        return False
LIBRARIES = ['matplotlib', 'seaborn', 'pandas', 'numpy']  # Update this line
for lib in LIBRARIES:
    os.makedirs(f"{app.config['UPLOAD_FOLDER']}/{lib}", exist_ok=True)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/matplotlib')
def matplotlib_page():
    return render_template('libraries/matplotlib.html')

@app.route('/seaborn')  
def seaborn_page():
    return render_template('libraries/seaborn.html')

@app.route('/pandas')  
def pandas_page():
    return render_template('libraries/pandas.html')

@app.route('/numpy')  # Add this route
def numpy_page():
    return render_template('libraries/numpy.html')

if __name__ == '__main__':
    if generate_all_visualizations():
        app.run(debug=True)
    else:
        print("Failed to start application due to data loading issues")