import numpy as np
from scipy import stats

gamers = [40, 180, 120, 250, 300, 140, 300, 400, 800]
np.mean(gamers)
np.median(gamers)

quartis = np.quantile(gamers, [0, 0.25, 0.5, 0.75, 1])
np.std(gamers, ddof=1)

stats.describe(gamers)