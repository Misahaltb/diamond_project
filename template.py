import os
from pathlib import Path


list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/__init__.py",
    "src/components/model_evaluation.py",  # Corrected spelling
    "src/pipeline/__init__.py",  # Corrected spelling
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction.py",
    "src/utils/utils.py",
    "tests/utils/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        
    
    
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filename,"w") as f:
            pass

