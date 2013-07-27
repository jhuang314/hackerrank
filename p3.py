
with open('corpus.txt', 'r') as f:
    text = f.readlines()


female = set(['miss', 'mrs.', 'she','herself', 'her'])
male = set(['mr.', 'he', 'him', 'himself', 'his'])

d = 30

T = int(raw_input())
for case in xrange(T):
    name = raw_input()

    fscore = 0
    mscore = 0
    for linum, line in enumerate(text):
        if name in line:
            for i in xrange(linum-d, linum+d):
                scale = 1
                compare = set(x.lower() for x in text[i].split(' '))
                fscore += len(female.intersection(compare)) * scale
                mscore += len(male.intersection(compare)) * scale

    if fscore > mscore:
        print "Female"
    else:
        print "Male"

    print "margin: ", abs(fscore - mscore)

    


    
        
        
