# DivStats_Caption
This code DivStats will compute Div-1 and Div-2 and mBLEU for caption diversity evaluation. (to solve this [issue](https://github.com/rakshithShetty/captionGAN/issues/5)). 

Original Code from https://github.com/rakshithShetty/captionGAN


```
conda create -n DivStats python=2.7 anaconda
conda activate DivStats
```

Compute  Div1, Div2 and mBLEU on the standard COCO-Captions 5K “Karpathy” test split.

```
 python computeDivStats.py  sample.json
 ```
