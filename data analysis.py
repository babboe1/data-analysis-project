import numpy as np
import pandas as pd

#data analysis for ex employees

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

merge1 = pd.merge(satisfaction_mean, average_monthly_hour_mean,
                  how="inner", on="dept")

merge2 = pd.merge(number_project_mean, last_evaluation_mean,
                  how="inner", on="dept")

merge3 = pd.merge(merge1, merge2, how='inner', on="dept")

merge4 = pd.merge(time_spend_company_mean,
                  promotion_last_5years_mean, how="inner", on="dept")

merge5 = pd.merge(work_accident_mean, merge4, how="inner", on="dept")

New_data = pd.merge(merge3, merge5, how="inner", on="dept")

print(New_data)

New_data.to_csv(r"C:\Users\admin\Desktop\project\analysis.ex_employees.csv")

#EXISTING EMPLOYEES  DATA ANALYSIS

existing_emp = pd.read_excel(
    r"Hash-Analytic-Python-Analytics-Problem-case-study-1.xlsx",
    sheet_name="Existing employees")


data1 = existing_emp.groupby("dept")
satisfaction_mean = data1.mean()["satisfaction_level"]

average_monthly_hour_mean = data1.mean()["average_montly_hours"]

number_project_mean = data1.mean()["number_project"]

time_spend_company_mean = data1.mean()["time_spend_company"]

last_evaluation_mean = data1.mean()["last_evaluation"]

promotion_last_5years_mean = data1.mean()["promotion_last_5years"]

work_accident_mean = data1.mean()["Work_accident"]


merge01 = pd.merge(satisfaction_mean, average_monthly_hour_mean,
                   how="inner", on="dept")

merge02 = pd.merge(number_project_mean, last_evaluation_mean,
                   how="inner", on="dept")

merge03 = pd.merge(merge01, merge02, how='inner', on="dept")

merge04 = pd.merge(time_spend_company_mean,
                   promotion_last_5years_mean, how="inner", on="dept")

merge05 = pd.merge(work_accident_mean, merge04, how="inner", on="dept")

New_Data1 = pd.merge(merge03, merge05, how="inner", on="dept")

print(New_Data1)








