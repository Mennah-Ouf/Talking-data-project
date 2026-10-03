#Talking Data Starter Code

#Part 2 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "Buried"
print ("my favourite movie is "+favMovie)



#Part 3 Investigate the data

#print(movieData.head())
#print(movieData["movie_title"])
      #Part 4 Filter data
favMovieBooleanList=movieData["movie_title"]==favMovie
#print(favMovieBooleanList)
favMovieData=movieData.loc[favMovieBooleanList]
print(favMovieData)
mysteryAndSuspenseMovieBooleanList=movieData["genres"].str.contains("Mystery & Suspense")
mysteryAndSuspenseMovieData=movieData.loc[mysteryAndSuspenseMovieBooleanList]
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information





print("\n\n")

#Create a new variable to store a new data set with a certain genre




numOfMovies=mysteryAndSuspenseMovieData.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre [Mystery & Suspense] in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category [Mystery & Suspense].")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
    " compares to other movies in this genre.\n")

#Part 5 Describe data
#min
min=mysteryAndSuspenseMovieData["audience_rating"].min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated [61] points higher than the lowest rated movie.")
print()

#find max
max=mysteryAndSuspenseMovieData["audience_rating"].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated [35] points lower than the highest rated movie.")
print()

#find mean
mean =mysteryAndSuspenseMovieData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " [is higher than the mean movie rating.")

#find median
median =mysteryAndSuspenseMovieData["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " [is higher than  the median movie rating.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram


#Adds labels and adjusts histogram
plt.hist(mysteryAndSuspenseMovieData["audience_rating"], range=(0,100), bins=20)
plt.grid(True)
plt.title("mystery and suspense audience ratings histogram")
plt.xlabel("audience rating")
plt.ylabel("number of movies")

#Prints interpretation of histogram
print(
  "According to the histogram, the audience rating of 40 wins first place for having the highest number of movies which is approximately 280"
)
print()

#Show histogram
plt.show()
input("Press enter to see the next data visualization.\n")
plt.close()

#Create scatterplot

#Adds labels and adjusts scatterplot
plt.scatter(data=mysteryAndSuspenseMovieData, x="audience_rating", y="critic_rating")
plt.grid(True)
plt.title("audience versus critic")
plt.xlabel("audience rating")
plt.ylabel("critic rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, it seems like the audience rating and the critic rating our friends with a positive correlation between them"
)
print()


#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
