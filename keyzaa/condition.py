nilai= int(input('Masukkan nilai: '))
eskul= input('Apakah mengikuti eskul? (ya/tidak): ')

if nilai>90:
  if eskul=="ya":
    nilai_akhir="A+"
else:
    nilai_akhir="A-"
print('nilai anda', nilai_akhir)

