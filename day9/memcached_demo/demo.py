import memcache

#连接之前 一定要先启动 windows 或者Linux的 服务
mc = memcache.Client(['127.0.0.1:11211'],debug=True)
# mc.set('username','jiabin',time=60)
#存字典进去
mc.set_multi({'name':'kangbazi','password':'123abc','age':18},time=120)

username = mc.get('password')
print(username)

mc.delete('name')
username = mc.get('name')
print(username)

mc.incr('age',delta=10)
age = mc.get('age')
print(age)