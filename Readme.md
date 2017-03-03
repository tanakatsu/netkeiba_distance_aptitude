# Netkeiba crawler for distance aptitude

Data crawler for [netkeiba.com](http://www.netkeiba.com) (especially for distance aptitude)

## Get started

Install dependency packages.

```
$ pip install beautifulsoup4 
$ pip install chardet
```

Fetch data

```
$ python netkeiba_distance_aptitude.py [--input sample.horselist.pkl] [--output output.pkl]
```

Sort

```
$ python sort.py output.pkl
```

Test one 

```
# Edit horsename and run.
$ python test.py
```

#### Input file

Input file is .pkl file which is a list of dictionary.
The key of dictionary items should be 'name'.

```
[ 
  {'name': u'ディープインパクト'}, 
  {'name': u'オルフェーヴル'} 
]
```

#### Format of output file

Output file is .pkl file which is a dictionary of name and distance factor.

```
{
    u'メジロマックイーン': 0.939655172414,
    u'サクラバクシンオー': 0.051724137931
}
```

Distance factor has a range of 0.0-1.0.

- 0.0: sprinter (a better performer over a shorter distance) 
- 1.0: stayer (a better performer over a longer distance)


## License
MIT



