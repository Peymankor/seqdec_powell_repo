import os
import pandas as pd
import numpy as np
os.chdir("/home/peyman/Documents/PhD_UiS/seqdec_powell_repo/Chap3_Adap_Mar_Plan/functions")
os.getcwd()
file = 'Base parameters.xlsx'
raw_data = pd.ExcelFile(file)
data = raw_data.parse('parameters')
cost = data.iat[0, 2]
trial_size = np.rint(data.iat[1, 2]).astype(int)
price = data.iat[2, 2]
theta_step = data.iat[3, 2]
T = data.iat[4, 2]
reward_type = data.iat[5, 2]
print(raw_data)

