# Data Project Tools

## File Manifest

### explorefeatures.py
Run in new dataset.csv and writes datasetfeatures.csv as an overview of set's columns.

### dtools.py
Currently includes a drop function that archives dropped series into a JSON file during data cleaning processes.

### /test_sets/*
- [asa_shooter.csv](https://www.americansocceranalysis.com/asa-xgoals)
- iris.csv

## To Do
- Tidy up explorefeatures.py and merge into dtools.py.


## ref.txt
# Reference
All sorts of snippets.

## Format
```
tech > topic > do something
snippet to do something
###
tech > another topic > do something else
snippet to do:
    something else
###
```
## To Do
- Add keys to ref.txt
To do: Remove or rework explorefeatures.py as Pandas has describe
