import numpy as np
import pandas as pd


emp_who_left = pd.read_excel(
    r"Hash-Analytic-Python-Analytics-Problem-case-study-1.xlsx", sheet_name="Employees who have left")
# print(emp_who_left)

a = emp_who_left.groupby("dept")
a_mean = a.mean()["satisfaction_level"]
# print(a_mean)

b = emp_who_left.groupby("dept")
b_mean = b.mean()["average_montly_hours"]


c = pd.merge(a_mean, b_mean, how="inner", on="dept")
