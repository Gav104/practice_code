import os
import csv


path = "C:/Users/Gavin/PycharmProjects/Practice_code"

high_scores_dict = {}
in_file_path = os.path.join(path, "scores.csv")
out_file_path = os.path.join(path, "highest_scores.csv")


with open(in_file_path, "r") as myFile, open(out_file_path, "w", newline="") as out_file:
    my_file_reader = csv.reader(myFile)
    for name, score in my_file_reader:  # get each name/score pair
        score = int(score)  # convert string score to integer
        if name in high_scores_dict:  # already had an entry for that name
            if score > high_scores_dict[name]:  # new score is higher
                high_scores_dict[name] = score
        else:  # haven't seen this name yet; add it to dictionary
            high_scores_dict[name] = score

    for name in sorted(high_scores_dict):
        guess = name, high_scores_dict[name]
        print(name, high_scores_dict[name])

        writer = csv.writer(out_file)
        writer.writerows([guess])

