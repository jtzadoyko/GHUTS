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


## :::Exercise 2
```python
def get_area_and_perimeter(height, width): ...
```
Create a function which takes a height and width of a rectangle and returns a tuple with the area and perimeter
The formula for area is height * width
The formula for perimeter is (height x 2) + (width x 2)

See area_perimeter.py for the file which you can work with

## :::Exercise 3
```python
def get_grade(students_score, grade_scale): ...
```
Create a function which takes a students_score and the teachers grading scale and returns the letter grade which the student recieved.

See students_grade.py for the file which you can work with
