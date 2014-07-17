from ggplot import *

# <example>
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "x": range(100),
    "y": np.random.choice([-1, 1], 100)
})
df.y = df.y.cumsum()

ggplot(df, aes(x='x', y='y')) +\
    geom_point()
# </example>

# <example>
ggplot(df, aes(x='x', y='y')) +\
    geom_step()
# </example>