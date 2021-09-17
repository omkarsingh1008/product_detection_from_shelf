# product_detection_from_shelf
Object Detector to detect the products present on the shelf.

## problem 
Given a grocery store shelf image, detect all products present in the shelf image.

## data collection & preparation
I collect dataset from [this](https://github.com/gulvarol/grocerydataset) repo.
for data prepration I crate one script which convert data into yolo format means(.txt file which have label coodinate).
example:-1 0.514545 0.412568 0.440000 0.792350 (label x_center y_center width  height)

# train
For training. I used yolov5m PyTorch. m instance for medium.
yolov5 have different model-like small, medium and large 

we need 3 files to train yolov5 model

1. data.yaml:- data related information
2. yolov5m.yaml:- it's a configuration file
3. (optional) yolov5m.pt:- it's weight file

yolov5m.pt file is used for transfer learning.

train model on 300 epochs and the batch size is 2
```bash
python train.py --img 416 --batch 2 --epochs 300 --data data.yaml --weights yolov5m.pt --cfg yolov5m.yaml
```
## hyper-prameters
 I use default hyper-prameters.

## results
after 300 epoch we get 0.60 mAP (mean aevrage percision)
![alt text](https://github.com/omkarsingh1008/product_detection_from_shelf/blob/main/model_training_files/runs/train/exp/results.png)

## examples
![alt text](https://github.com/omkarsingh1008/product_detection_from_shelf/blob/main/results/images_with_detections/exp/C4_P02_N4_S2_1.JPG)

## setup 

setup on loacl machine.

Clone repo and install requirements.txt in a Python>=3.6.0 environment, including PyTorch>=1.7.
```bash
git clone https://github.com/omkarsingh1008/product_detection_from_shelf.git
```
```bash
cd Street_light-laptop_detection
```

```bash
pip install -r requirements.txt
```
## demo
demo on video

```bash
python3 detect.py --weight best.pt --source video_path
```
demo on image
```bash
python3 detect.py --weight best.pt --source image_path
```

demo on webcam
```bash
python3 detect.py --weight best.pt --source 0
```
