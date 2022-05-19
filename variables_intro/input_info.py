input_result_name = input("What is your name?\n")  # \n gathers the input in the next line

input_result_fav_movie = input("What is your favourite movie?\n")

input_result_times_watched = input(f"How many times have you watched {input_result_fav_movie}?\n")

input_result_rating = input(f"What rating would you give {input_result_fav_movie}?\n")

print(f"Hello {input_result_name}, welcome. You've told me that your favourite movie is {input_result_fav_movie}, and that you have watched it {input_result_times_watched} times! You also told me that you would give {input_result_fav_movie} a rating of {input_result_rating}")
