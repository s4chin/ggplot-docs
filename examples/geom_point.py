from ggplot import *

# <example>
ggplot(mtcars, aes('wt', 'mpg')) + \
    geom_point()
# </example>

# <example>
ggplot(mtcars, aes('wt', 'mpg', 'qsec')) + \
    geom_point()
# </example>

# <example>
ggplot(mtcars, aes(x='wt', y='mpg', size='qsec')) + \
    geom_point()
# </example>

# <example>
ggplot(mtcars, aes(x='wt', y='mpg', color='qsec')) + \
    geom_point() +\
    scale_colour_gradient(low="coral", high="steelblue")
# </example>

# <example>
ggplot(mtcars, aes(x='wt', y='mpg')) + \
    geom_point(color='steelblue', size=100)
# </example>

# <example>
ggplot(mtcars, aes(x='wt', y='mpg')) +\
    geom_point(colour="black", size = 100) +\
    geom_point(colour="pink", size = 40)
# </example>

# <example>
ggplot(mtcars, aes(x='wt', y='mpg')) + \
    geom_point(color='steelblue', size=100, alpha=0.4)
# </example>

# <example>
ggplot(diamonds, aes(x='carat', y='price', color='color')) +\
    geom_point(alpha=0.1)
# </example>