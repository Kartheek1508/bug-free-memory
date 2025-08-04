with open('something.txt','r') as f:
    text = f.read()

if text.__contains__('twinkle'):
    print('yes it does')

else:
    print('It does not conatain')