#12322222222222222222
import qrcode
import Image


for i in range(1,5):
    id= raw_input("Input your id plz")
    if id != '0' :    
        id = '44170' + id
        img = qrcode.make( id )
        img.show()
    else :
        break

print('ok')
