import os
import requests
import pandas as pd

def extract():
    url="https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def transform(data):
    df = pd.json_normalize(data)
    df = df[['name', 'email','address.city']]
    df.columns = ['full_name','email','city']
    df['email'] = df['email'].str.lower()
    return df

def load(df, path="output/users.parquet"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_parquet(path, index=False)
    print(f"File save in: {path}")

def main():
    raw_data = extract()
    clean_df = transform(raw_data)
    load(clean_df)


if __name__ == "__main__":
    main()