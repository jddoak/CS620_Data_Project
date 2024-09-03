import os
import numpy as np
import pandas as pd

ds16 = pd.read_excel("./data/2016/2015-16_division_subject.xlsx","DIV Subject by Subgroup")
ds17 = pd.read_excel("./data/2017/2016-17_division_subject.xlsx","Div by Subject by Subgroup")
ds18 = pd.read_excel("./data/2018/2017-2018-division-subject-area.xlsx","Division by Subject & Subgroup")
ds19 = pd.read_excel("./data/2019/division-by-subject-2019.xlsx","Division by Subject by Subgroup")
ds21 = pd.read_excel("./data/2021/2020-2021-division-subject-area.xlsx","Division by Subject and Group")
ds22 = pd.read_excel("./data/2022/division-by-subject-2022.xlsx","Div by Subject by Subgroup")
ds23 = pd.read_excel("./data/2023/division_pass_rates_by_subject_by_stu_group_2022_2023.xlsx","Div subject by subgroup")
ds24 = pd.read_excel("./data/2024/Division-Subject_by_Reporting Group-_2023-2024.xlsx","Division")