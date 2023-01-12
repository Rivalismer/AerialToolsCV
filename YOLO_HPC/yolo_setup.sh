#!bin/sh

### -- set the job Name AND the job array --
#BSUB -J yolo_retrain

### –- specify queue -- 
#BSUB -q hpc 

### -- ask for number of cores (default: 1) --
#BSUB -n 6

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
python -m pip install requirements_gpu.txt
python -m pip install requirements.txt

# here follow the commands you want to execute 
# Program_name_and_options
./python train.py --epochs 100 --workers 4 --device 0 --batch-size 16 --data data/pv.yaml \
--img 640 640 --cfg cfg/training/yolov7_pv.yaml --weights 'yolov7_training.pt' \
--name yolov7_pv_fixed_res --hyp data/hyp.scratch.custom.yaml