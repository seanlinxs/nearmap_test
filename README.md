# nearmap_test

## implementation details

* copy dataset to current folder
* extract dataset tar file to get the data file(.psv)
* use pandas to read data from .psv file
* explore the data using pandas
* according to the requirement, write a util to find thursdays
* filter data for thursdays
* use scikit-learn to calculate f1_score of thursdays only

## how to run

### running environment

python 3.7.3, jupyter, scikit-learn, pandas, venv

### unit test

```
python -m doctest utils.py -v
```

### notebook

open ```calculate_f1_of_thursdays.ipynb``` and run the kernel

### python

```
python calculate_f1_of_thursdays.ipynb
```