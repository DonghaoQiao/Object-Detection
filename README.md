# Object-Detection  
My Object Detection Playground  

Reference  
<https://github.com/hoya012/deep_learning_object_detection>

### Paper list from 2014 to now(2019)
<p align="center"><img width="600" src="/imgs/deep_learning_object_detection_history.jpg"></p>

### R-CNN: Region-based Convolutional Network  
[paper](https://arxiv.org/pdf/1311.2524.pdf)  
<p align="left"><img width="400" src="/imgs/R-CNN.jpg"></p>

Three modules:  
* Region proposals. Using **selective search** to enerate category-independent region proposals.  
* Feature extraction. Using CNN to extract a fixed-length feature vector from each region.  
* Object category classifiers. Using linear SVMs to classify features.  

### Fast R-CNN  
[paper](https://arxiv.org/pdf/1504.08083.pdf)  
Using a single-stage training algorithm to classify object proposals and refine their spatial locations simultaneously.  

### Faster R-CNN  
[paper](https://arxiv.org/pdf/1506.01497.pdf)  

### YOLO: You Only Look Once
### YOLOv1  
[paper](https://arxiv.org/pdf/1506.02640.pdf)  

### YOLOv2/YOLO9000  
[paper](https://arxiv.org/pdf/1612.08242.pdf)  

### YOLOv3  
[paper](https://arxiv.org/pdf/1804.02767.pdf)  

### SSD: Single Shot MultiBox Detector  
[paper](https://arxiv.org/pdf/1512.02325.pdf)  







