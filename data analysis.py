import numpy as np
import pandas as pd


ex_employees = pd.read_excel(
    r"Hash-Analytic-Python-Analytics-Problem-case-study-1.xlsx",
    sheet_name="Employees who have left")

data = ex_employees.groupby("dept")
satisfaction_mean = data.mean()["satisfaction_level"]





