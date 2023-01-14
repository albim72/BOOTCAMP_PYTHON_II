from simplebucket import Bucket,fill,deduct

print("______zbiornik danych nr 1_______")
bucket = Bucket(60)
print(bucket)
fill(bucket,100)
print(bucket)

if deduct(bucket,99):
    print('potrzebne 99 jednostek')
else:
    print('nie ma 99 jednostek')
print(bucket)

if deduct(bucket,3):
    print('potrzebne 3 jednostek')
else:
    print('nie ma 3 jednostek')
print(bucket)

print("______zbiornik danych nr 2 [nowa wersja] _______")
