from ggplot import *

# <example>
ggplot(aes(x='factor(cyl)'), data=mtcars) + \
     geom_bar()
# </example>

# <example>
ggplot(aes(x='factor(cyl)'), data=mtcars) + \
    geom_bar(fill='white', color='steelblue')
# </example>

# <example>
ggplot(aes(x='factor(cyl)', fill='factor(cyl)'), data=mtcars) + \
    geom_bar()
# </example>

# <example>
ggplot(aes(x='factor(cyl)', fill='factor(vs)'), data=mtcars) + \
     geom_bar()
# </example>

# <example>
ggplot(aes(x='factor(cyl)', fill='factor(gear)'), data=mtcars) + \
    geom_bar()
# </example>