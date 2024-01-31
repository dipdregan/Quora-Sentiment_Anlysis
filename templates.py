import os
from pathlib import Path

project_name = 'senti_ays'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"{project_name}/src/__init__.py",
    f"{project_name}/src/constant/__init__.py",
    f"{project_name}/src/constant/constants.py",
    f"{project_name}/src/entity/config_entity.py",
    f"{project_name}/src/entity/artifact_entity.py",
    f"{project_name}/src/components/__init__.py",
    f"{project_name}/src/components/data_ingetion.py",
    f"{project_name}/src/components/data_validation.py",
    f"{project_name}/src/components/data_trasnformation.py",
    f"{project_name}/src/components/model_trainer.py",
    f"{project_name}/src/components/model_evaluation.py",
    f"{project_name}/src/pipeline/__init__.py",
    f"{project_name}/src/pipeline/data_pipeline.py",
    f"{project_name}/src/pipeline/model_pipeline.py",
    f"{project_name}/src/logging.py",
    f"{project_name}/src/exception.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    
    "setup.py",
    "model/.gitkeep",
    "templates/index.html",
    "init_setup.sh",
]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
    else:
        print(f"{filepath} already exists")