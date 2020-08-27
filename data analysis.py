import numpy as np
import pandas as pd


ex_employees = pd.read_excel(
    r"Hash-Analytic-Python-Analytics-Problem-case-study-1.xlsx",
    sheet_name="Employees who have left")

data = ex_employees.groupby("dept")


satisfaction_mean = data.mean()["satisfaction_level"]

average_monthly_hour_mean = data.mean()["average_montly_hours"]

number_project_mean = data.mean()["number_project"]

time_spend_company_mean = data.mean()["time_spend_company"]

last_evaluation_mean = data.mean()["last_evaluation"]

promotion_last_5years_mean = data.mean()["promotion_last_5years"]

work_accident_mean = data.mean()["Work_accident"]






