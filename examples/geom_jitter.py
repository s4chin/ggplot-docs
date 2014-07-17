from ggplot import *

# <example>
ggplot(diamonds, aes(x='carat', y='price', color='color')) +\
    geom_point(alpha=0.1)
# </example>

# <example>
ggplot(diamonds, aes(x='carat', y='price', color='color')) +\
    geom_jitter(alpha=0.1)
# </example>

# <example>
ggplot(mtcars, aes(x='wt', y='mpg')) + \
    geom_point()
# </example>