import os
import box.exceptions import BoxvalueError
import yaml
from src.endtoendmlflowproject.logging import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"reading the yaml file from {path_to_yaml}")
            return ConfigBox(content)
    except BoxvalueError:
        return ValueError
    except Exception as e:
        raise e
