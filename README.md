# BMI-Calc

This is a short project to gain experience with Panda as well as reading and modifying CSV files.

## Table of Contents
- [How to use](#how-to-use)
- [Functions](#functions)
- [Example Use](#example-use)

## How to use

1. Make sure you have Python 3 and the Pandas library installed (`pip install pandas`).
2. Copy and paste the provided code into a Python script (e.g., **BMI.py**).
3. Save the CSV file **sampledata.csv** in the same directory as the Python script.
4. Run the Python script, and it will prompt you to enter the name of the CSV file.
5. After entering the filename, the script will calculate BMI and weight status for each row in the CSV file and save the updated data back to the same file.

## Functions:

1. `**bmiCalc(weight, height)**`: Calculates the BMI (Body Mass Index) given the weight (in kilograms) and height (in meters) using the formula **BMI = weight / (height^2)**. The result is rounded to two decimal places.
2. `**bmiStat(bmi)**`: Determines the weight status based on the provided BMI value. It takes the BMI as input and returns the weight status as a string. The weight status categories are defined as follows:
* Underweight: BMI >= 11.9 and < 18.5
* Normal weight: BMI >= 18.5 and < 24.9
* Overweight: BMI >= 24.9 and < 29.9
* Obese: BMI >= 29.9 and < 39.9
* Morbidly Obese: BMI >= 39.9

##  Example Use
```bash
python BMI.py
Enter the name of the CSV file : data.csv
Updated results to: 'data.csv'
```
