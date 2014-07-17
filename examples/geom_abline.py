from ggplot import *



# <example>
ggplot(mtcars,aes(x='wt',y='mpg')) + \
    geom_point() + \
    geom_abline(intercept=20)
# </example>

# <example>
ggplot(mtcars,aes(x='wt',y='mpg')) + \
    geom_point() + \
    geom_abline(intercept=37,slope=-5,
                colour="red",size=10)
# </example>