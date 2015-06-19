#Usage for running the HOG codes

The `complete_HOG_video.cpp` displays visually on-the-go the boxes of humans, it compiles using :  
```
g++ complete_HOG_video.cpp `pkg-config opencv --cflags --libs`
./a.out test.avi
```

N.B. The sample video initially has a logo, which gets detected to be a person; after the first few seconds, the actual persons get detected