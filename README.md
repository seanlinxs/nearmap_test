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

### extract

```
tar -xzf nearmap_test.tar.gz
```

### running environment

python 3.7.3, jupyter, scikit-learn, pandas, venv

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp /path/to/test.tar.gz ./
```

### unit test

```
python -m doctest utils.py -v
```

### notebook

```
jupyter-notebook
```

Then open ```calculate_f1_of_thursdays.ipynb``` and run the kernel

### python

```
python calculate_f1_of_thursdays.py
```