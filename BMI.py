import math
import pandas as pd
import os


def main():
    filename = input("Enter the name of the CSV file : ")
    filePath = os.path.join(os.getcwd(), filename)
    try:
        data = pd.read_csv(filePath)
        data['BMI'] = data.apply(lambda row: bmiCalc(row['Weight (kg)'], row['Height (m)']), axis=1).round(2)
        data['Weight Status'] = data['BMI'].apply(bmiStat)
        data.to_csv(filePath, index=False)
        print(f"Updated results to: '{filename}'")
    except FileNotFoundError:
        print(f"File '{filename}' not found")

def bmiCalc(weight, height):
    return round(weight / math.pow(height, 2), 2)

def bmiStat(bmi):
    if 11.9 <= bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal weight'
    elif 24.9 <= bmi < 29.9:
        return 'Overweight'
    elif 29.9 <= bmi < 39.9:
        return 'Obese'
    else:
        return 'Morbidly Obese'

main()
