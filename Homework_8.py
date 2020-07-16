import pandas as pd
import numpy as np

#reads in a .csv file as a Pandas dataframe, which is a lot like a spreadsheet and very powerful!
covid = pd.read_csv(r'C:\Users\Ryan\Desktop\jupyter\COVID19_line_list_data.csv')

'''
Some things to know

covid.head() #returns first 5 rows in the DataFrame
len(covid) #returns the number of rows in the dataframe
covid.columns #returns a list of the column names
covid.index #returns all the index (think row numbers) of the dataframe
'''

'''
We need to address the issue that a number of 'deaths' are marked with only a date
We have a few options, we could delete all those rows, but it turns out to be almost 25% of the dataset, would you want to delete all that? Not really.
We could think, if a date is given, the person unfornately died on that day, so the column value should be a '1' to tell us that
This is what I decided to do
'''
death = {} # empty dictionary
for index in range(len(covid['death'])): #len(covid['death']) gives us how many rows, and using range() we go from row 0 to the ending row, incrementing by 1
    try:
        # the point of this is to simply check if we can convert the value to a integer, if we can't we assume it is a date
        # if it is a date, Python will throw a ValueError, which then forces us to go to the 'except' block of code and skips everything else
        value = int(covid.iloc[index].loc['death']) 
        # note: pandas uses .iloc[] and .loc[] meathods to "locate" rows or columns or both, here we are .iloc[] by row number (where iloc is like index locate)
        # and then once we have that row from .iloc[], we "locate" the column we want using .loc['death'] to get the value in that column since we have row and column
        if value != 0:
            death[index] = 1
        else:
            death[index] = 0
    except ValueError:
        #if the value couldn't be converted to an integer, let's assume it was a date and simply use a '1' to confirm the death
        death[index] = 1
        
 # all of these 0 and 1 values are actually in the dictionary 'death' from before the loop
 # since we have the index that corresponds to each row in the column, 
 # pandas lets us simply turn this into a Series (think array, list, tuple type)
 # and then we simply assign this to the covid['death'] column and replace all its values with clean ones
covid['death'] = pd.Series(death)


# next we need to tackle the missing age values, I decided to simply replace the missing values with the average of all the other values
# this is done using .fillna()
# IMPORTANT, inplace=True ensures we are actually making changes to the dataframe, otherwise we could just be returning the values and not modifying our dataframe

covid['age'].fillna(np.round(np.mean(covid['age']), 0), inplace=True) 
covid.age.describe()


# I decided to also use the covid['gender'] column for further relationship analysis
# we were only missing about 100 values and since we can't really guess the value, we are forced to drop it

covid.dropna(inplace=True) # NOTE: inplace=True being used again!
covid['gender'].isna().sum() # .isna().sum() will tell us how many missing values there are! 



# finally the fun part! It is important to ensure your dataframe has the right datatypes
# calling covid.dtypes will return the types of each column, the generic 'object' datatype is Pandas kind of "catch all" type and can lead to weird issues plotting!
# the 'category' datatype is a useful type for things we know are catergorical, since it handles a lot of things for us on the back end later
covid.gender = covid.gender.astype('category')
covid.location = covid.location.astype('category')
covid.country = covid.country.astype('category')


# I used Seaborn here as it simplifies plotting a lot more than matplotlib.pyplot, personal preferrence
import seaborn as sns
# barplot 
sns.barplot(data=covid, x='gender', y='death', dodge=True)
# point plot, useful for error estimation and relationships on categorical data
sns.pointplot(data=covid, x='gender', y='death', ci=0.95)
# a bit advanced, describes kernel density estimated probability distributions for each set
sns.violinplot(data=covid, x='death', y='age', dodge=True)
#
print('% male:', len(covid[(covid.gender == 'male') & (covid.death == 1)]) / len(covid))
print('% female:', len(covid[(covid.gender == 'female') & (covid.death == 1)]) / len(covid))

# Interestingly, males seem much more likely affected in our dataset in terms of probability of death, 4.9% for males and 1.6% for females
# We have no way of describing the causality model here but it would be interesting to work with more recent data to see if that trend continues!
