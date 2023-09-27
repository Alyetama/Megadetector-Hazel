# Megadetector-Hazel
Running Megadetector 5 jobs on Hazel (NCSU's HPC)

## Setup

### Connect to your cloud storage account (run only once)

- Here, we will use `Google Drive` as an example, but you can use any cloud storage listed [here](https://rclone.org/docs/).

```sh
./rclone config
# >>>> Prompt responses:
# n/s/q> n
# name> gdrive
# Storage> drive
# client_id> leave empty
# client_secret> leave empty
# scope> 1
# root_folder_id> leave empty
# service_account_file> leave empty
# y/n> n
# y/n> n
# COPY THE URL IN THE OUTPUT, AND OPEN IT IN YOUR BROWSER TO LOG IN...
#     ...THEN COPY THE CODE THAT WILL SHOW UP
# config_verification_code> PASTE THE CODE YOU COPIED HERE
# y/n> n
# y/e/d> y
# e/n/d/r/c/s/q> q
```

### Clone this repo

```sh
git clone https://github.com/Alyetama/Megadetector-Hazel.git
cd Megadetector-Hazel
git clone https://github.com/ultralytics/yolov5.git

module load conda
conda create -n yolov5 python=3.8 --yes
conda activate yolov5
pip install -r yolov5/requirements.txt
```

## Run
```sh
PARENT_DIRECTORY="REPLACE_WITH_DIR_PATH"
REMOTE="REPLACE_WITH_FULL_REMOTE_PATH"

bsub -env "PARENT_DIRECTORY=$PARENT_DIRECTORY, REMOTE=$REMOTE" < predict.sh
```
