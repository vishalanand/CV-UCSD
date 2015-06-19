#Usage for generating the `IOU_Fudan_CPU.dat` output : 

Use the Matlab codes at [Intersection_Over_UnionCompile](https://github.com/vishalanand/CV-UCSD/tree/master/Intersection_Over_Union/) the `complete_HOG_automate.cpp` from `../HOG_Image/` folder and execute one of the following : 

* IOU_<Dataset>_direct.m to compute if the corresponding detections are correct wrt the ground-truth. Imagine, that there are three pedestrian in an image and the first and third are detected. Then, using this process the third pedestrian will be mapped with the ground truth of second one's and will probably return as false-positive(FP). TO do away with this error, we used the second approach.

* IOU_<Dataset>_all.m to computes if the detections are present in the ground-truth. Thus non-synchronized detections will be correctly detected in the IOU calculations.