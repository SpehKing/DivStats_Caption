# DivStats_Caption
This code DivStats will compute Div-1 and Div-2 and mBLEU for caption diversity evaluation. (to solve this [issue](https://github.com/rakshithShetty/captionGAN/issues/5)). 

Original Code from https://github.com/rakshithShetty/captionGAN to compute Table 4 _Diversity Statistics_ in this paper "Speaking the Same Language: Matching Machine to Human Captions by Adversarial Training" (https://arxiv.org/abs/1703.10476)


```
conda create -n DivStats python=2.7 anaconda
conda activate DivStats
pip install theano
```

 
Compute  Div1, Div2 and mBLEU on the standard COCO-Captions 5K “Karpathy” test split.


Here ``sample.json`` , the DivStats of the candidate captions are computed with respect to the greedy and best beam search 


 
 ```
  python computeDivStats.py  sample.json
 ```
Also, we could compute the Div against the 5-humans ref (5K “Karpathy”), here an example with SoTA image caption system [BLIP](https://arxiv.org/abs/2201.12086), result from [my run](https://github.com/sabirdvd/BLIP_image_caption_demo).

```
python computeDivStats.py BLIP_ViT_Div_5_humans_ref.json
```
Result 
```
PTBTokenizer tokenized 346195 tokens at 657341.73 tokens per second.
Diversity Statistics are as follows:
 Div1: 0.48, Div2: 0.69, gDiv1: 7371

{'reflen': 49005, 'guess': [49907, 44907, 39907, 34907], 'testlen': 49907, 'correct': [39575, 23417, 12580, 6598]}
ratio: 1.01840628507
{'reflen': 49616, 'guess': [51094, 46094, 41094, 36094], 'testlen': 51094, 'correct': [34954, 17054, 7826, 3639]}
ratio: 1.02978877781
{'reflen': 49424, 'guess': [51045, 46045, 41045, 36045], 'testlen': 51045, 'correct': [33828, 15777, 6725, 2855]}
ratio: 1.03279783101
{'reflen': 49466, 'guess': [50996, 45996, 40996, 35996], 'testlen': 50996, 'correct': [33867, 15898, 6885, 2952]}
ratio: 1.03093033599
{'reflen': 49782, 'guess': [51589, 46589, 41589, 36589], 'testlen': 51589, 'correct': [34050, 15881, 6869, 2926]}
ratio: 1.03629826042
{'reflen': 49789, 'guess': [51429, 46429, 41429, 36429], 'testlen': 51429, 'correct': [33945, 15662, 6616, 2808]}
ratio: 1.03293900259
Mean mutual Bleu scores on this set is:
mBLeu_1, mBLeu_2, mBLeu_3, mBLeu_4

[0.68732791 0.50799234 0.36752429 0.26543623]
```
