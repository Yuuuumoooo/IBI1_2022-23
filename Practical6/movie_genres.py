#make two lists for Key and Value
Movie_genre=["Comedy","Action","Romance","Fantasy","Science-fiction","Horror","Crime","Documentary","History","War"]
students_number=[73,42,38,28,22,19,18,12,8,7]
#use for-loop to make a dictionary of these two lists
favourite_movie_generes={}
for i in range(len(Movie_genre)):
  favourite_movie_generes[Movie_genre[i]]=students_number[i]
print(favourite_movie_generes)

#{'Comedy': 73, 'Action': 42, 'Romance': 38, 'Fantasy': 28, 
#'Science-fiction': 22, 'Horror': 19, 'Crime': 18, 'Documentary': 12, 
#'History': 8, 'War': 7}

#draw the pie chart
import matplotlib.pyplot as plt
explode=[0,0,0,0,0,0,0.05,0.1,0.15,0.2]
colors=["gold","salmon","mediumpurple","royalblue","mediumaquamarine","teal","darkkhaki","lightslategrey","lightpink","sandybrown"]
plt.pie(students_number,labels=Movie_genre,colors=colors,explode=explode,autopct="%0.1f%%",startangle=90)
plt.show()

#print number of students for a given genre
print("available movie genre: ",Movie_genre)
X=input()
print(favourite_movie_generes[X],"students prefer",X)
