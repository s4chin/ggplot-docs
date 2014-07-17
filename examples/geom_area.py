from ggplot import *


# <example>
ggplot(aes(x='date', ymin='beef - 1000', ymax='beef + 1000'), data=meat) + \
    geom_area()
# </example>

# <example>
ggplot(aes(x='date', y='beef', ymin='beef - 1000', ymax='beef + 1000'), data=meat) + \
    geom_area() + \
    geom_point(color='coral')
# </example>