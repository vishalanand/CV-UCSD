## Computer Vision - University of California SantaCruz, Stanford University

### Localization of humans, the first step

We, Team TuringTested, are working on pose estimation of humans in a video clip. 

The first step would be to localize them in a frame. This can be done by an automated algorithm called HOG prediction. Please find the implementation of the algorithm for a video clip [here](https://github.com/vishalanand/CV-UCSD/tree/master/HOG_Video). We have calculated the confidence of the algorithm which has been carried out for images on three different datasets : [Fudan Pedestrian Dataset](http://www.cis.upenn.edu/~jshi/ped_html/), [Penn Pedestrian Dataset](http://www.cis.upenn.edu/~jshi/ped_html/) and the [Caltech Dataset](http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/). The image HOG prediction algorithms with confidence values are carried out [here](https://github.com/vishalanand/CV-UCSD/tree/master/HOG_Image).

The HPU setup is hosted [here](http://vishalanand.pythonanywhere.com/) with the 4024 images of Caltech Dataset, which queries images from [here](http://vishalanand.net/CV_UCSD_images/). (N.B. The images name have to be preserved to query the images correctly.)

### DATASET INFORMATION

* The Fundan dataset consists of 74 images
* The PennPed consists of 96 images.
* The Caltech consists of 4024 images.

The dataset images and its annotations can be found [here](https://github.com/vishalanand/CV-UCSD/tree/master/Dataset/). We now present the procedure we followed to get the results.  

### CPU ALGORITHM


The first step in the pipeline was to calculate the bounding box using an automated CPU algorithm. As mentioned, we used the HOG prediction algorithm to get the bounding boxes with the confidence value (SVM prediction).

### HPU EXPERIMENTS

There were four HPU experiments conducted and the description is as follows:
* [HPU1](http://vishalanand.pythonanywhere.com/hpu1): Draw the bounding boxes without any prior CPU algorithm.
* [HPU2](http://vishalanand.pythonanywhere.com/hpu2): Given a CPU algorithm, Click on all detected bounding boxes that do not contain pedestrians. It aims towards reducing the number of false positives
* [HPU3](http://vishalanand.pythonanywhere.com/hpu3): Given a CPU prediction, Locate and draw bounding boxes around pedestrians that have NOT been detected. By doing this, we can increase the number of true positive and reduce the number of false negative.
* [HPU4](http://vishalanand.pythonanywhere.com/hpu4): Given a CPU algorithm, click on objects not enclosed by bounding box. Then, the CPU chooses the bounding box from the predicted boxes below the threshold to place round it. This method achieves what HPU3 tries to, but in lesser average time. 

### IOU CALCULATION
The results are listed in the corresponding IOU calculation folders in the project.

### Team Members

* [Anshu Aviral](https://github.com/cyclotronian)
* [Vishal Anand](http://vishalanand.net)
* Shweta Sharma
* [Utkarsh Dwivedi](https://github.com/Utkarshdevd/)

### Guidance
* [Prof. James Davis](https://users.soe.ucsc.edu/~davis/)
* [Rajan Vaish](http://stanford.edu/~rvaish/)
