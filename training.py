import iterativeWeightLearning

file2 = '/home/prateek/BTP/Code/train.txt'
file3 = '/home/prateek/BTP/Code/dev.txt'
file4 = '/home/prateek/BTP/Code/test.txt'
file5 = '/home/prateek/BTP/Code/other.txt'
file1 = '/home/prateek/BTP/Code/allFiles.txt'

other_articles=[]
train_articles = []
development_articles=[]
all_articles=[]

with open(file1) as f:
    data = f.readlines()
    for line in data:
        all_articles.append(line[:-1])

with open(file2) as f:
    data = f.readlines()
    for line in data:
        train_articles.append(line[:-1])

with open(file3) as f:
    data = f.readlines()
    for line in data:
        development_articles.append(line[:-1])

with open(file5) as f:
    data = f.readlines()
    for line in data:
        other_articles.append(line[:-1])

hit_count = 100
total_features_in_vector = 6

iterativeWeightLearning.Learn(all_articles, other_articles, train_articles, development_articles, hit_count, total_features_in_vector)
