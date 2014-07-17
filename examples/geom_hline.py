from ggplot import *


# <example>
ggplot(aes(x='date_hour', y='pageviews'), data=pageviews) + \
    geom_point() +\
    geom_hline(yintercept=[10000])
# </example>

# <example>
ggplot(aes(x='date_hour', y='pageviews'), data=pageviews) + \
    geom_point() +\
    geom_hline(yintercept=range(5000, 20000, 5000), color='coral', size=5)
# </example>

# <example>
ggplot(meat, aes(x='date', y='beef')) +\
    geom_line() +\
    geom_hline(yintercept=2500, color='red') +\
    geom_hline(yintercept=2000, color='yellow') +\
    geom_hline(yintercept=1500, color='green')
# </example>