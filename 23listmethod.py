l= [11,45,1,2,4,6]
print(l)

# append() list ke aakhiri (end) mein ek naya element jod deta hai
l.append(7)
print(l)

# sort() saare numbers ko chote se bada (Ascending order) kar deta hai
l.sort()
print(l)

# sort(reverse=True) numbers ko bade se chota (Descending order) kar deta hai
l.sort(reverse=True)
print(l)

# reverse() list ke order ko bilkul ulta (piche se aage) kar deta hai
l.reverse()
print(l)

# index() batata hai ki koi element pehli baar kis position (index) par aaya hai
print(l.index(1))

# count() ginta hai ki koi number list mein kul kitni baar aaya hai
print(l.count(1))

# copy() ek bilkul nayi aur alag list banata hai. 
# Ab 'm' mein badlav karne se asli list 'l' par koi asar nahi padega.
m=l.copy()
m[0]=0
print(l)

# insert(index, element) kisi bhi specific jagah par naya number daalne ke liye hai
# Yahan index 1 par 899 aa jayega aur baaki numbers aage khisak jayenge
l.insert(1,899)
print(l)

m=[900,100,198]
# extend() ek poori list ko doosri list ke piche jod deta hai, jisse 'l' change ho jati hai
l.extend(m)
print(l)

# k=l+m 
# print(k)  # Harry sir ne bataya tha ki '+' karne se ek nayi list 'k' banti hai, asli 'l' safe rehti hai