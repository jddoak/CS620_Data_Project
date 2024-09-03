import os
import numpy as np
import pandas as pd

sts16 = pd.read_excel("./data/2016/2015-16_state_subject.xlsx","STATE Subject by Subgroup")
sts17 = pd.read_excel("./data/2017/2016-17_state_subject.xlsx","State by Subject by Subgroup")
sts18 = pd.read_excel("./data/2018/2017-2018-state-subject-area.xlsx","Sheet0")
sts19 = pd.read_excel("./data/2019/state-by-subject-2019.xlsx","State by Subject by Subgroup")
sts21 = pd.read_excel("./data/2021/2020-2021-state-subject-area.xlsx","State by Subject and Group")
sts22 = pd.read_excel("./data/2022/state-by-subject-2022.xlsx","State by Subject by Subgroup")
sts23 = pd.read_excel("./data/2023/state_pass_rates_by_subject_by_stud_group_2022_2023.xlsx","State subject by  student group")
sts24 = pd.read_excel("./data/2024/State-Subject_by_Reporting Group-_2023-2024.xlsx","State")