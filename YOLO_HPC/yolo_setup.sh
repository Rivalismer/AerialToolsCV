#!/bin/sh

### -- set the job Name AND the job array --
#BSUB -J yolo_retrain

### –- specify queue --
#BSUB -q gpuv100

### -- ask for number of cores (default: 1) --
#BSUB -n 4

### -- Select the resources: 1 gpu in exclusive process mode --
#BSUB -gpu "num=1:mode=exclusive_process"

### -- allocate hosts --
#BSUB -R "span[hosts=1]"

### -- set walltime limit: hh:mm --
#BSUB -W 24:00

### -- specify that we need 4GB of memory per core/slot --
#BSUB -R "rusage[mem=4GB]"

### -- kill if each core surpasses 5 GB --
#BSUB -M 5GB

### -- send notification at start --
#BSUB -B

### -- send notification at completion--
#BSUB -N

### -- Specify the output and error file. %J is the job-id --
### -- -o and -e mean append, -oo and -eo mean overwrite --
#BSUB -o Output_%J.out
#BSUB -e Output_%J.err

### -- Load Modules --
source ../yolo_venv/bin/activate
module load matplotlib/3.6.0-numpy-1.23.3-python-3.9.14
module load numpy/1.23.3-python-3.9.14-openblas-0.3.21
module load opencv/4.6.0-python-3.9.14-cuda-11.8-without-cudnn
module load scipy/1.9.1-python-3.9.14
module load pandas/1.4.4-python-3.9.14

# here follow the commands you want to execute
# Program_name_and_options - weight/train path is relative to shell script
python3 yolov7/train.py --epochs 100 --workers 4 --device 0 --batch-size 16 \
--data data/pv.yaml --img 640 640 --cfg cfg/training/yolov7_pv.yaml \
--weights 'yolov7/yolov7_training.pt' --name yolov7_pv_fixed_res --hyp data/hyp.scratch.custom.yaml