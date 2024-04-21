import os
import box.exceptions import BoxValueError
from ensure import ensure_annotations
import yaml
from cnnClassifier import logger
import joblib
import json
from pathlib import Path


# Defining util functions as needed.

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    '''
    reads yaml file and returns ConfixBox output which makes it easy to access keys as methods.

    Args:
        path_to_yaml : path like input
    Raises:
        ValueError if yaml_file is empty
     Returns:
        ConfigBox : ConfigBox type
    '''
    try:
        with open(path_to_yaml) as file_read:
            content = yaml.safe_load(file_read)
            logger.info(f"yaml file {path_to_yaml} is loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    '''
    creates list of directories
    
    Args:
        path_to_directories (list): list of path of directories
        verbose (boolean): for logs. Defaults to True
    
    '''  

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)

        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """

    with open(path, "w") as file_write:
        json.dump(data, file_write, indent=4)

        logger.info(f"json file saved at {path}") 
    
