# GHUTS

::Exercise 1
```python
def batchLoading(list_arg, bsize = 5): ...
```
Create a method called batchLoading which takes in two arguements, a list and a batch size which will default to 5 if the arguement is not specified.
The function should now print elements of that list in batches.

```python
my_list = ['val1','val2','val3','val4','val5','val6','val7','val8','val9','val10']
batchLoading(my_list, bsize = 2)
```

```console
>>> 'val1','val2'
>>> 'val3','val4'
>>> 'val5','val6'
>>> 'val7','val8'
>>> 'val9','val10'
```

In stances where there it is not possible to have the final batch complete based on the batch size argument it should return the remaining values like the below example.
```python
my_list = ['val1','val2','val3','val4','val5','val6','val7','val8','val9','val10']
batchLoading(my_list, bsize = 6)
```

```console
>>> 'val1','val2','val3','val4','val5','val6'
>>> 'val7','val8','val9','val10'
```
