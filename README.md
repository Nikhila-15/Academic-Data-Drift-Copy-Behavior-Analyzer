# Academic-Data-Drift-Copy-Behavior-Analyzer

## Overview
This project analyzes student academic data and demonstrates how shallow copy and deep copy behave in Python. It generates random student records and applies modifications based on roll number logic. The program also measures data drift using statistical calculations.

## Features
Random student data generation
Use of shallow copy and deep copy
Personalized data modification using roll number
Statistical analysis including mean and standard deviation
Manual calculation of mean
Drift detection and classification

## Data Structure
Each student record contains:
student id, marks, attendance, and assignment scores stored in a list
All records are stored in a list of dictionaries

## Functions / Logic Used
Data generation using loops
Copy operations using shallow and deep copy
Conditional modification using roll number logic
Data analysis using Pandas and NumPy

## Personalization Logic
Roll number is used to decide which records to modify
Formula used:
roll number modulo 3
For roll number 2:
indices 0, 2, 4, 6, 8 are modified

## Drift Logic

Drift is calculated as the difference between original mean and modified mean
A custom threshold value is used:5
Based on drift value:
Stable Data
Minor Drift
Critical Drift

## How to Run

Install required libraries
pip install pandas numpy
Run the program
python file_name.py

## Output

Original data
Shallow copy data
Deep copy data
Mean, standard deviation, drift
Tuple containing calculated values
Final result showing data stability

## Learning Outcome
This project helped in understanding shallow copy and deep copy behavior, data drift, and basic data analysis using Python libraries.
