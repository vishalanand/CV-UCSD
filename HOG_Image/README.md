#Usage for running the HOG codes

The `complete_HOG.cpp` displays visually the boxes of pedestrians compiles using : 
```
g++ complete_HOG.cpp `pkg-config opencv --cflags --libs`
./a.out pedestrian.jpg
```

The `complete_HOG_automate_dat.cpp` writes the boxe dimensions of pedestrians : 
```
g++ complete_HOG_automate_dat.cpp `pkg-config opencv --cflags --libs`
./a.out pedestrian.jpg
```

The codes are run agains the image data obtained from [FudanPed](https://github.com/vishalanand/CV-UCSD/tree/master/Dataset/FudanPed/Recognition), [PennPed](https://github.com/vishalanand/CV-UCSD/tree/master/Dataset/PennPed/Recognition), [Caltech](http://vishalanand.net/CV_UCSD/*.jpg) Pedestrian Samples
 
# The bash scripts are then run to generate the box dimenstions in 
 [x y w h] format
