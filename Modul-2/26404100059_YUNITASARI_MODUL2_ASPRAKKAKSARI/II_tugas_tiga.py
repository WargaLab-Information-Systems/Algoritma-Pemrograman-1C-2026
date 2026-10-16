suhu = float(input('masukkan suhu reaktor (c): '))
tekanan = float(input('masukkan tekanan gas (bar): '))

if suhu > 1000:
    if tekanan > 50:
      print('MELTDOWN! SEGERA AVAKUASI')
    else:
      print('bahaya suhu, segera turunkan daya')   
elif suhu <= 500:
    if tekanan >30:
     print('tekanan tidak stabil')
    else:
     print('operasi reaktor normal')
else: 
  print('reaktor belum cukkup panas')

status_pompa = 'pompa maksimal' if suhu > 800 else 'pompa normal'
print('status pompa: ', status_pompa)
