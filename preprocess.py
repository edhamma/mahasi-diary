import re
inp=open('diary.in.rst','r')
out=open('diary.rst','w')
for l in inp:
    l=l[:-1]
    if m:=re.match('^([0-9].\s)?(A:|Q:|Answer:|Question:)( .*)',l):
        l=f'{m.group(1) if m.group(1) else ""}**{m.group(2)}** {m.group(3)}'
    elif m:=re.match('^(\s*)(comment|caution|correction|instruction|warning|instruction and encouragement|warning and instruction|encouragement|instructions|correction and encouragement|warning and encouragement|for example|note|test and instruction|test and guidance|attention|teachers encouragement|special note): (.*)',l,re.IGNORECASE):
        pad=m.group(1)
        g1=m.group(2).lower().capitalize()
        g2='\n\n'.join([pad+'    '+_ for _ in m.group(3).split(' | ')])
        l=f'{pad}.. admonition:: {g1}\n\n{g2}\n\n'
    l=re.compile('\((?P<comm>(The yogi|This yogi|Yogi|yogi|This is)([^)]*))\)').sub('*(\g<comm>)*',l)
    #     l=f'{m.group("head")}*({m.group("comm")})*{m.group("tail")}'
    out.write(l+'\n')

