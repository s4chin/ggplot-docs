from ggplot import *

# <example>
ggplot(aes(x='pageviews'), data=pageviews) + \
    geom_histogram()
# </example>

# <example>
ggplot(aes(x='pageviews'), data=pageviews) + \
    geom_histogram(binwidth=50)
# </example>

# <example>
ggplot(aes(x='pageviews'), data=pageviews) + \
    geom_histogram(binwidth=1000)
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
    geom_histogram()
# </example>

# <example>
ggplot(aes(x='value', fill='variable', color='variable'), data=df) + \
    geom_histogram(alpha=0.6)
# </example>

# <example>
ggplot(movies, aes(x='rating')) + \
    geom_histogram()
# </example>

# <example>
ggplot(movies, aes(x='rating', weight='votes')) + \
    geom_histogram()
# </example>

# <example>
ggplot(movies[movies.mpaa.isnull()==False], aes(x='rating', color='mpaa')) + \
    geom_density()
# </example>

# <example>
movies['decade'] = movies.year.round(-1)
ggplot(movies, aes(x='rating', colour='factor(decade)')) + \
    geom_histogram()
# </example>
