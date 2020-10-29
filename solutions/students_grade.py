# TODO: create a function provided a students grade and the grading scale of the course
# an output which returns the letter grade for the student assuming the grading scale is provided as a dictionary
# where the keys are the letter grades, and the values are the ranges for that letter grade provided as a tuple
# HINT: try using items() on a dict to get the key value pairs
# run the code and if no errors are triggered from the run_test_case method, you have successfully completed this exercise

get_students_grade(students_grade, grade_scale):
  for letter_grade, grade_range in grade_scale.items():
    if students_grade >= grade_range[0] and students_grade <= grade_range[1]:
      return letter_grade


run_test_case():
  teachers_grade_scale = {"A": (90,100),
                          "B": (80, 89),
                          "C": (70, 79),
                          "D": (60, 69),
                          "F": (0, 59)
                        }
  students_grade = 64
  
  assert "D" == get_students_grade(students_grade, teachers_grade_scale)

run_test_case()
