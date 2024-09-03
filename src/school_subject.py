import os
import numpy as np
import pandas as pd

ss16 = pd.read_excel("./data/2016/2015-16_school_subject.xlsx","SCH Subject by Subgroup")
ss17 = pd.read_excel("./data/2017/2016-17_school_subject.xlsx","Sch by Subject by Subgroup")
ss18 = pd.read_excel("./data/2018/2017-2018-school-subject-area.xlsx","School by Subject and Subgroup")
ss19 = pd.read_excel("./data/2019/school-by-subject-2019.xlsx","School by Subject by Subgroup")
ss21 = pd.read_excel("./data/2021/2020-2021-school-subject-area.xlsx","School by Subject and Group")
ss22 = pd.read_excel("./data/2022/school-by-subject-2022.xlsx","Sch by Subject by Subgroup")
ss23 = pd.read_excel("./data/2023/school_pass_rates_by_subject_by_stu_group_2022_2023.xlsx","Sch subject by student group")
ss24 = pd.read_excel("./data/2024/School-Subject_by_Reporting Group-_2023-2024.xlsx","School")