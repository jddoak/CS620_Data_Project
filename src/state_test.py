import os
import numpy as np
import pandas as pd

stt16 = pd.read_excel("./data/2016/2015-16_state_test.xlsx","STATE test-level")
stt17 = pd.read_excel("./data/2017/2016-17_state_test.xlsx","State by Test")
stt18 = pd.read_excel("./data/2018/2017-2018-state-test-by-test.xlsx","Sheet0")
#stt19 = pd.read_excel("./data/2019/state-by-test-2019.xlsx","state by Test") Corrupt
stt21 = pd.read_excel("./data/2021/2020-2021-state-test-by-test.xlsx","State Test by Test")
stt22 = pd.read_excel("./data/2022/state-by-test-2022.xlsx","State by Test")
stt23 = pd.read_excel("./data/2023/state_pass_rates_by_test_2022_2023.xlsx","State by test")
stt24 = pd.read_excel("./data/2024/State_Test_by_level_2023_2024.xlsx","State")