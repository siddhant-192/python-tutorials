users = [ {"username": 'seema', "tweets": ["i love chocolate", "i am a student"]}, {"username": 'arush', "tweets": []}, {"username": 'kumal', "tweets": ["India", "Python"]}, {"username": 'sam', "tweets": []}, {"username": 'lokesh', "tweets": ["i am good"]}, ]

fil = list(filter(lambda n:not n["tweets"],users))
print(fil)
filupp=list(map(lambda m:m["username"].upper(),filter(lambda n:not n["tweets"],users))) 
print(filupp)
names=['Rohin','Joe','Alia','Siddhant']
new=list(map(lambda name:f"your name is {name}", filter(lambda x:len x)>=4,names))) 
print(new)