from ggplot import *


# <example>
ggplot(mtcars, aes(x='wt', y='mpg', label='name')) +\
    geom_text()
# </example>

# <example>
ggplot(mtcars, aes(x='wt', y='mpg', label='name')) +\
    geom_text(size=100)
# </example>

# <example>
ggplot(mtcars, aes(x='wt', y='mpg', label='name', size='mpg')) +\
    geom_text()
# </example>

# <example>
ggplot(mtcars, aes(x='wt', y='mpg', label='name')) +\
    geom_text(hjust=0.15, vjust=0.1) +\
    geom_point()
# </example>

# <example>
ggplot(mtcars, aes(x='wt', y='mpg', label='name')) +\
    geom_text(angle=45) +\
    geom_point()
# </example>

# <example>
ggplot(mtcars, aes(x='wt', y='mpg', label='name', color='factor(cyl)')) +\
    geom_text()
# </example>