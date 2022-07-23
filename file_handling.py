# f = open('filehandling.txt','a')
# f.write('results mathematical wrong\n')

# f = open('files', 'w')

f =open('IMG_1824.JPG', 'rb')
f1 = open('my pic.JPG','wb')

for i in f:
    f1.write(i)