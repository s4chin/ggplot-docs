from ggplot import *


# <example>
ggplot(aes(x='pageviews'), data=pageviews) + \
    geom_density()
# </example>

# <example>
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "x": np.random.normal(0, 10, 1000),
    "y": np.random.normal(0, 10, 1000),
    "z": np.random.normal(0, 10, 1000)
})
df = pd.melt(df)

ggplot(aes(x='value', color='variable'), data=df) + \
    geom_density()
# </example>

# <example>
ggplot(aes(x='value', color='variable', fill='variable'), data=df) + \
    geom_density(alpha=0.6)
# </example>

# <example>
ggplot(movies, aes(x='rating')) + \
    geom_density()
# </example>

# <example>
ggplot(movies[movies.mpaa.isnull()==False], aes(x='rating', color='mpaa')) + \
    geom_density()
# </example>

# <example>
movies['decade'] = movies.year.round(-1)
ggplot(movies, aes(x='rating', colour='factor(decade)')) + \
    geom_density()
# </example>