# DivStats_Caption
This code DivStats will compute Div-1 and Div-2 and mBLEU for caption diversity evaluation. (to solve this [issue](https://github.com/rakshithShetty/captionGAN/issues/5)). 

Original Code from https://github.com/rakshithShetty/captionGAN to compute Table 4 in this paper "Speaking the Same Language: Matching Machine to Human Captions by Adversarial Training" (https://arxiv.org/abs/1703.10476)


```
conda create -n DivStats python=2.7 anaconda
conda activate DivStats
```

Compute  Div1, Div2 and mBLEU on the standard COCO-Captions 5K “Karpathy” test split.


Here ``sample.json`` , the DivStats of the candidate captions are computed with respect to the greedy and best beam search 

```
 python computeDivStats.py  sample.json
 ```
