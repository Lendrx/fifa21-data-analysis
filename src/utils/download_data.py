import os
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

def download_fifa_data():
    """
    Downloads FIFA 21 dataset from Kaggle and extracts it to the raw data directory.
    """
    try:
        # Initialize Kaggle API
        api = KaggleApi()
        api.authenticate()
        
        # Create raw data directory if it doesn't exist
        os.makedirs('data/raw', exist_ok=True)
        
        print("Downloading FIFA 21 dataset...")
        # Download the dataset
        api.dataset_download_files(
            'stefanoleone992/fifa-21-complete-player-dataset',
            path='data/raw'
        )
        
        print("Extracting downloaded files...")
        # Extract the zip file
        with zipfile.ZipFile('data/raw/fifa-21-complete-player-dataset.zip', 'r') as zip_ref:
            zip_ref.extractall('data/raw')
        
        # Remove the zip file
        os.remove('data/raw/fifa-21-complete-player-dataset.zip')
        
        print("Dataset successfully downloaded and extracted to data/raw/")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    download_fifa_data()