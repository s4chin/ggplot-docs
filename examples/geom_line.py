from ggplot import *
import pandas as pd


# <example>
ggplot(mtcars, aes('wt', 'mpg')) + \
    geom_line()
# </example>

# <example>
ggplot(mtcars, aes('wt', 'mpg', 'qsec')) + \
    geom_line()
# </example>

# <example>
ggplot(mtcars, aes(x='wt', y='mpg', size='qsec')) + \
    geom_line()
# </example>

# <example>
ggplot(mtcars, aes(x='wt', y='mpg', color='qsec')) + \
    geom_line() +\
    scale_colour_gradient(low="coral", high="steelblue")
# </example>

# <example>
ggplot(mtcars, aes(x='wt', y='mpg')) + \
    geom_line(color='steelblue', size=100)
# </example>

# <example>
ggplot(mtcars, aes(x='wt', y='mpg')) +\
    geom_line(colour="black", size = 100) +\
    geom_line(colour="pink", size = 40)
# </example>

# <example>
ggplot(mtcars, aes(x='wt', y='mpg')) + \
    geom_line(color='steelblue', size=100, alpha=0.4)
# </example>

# <example>
ggplot(diamonds, aes(x='carat', y='price', color='color')) +\
    geom_line(alpha=0.1)
# </example>

# <example>
ggplot(meat, aes(x='date', y='beef')) +\
    geom_line()
# </example>

# <example>
ggplot(pd.melt(meat, id_vars=['date']), aes(x='date', y='value', color='variable')) +\
    geom_line()
# </example>

# <example>
ggplot(pd.melt(meat, id_vars=['date']), aes(x='date', y='value', color='variable')) +\
    geom_line()
# </example>


# <example>
movies.rating = movies.rating.round(0)
movies_by_year = movies.groupby(["year", "rating"]).apply(len).reset_index()
movies_by_year.columns = ['year', 'rating', 'number']
ggplot(movies_by_year, aes(x='year', y='number', color='rating')) +\
    geom_line()
# </example>

# <example>
ggplot(movies_by_year, aes(x='year', y='number', color='factor(rating)')) +\
    geom_line()
# </example>

