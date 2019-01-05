d={"1":5,"test":"home","ele":None}

d.update(**{"2":4})

#创建字典的特殊方式,传入iterable
seq = ('Google', 'Runoob', 'Taobao')
d=dict.fromkeys(seq)
d2=dict.fromkeys(seq,'')


from collections import OrderedDict