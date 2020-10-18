# GHUTS

## :::Exercise 1
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

For cases where it is not possible to have the final batch 'full' based on the batch size argument, it should return the remaining values like the below example.
```python
my_list = ['val1','val2','val3','val4','val5','val6','val7','val8','val9','val10']
batchLoading(my_list, bsize = 6)
```

```console
>>> 'val1','val2','val3','val4','val5','val6'
>>> 'val7','val8','val9','val10'
```

- [ ] How many iterations will i need to perform considering the size of the list and the batch size?
- [ ] How should i determine the starting and ending points for each batch?
- [ ] How do i create a repository using GIT?
- [ ] How do i create a branch in the repository to make edits?
- [ ] How do i push those changes to my new branch and then create a pull request for review?



Upon completion of this exercise you should create a pull request aka PR with a file name called **batchloading.py**
