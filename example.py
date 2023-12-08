from hrbrthemes import *

from plotnine import *
from plotnine.data import mtcars

(ggplot(mtcars, aes("wt", "mpg", color="factor(gear)")) 
  + geom_point() 
  + labs(title = "hrbrmstr's Fav Example Plot", x = "Weight (tons)", y = "Miles-per-gallon")
  + theme_ipsum())