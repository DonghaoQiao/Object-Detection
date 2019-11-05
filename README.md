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
* Using **selective search** to generate category-independent region proposals.  
* Using **CNN** to extract a fixed-length feature vector from each region.  
* Using **linear SVMs** to do classification.  

### Fast R-CNN  
[paper](https://arxiv.org/pdf/1504.08083.pdf)  
<p align="left"><img width="300" src="/imgs/Fast-R-CNN.jpg"></p>

* Using **selective search** to generate category-independent region proposals.  
* Using **CNN** and max pooling layers to produce a conv feature map.  
* Using **Region of Interests(RoI)** poolin to extract a fixed-length feature vector from the feature map.  
* Using **Softmax** to do classification.  

### Faster R-CNN  
[paper](https://arxiv.org/pdf/1506.01497.pdf)  
<p align="left"><img width="200" src="/imgs/Faster-R-CNN.jpg"></p>

* Using **Region Proposal Networks(RPNs)** to compute region proposals.  
* Using **CNN** and max pooling layers to produce a conv feature map.  
* Using **Region of Interests(RoI)** poolin to extract a fixed-length feature vector from the feature map.  

### YOLO: You Only Look Once
### YOLOv1  
[paper](https://arxiv.org/pdf/1506.02640.pdf)  

### YOLOv2/YOLO9000  
[paper](https://arxiv.org/pdf/1612.08242.pdf)  

### YOLOv3  
[paper](https://arxiv.org/pdf/1804.02767.pdf)  

### SSD: Single Shot MultiBox Detector  
[paper](https://arxiv.org/pdf/1512.02325.pdf)  







