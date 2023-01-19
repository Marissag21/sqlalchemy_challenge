# sqlalchemy_challenge
I created an engine to connect to the sqlite.
In part 1 (climate-starter) I used automap_base() to reflect the tables into classes and saved the references to those classes. 
A session was created to connect to the DB

#Exploratory Data
A query was ran to find the most recent date in the data set.
I ran inspect on the engine to find out what each column was for Measurement.
Then I queried the last 12 months of precipitation data and plotted the results. 
df.describe() was used to calculate the summary statistics. 

# Exploratory Station Analaysis
I ran a query to calculate the total number of stations. Then I ran inpspector.get_columns() to get the columns for each table. 
A query was ran to find the most active stations, and then calculations for the min, max, average, and count were ran for te most active station. 
Next, the most active station's temperature observations for the last 12 months was queried. 
I converted the 'tobs' into a dataframe then ran value_counts() for tobs and plotted the results. 
Lastly, the session was closed. 

# Part 2

First, dependencies were ran.
An engine was created and the references were saved to each table. 
An app was created for flask.
Next, the home page was created to reflect all the possible routes. 
Then, the precipitation route was defined for precipitation and a session link was created. 
A query was created to obtain the date and average prcp from 'Measurement', then the results were converted into a dictionary and was displayed in a json reprentation. 
Next, the 'stations' route was created, a session was created, and a query was ran for the list of the stations from 'station'. The list of tuples was converted into a list then returned in a json representation. 
The 'tobs' route was then created, a session was created, then the variable 'last_year' was created by using dt. date and the last date in the data set and subtracting a year using dt. timedelta to reflect the previous year. 
A query was ran for the dates and temperature observations of the most active station for the previous year.
The list of tuples was converted to a normal list then displayed as a json object. 
Next, the start and start/end route were created by defining start date  and start_end. I used dt. datetime.strptime(start, "%m-%d-%Y") and dt.datetime.strptime(end, "%m-%d-%Y") to be able to get a return of data based on the dates that were asked by the user. 