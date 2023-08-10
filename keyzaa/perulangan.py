import re;
print('merubah huruf');

listkota=['solo', 'surabaya', 'bekasi', 'jakarta'];
listhurufvokal=['a', 'i', 'u', 'e', 'o'];

for kota in listkota:
    print('[' +kota+ ']');
    for vokal in listhurufvokal:
        print('--->' + re.sub('[aiueo]', vokal, kota));