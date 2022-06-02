from textanalysis.textanalysis import count_words

filePath = "hotel-reviews.txt"

# Count the number of positive words
nb_positive_words = count_words(filePath, ["good","great"])

# Count the number of negative words
nb_negative_words = count_words(filePath, ["bad", "awful"])

print("{} positive words.".format(nb_positive_words))
print("{} negative words.".format(nb_negative_words))
