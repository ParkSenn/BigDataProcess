#!/usr/bin/python3

genre_count = dict()

with open("movies_exp.txt", "rt") as fp:
    for line in fp:
            data = line.split("::")
            genres = data[2]
            genre_list = genres.split("|") # genre를 구분한 리스트
            for genre in genre_list:
                genre = genre.strip() # 양 옆 공백 다 제거
                if genre not in genre_count:
                    genre_count[genre] = 1
                else :
                    genre_count[genre] += 1

with open("movieoutput.txt", "wt") as f:
     for genre, count in genre_count.items():
          f.write(f"{genre} {count}\n")