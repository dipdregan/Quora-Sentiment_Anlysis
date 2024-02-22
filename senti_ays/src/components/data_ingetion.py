import gdown
import zipfile
import os
from src.constant.constants import *
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.url = Data_URL
        self.ingested_dir = data_ingestion_config.data_ingestion_dir

    def download_and_unzip(self, output_folder):
        try:
            print("Downloading the data from Gdrive........")
            output_zip = os.path.join(output_folder, 'data.zip')
            gdown.download(self.url, output_zip, quiet=False)

            print("Unzip the downloaded file ........")
            with zipfile.ZipFile(output_zip, 'r') as zip_ref:
                zip_ref.extractall(output_folder)

            print(f"Remove the ZIP file after extraction {output_zip}.......")
            os.remove(output_zip)

            print("Data downloaded and unzipped successfully.")
            return output_folder

        except Exception as e:
            print(f"Error occurred during data ingestion: {e}")

    def initiate_data_ingestion(self):
        print("================ Data Ingestion Started ===========")
        os.makedirs(self.ingested_dir, exist_ok=True)
        output = self.download_and_unzip(self.ingested_dir)
        data_path = os.path.join(output, os.listdir(output)[0])
        print(os.listdir(data_path))

        data_files = os.listdir(data_path)

        # Define paths to the data files
        raw_data_file_path = None
        test_data_file_path = None
        actual_data_file_path = None

        # Iterate through the files in the extracted data folder and assign paths
        for file in data_files:
            if 'train' in file:
                raw_data_file_path = os.path.join(data_path, file)
            elif 'test' in file:
                test_data_file_path = os.path.join(data_path, file)
            elif 'sample_submission' in file:
                actual_data_file_path = os.path.join(data_path, file)

        artifact = DataIngestionArtifact(raw_data_file_path=raw_data_file_path,
                                          test_data_file_path=test_data_file_path,
                                          actual_data_file_path=actual_data_file_path)
        print(artifact)
        print("================= Data Ingestion Completed ==========")
        return artifact

if __name__ == "__main__":
    obj = DataIngestion(DataIngestionConfig())
    obj.initiate_data_ingestion()
