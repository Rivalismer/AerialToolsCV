#!/bin/sh

### -- set the job Name AND the job array --
#BSUB -J mask_rcnn_train

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
source ../rcnn_venv/bin/activate
module load matplotlib/3.6.0-numpy-1.23.3-python-3.9.14
module load numpy/1.23.3-python-3.9.14-openblas-0.3.21
module load opencv/4.6.0-python-3.9.14-cuda-11.8-without-cudnn
module load scipy/1.9.1-python-3.9.14
module load pandas/1.4.4-python-3.9.14

# Here follow the commands you want to execute
python3 detectron2/train.py