import re
inp=open('diary.in.rst','r')
out=open('diary.rst','w')
for l in inp:
    l=l[:-1]
    if m:=re.match('^(A:|Q:|Answer:|Question:)( .*)',l):
        l=f'**{m.group(1)}** {m.group(2)}'
    elif m:=re.match('^(comment|caution|correction|instruction|warning|instruction and encouragement|warning and instruction|encouragement|instructions|correction and encouragement|warning and encouragement|for example|note|test and instruction|test and guidance|attention|teachers encouragement|special note): (.*)',l,re.IGNORECASE):
        g1=m.group(1).lower().capitalize()
        g2='\n\n'.join(['    '+_ for _ in m.group(2).split(' | ')])
        l=f'.. admonition:: {g1}\n\n{g2}\n\n'
    l=re.compile('\((?P<comm>(The yogi|This yogi|Yogi|yogi|This is)([^)]*))\)').sub('*(\g<comm>)*',l)
    #     l=f'{m.group("head")}*({m.group("comm")})*{m.group("tail")}'
    out.write(l+'\n')

