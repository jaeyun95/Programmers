#(3) 베스트앨범

import operator
def solution(genres, plays):
    answer = []
    genre_lank = dict()
    for index, genre_list in enumerate(zip(genres,plays)):
        if genre_list[0] in genre_lank:
            genre_lank[genre_list[0]][0] += genre_list[1]
            genre_lank[genre_list[0]].append([index,genre_list[1]])
        else: 
            genre_lank[genre_list[0]] = [genre_list[1]]
            genre_lank[genre_list[0]].append([index,genre_list[1]])
    genre_lank = sorted(genre_lank.items(), key=operator.itemgetter(1), reverse=True)
    for genre in genre_lank:
        genre_list = genre[1][1:]
        genre_list.sort(key=operator.itemgetter(1), reverse=True) 
        if len(genre_list) < 2: answer.append(genre_list[0][0])
        else:
            for i in range(2):
                answer.append(genre_list[i][0])
    return answer
	
#다른 코드
'''
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer
'''