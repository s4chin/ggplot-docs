from ggplot import *


# <example>
ggplot(mtcars, aes(x='wt', y='mpg')) +\
    geom_point() +\
    geom_vline(xintercept=[2, 4, 6])
# </example>

# <example>
ggplot(mtcars, aes(x='wt', y='mpg')) +\
    geom_point() +\
    geom_vline(xintercept=[2, 4, 6], linetype='dashed')
# </example>