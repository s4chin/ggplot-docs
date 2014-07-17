from ggplot import *


# <example>
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "x": np.random.choice(range(10), 20),
    "y": np.random.choice(range(10), 20)
})
ggplot(df, aes(xmin='x', xmax='x+1', ymin='y', ymax='y+2')) +\
    geom_rect()
# </example>