# Object-Detection  
My Object Detection Playground  

Reference  
<https://github.com/hoya012/deep_learning_object_detection>  
<https://github.com/amusi/awesome-object-detection>  
[Deep Learning for Generic Object Detection: A Survey](https://arxiv.org/pdf/1809.02165v1.pdf)

### Paper list from 2014 to now(2019)
<p align="center"><img width="600" src="/imgs/deep_learning_object_detection_history.jpg"></p>

### R-CNN: Region-based Convolutional Network  
[paper](https://arxiv.org/pdf/1311.2524.pdf)  
<p align="left"><img width="400" src="/imgs/R-CNN.jpg"></p>

* Using **Selective Search** to extract category-independent region proposals.  
* Using **CNN** to extract a fixed-length feature vector from each region.  
* Using **Linear SVMs** to do classification.  
* Using **Fine Tuning** to do **Bounding Box Regression**.  

### Fast R-CNN  
[paper](https://arxiv.org/pdf/1504.08083.pdf)  
<p align="left"><img width="300" src="/imgs/Fast-R-CNN.jpg"></p>

* Using **selective search** to extract region proposals.  
* Using **CNN** and max pooling layers to produce a conv feature map.  
* Using **Region of Interests(RoI)** poolin to extract a fixed-length feature vector(6*6) from the feature map.  
* Using **Softmax** to do classification.  
Using **Fine Tuning** to do **Bounding Box Regression**.  

### Faster R-CNN  
[paper](https://arxiv.org/pdf/1506.01497.pdf)  
<p align="left"><img width="200" src="/imgs/Faster-R-CNN.jpg"></p>

* Using **Region Proposal Networks(RPNs)** to extract region proposals.  
* Using **CNN** and max pooling layers to produce a conv feature map.  
* Using **RoI** pooling to extract a fixed-length feature vector(6*6) from the feature map.  
* Using **Softmax** to do classification.  
Using **Fine Tuning** to do **Bounding Box Regression**.  

### YOLO: You Only Look Once
### YOLOv1  
[paper](https://arxiv.org/pdf/1506.02640.pdf)  

### YOLOv2/YOLO9000  
[paper](https://arxiv.org/pdf/1612.08242.pdf)  

### YOLOv3  
[paper](https://arxiv.org/pdf/1804.02767.pdf)  

### SSD: Single Shot MultiBox Detector  
[paper](https://arxiv.org/pdf/1512.02325.pdf)  







