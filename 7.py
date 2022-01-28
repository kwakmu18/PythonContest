if __name__ == '__main__':
    records=[]
    scores=set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.add(score)
        records.append([name, score])
    records=sorted(records, key=lambda x:(x[1], x[0]))
    scores=sorted(scores)
    if len(scores)==1: seclow=0
    else:seclow=1
    for i in records:
        if i[1]==scores[seclow]:print(i[0])