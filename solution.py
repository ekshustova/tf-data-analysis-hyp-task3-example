import pandas as pd
import numpy as np
from scipy import stats

chat_id = 560481426 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    otv = stats.ttest_1samp(x, 500).pvalue/2 > 0.05 or x.mean() > 500
    return not otv
