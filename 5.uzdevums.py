from datetime import datetime

tagad_stunda = datetime.now().hour

if 5 <= tagad_stunda < 12:
    sveiciens= 'labrīt'
elif 12 <= tagad_stunda < 18:
    sveiciens= 'labdien'
else:
    sveiciens= 'labvakar'


print(sveiciens)