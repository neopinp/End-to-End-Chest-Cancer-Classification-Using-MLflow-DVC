# utility related code 
# functionality frequently used 
import os 
import yaml
from src.cnnClassifier import logger
import json
import joblib 
from ensure import ensure_annotations
from box import ConfigBox, BoxError 
from pathlib import Path
from typing import Any 
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns 

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns: ConfigBox: ConfigBox type 
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe.load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """ create list of directories 

    Args: 
        path_to_directories (list): list of path directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent = 4)

    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)
    """ Returns: 
            ConfigBox: data as class attributes instead of dict 
    """
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations # save as a binary object 
def save_bin(data: Any, path: Path):
    # save binary file 
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations # load binary object 
def load_bin(path: Path) -> Any: 
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data 

@ensure_annotations # get size of file
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

@ensure_annotations
def decodeImage(imgstring, fileName): 
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64decode(f.read())

# image uploaded by user encodes to base 64, decodes image, 
# converts to JPC format, predicts, converts back to base64
# can't pass image directly 