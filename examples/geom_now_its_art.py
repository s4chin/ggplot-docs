from ggplot import *


# <example>
ggplot(mtcars, aes('wt', 'mpg')) + \
    geom_point() +\
    ggtitle("Not Art")
# </example>

# <example>
ggplot(mtcars, aes('wt', 'mpg')) + \
    geom_now_its_art() +\
    ggtitle("Art!")
# </example>