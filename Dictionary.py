dic = {'name':'thasneem',"sduty":'python','sub':'dictinory','list':[100,900,80]}

'''print(dic)
print(dic['name'])
dic ['name'] ='MT'
del dic['sduty']'''

#a = dic.get('name')
#a = dic.clear()
a = dic.copy()

a['list'].append(300)

print(a)
print(dic)