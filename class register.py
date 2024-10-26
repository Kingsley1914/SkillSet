h=[]

s = input('enter how many enteries you will make\n')
o=int(s)
for n in range(o):
    b=input('enter data\n')
    x=open('exam.txt','a')
    x.write(b+'\n')
    x.close()
l=open('exam.txt')
def scores():
  for d in l:
      #d.replace('\n', '')
      t=d.split(':')
      q=t[1]
      q = int(q.replace('\n',''))
      w=h.append(q)

def total_score():
    tr=sum(h)
    pl=print(tr)
def highest():
    aq=max(h)
    print(aq)
def average():
    i=sum(h)
    m=len(h)
    sd=m * i
    print(sd)
def ret_score():
    re = input('enter name\n')
    for v in l:
      v.startswith(re)
      print(v)
def lowest():
    sa = min(h)
    print(sa)
scores()
while True:
    will = input('please enter any of our entery selection\n, 1 for totalscore\n, 2 for showing the highest score\n, 3 for average\n, 4 for retriving a score\n, 5 for showing the lowest score\n, 6 for quiting the process\n')
    if will == '1':
      total_score()
    if will == '2':
      highest()
    if will == '3':
      average()
    if will == '4':
      ret_score()
    if will == '5':
        lowest()
    if will == '6':
        break
