from Postcard.Postcard import *


result = Postcard("triangle_mask_closed", {"backGround" : Image.open("Images/tryPhoto.png"), "color": "orange", "text": "Приглашаем на Пик IT 2021"})
result.create_result_post()
result.save('Images/prosbaArtyoma.png')

