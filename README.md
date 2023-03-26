# fasf (fast)

Type faster by not lifting your fingers off the keyboard - a concept. 

The logic behind it is that it would not take long for someone who types using all of their fingers to get used to this kind of typing. 

## Intro 

Out WPM is affected by the fact that we have to lift our fingers off the keyboard. What if we could have our hands in the 'base' position for 10 finger typing and still be able to write comprehensible sentences? 

## How to use

![image of 10 finger typing](https://upload.wikimedia.org/wikipedia/commons/9/93/Finger_position_on_a_keyboard.png)

clone the repo, run `python fast-type.py` and have your hands in the default typing position (pointers on F and J); instead of lifting the finger to press a key, press down with that finger on the key underneath it.

For example, instead of pressing `w` with your ring finger, press `s`which is the key under the ring finger. The longer the words, the less likely there will be a collision. Using a word prediction model like ChatGPT would help solve collisions.

## Data

The data is based on 10k most used words dictionary that are saved in `common-words.txt'.

## Example 


### 1

```
jskjf a slfd ;fddkdfklj jlddl sljld jdl; sllfd fjks kssjd
```

output :

```
Most likeley : using a word prediction model would help solve this issue

Raw output: using a/q/z word prediction model would help solve this issue
```

### 2

```
 fsl fjkjfs afd kjfkjkfd fjd jjkfdfsd ajd jjjaj sfj;kdkfj ajd k aj jlf sjfd afljf fjd jjkfdfsd
```

output :

```
Most likeley : two things are infinite the universe and human stupidity and i an not sure about the universe

Raw output: two things are/age/ave/abc/arc/ate infinite the/tue/bye/gmc universe and/que/aud/amd/aye human stupidity and/que/aud/amd/aye i/k an/am/au/ah/aj/zu not/job/hot/nov/nor/mlb sure about the/tue/bye/gmc universe
```

## Asking ChatGPT to fill in the blanks (collisions)

![asking chat gpt to fill in the blanks](https://i.imgur.com/Wjd0cJK.png)




