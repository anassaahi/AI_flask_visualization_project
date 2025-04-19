import pandas as pd
import re
import random
import os

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