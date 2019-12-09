# surfs_up

##Challenge Overview  
in this project we are we gather data on beautiful Oahu weather on July and December to open a surf and shake shop. The goals for this challenge are to:
- Determine key statistical data about the month of July.
- Determine key statistical data about the month of December.
- Compare your findings between the month of July and December.
- Make 2 or 3 recommendations for further analysis.
- Share your findings in the Jupyter Notebook.

## Modual Objectives: 
In this module we work with SQLite, SQLAlchemy, and Flask to build on our knowledge of SQL database structures and querying methods. Use SQLAlchemy to connect to and query a SQLite database. We Used Flask tool on app.py file to get summary precipitation to display our results in a webpage.Also using Matplotlib, Datetime to graph.
![flask](https://github.com/hbostanchi/surfs_up/blob/master/pic/flask.png)

## Resources Data Source: 
Software: SQLite, Flask, Python, From Jupyter notebook used NumPy, Pandas, Matplotlib, Datetime and SQLAlchemy.
The dataset we explored on weather data 2010-2017.
There are rows contain NaN and  also more data for month of Jun and July than December.


## Observation from Analysis:
- The data count for the month of July is more than Dec, so we  should look closely  to the station data.
- The mean for daily precipitation is about 0.21inches in December and about 016 inches in July. So in general on December we get more rain than July.
- The standard deviation is 0.54 inches in December and 0.62 inches.
- As we look at the bar chart for precipitation on months of June, July and December we noticed that the December is much heavier in rain so it might have some difficulty for the surf shop on that month.
![prc](https://github.com/hbostanchi/surfs_up/blob/master/pic/percepitation%20comparison.png)
![bar](https://github.com/hbostanchi/surfs_up/blob/master/pic/bar.png)

## Recommendation:
- The analysis only compare the July and Dec months in 7 years toghther. However it would be better if the comparison between each year July and Dec and compare the data annually together to make sure finding the trend.
- Also only 2 months analysis wouldn’t help much to narrowed down for some suggestion like coupons or sale on rainy days to run business. If we get monthly data, we find more idea which months the discount could help the business to sell more.
- We should look at the skewness of the data and look into the outliers  for both months.


