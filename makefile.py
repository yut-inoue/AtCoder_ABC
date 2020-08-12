import os
# n=input()
n="072"
contest_name="ABC"+n
rank_list=['A','B','C']
os.makedirs(contest_name,exist_ok=False)
for rank in rank_list:
    pyfile="{0}_{1}.py".format(contest_name,rank)
    f = open('{0}/{1}'.format(contest_name,pyfile),'w')
    f.write('')
    f.close()
