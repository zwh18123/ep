#12322222222222222222
import qrcode
import Image
id= raw_input("Input your id plz")
id = '44170' + id
print(id)
#fsdfasdwhile 1:
if id != 0 :
    img = qrcode.make( id )
    img.show()
else :
    print(id)

print('ok')
