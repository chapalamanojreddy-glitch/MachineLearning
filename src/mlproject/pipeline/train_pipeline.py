from mlproject.components.data_ingenstion import DataIngestion
from mlproject.components.data_transformation import DataTransformation


def main():
    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()

    transformation = DataTransformation()
    transformation.initiate_data_transformation(train_path, test_path)


if __name__ == "__main__":
    main()