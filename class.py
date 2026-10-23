class Whatsapp_v1:
    chat_feature = "Available"
    vc_feature = "Not Available"

class Whatsapp_v2:
    vc_feature = "Available"

class Facebook_v1:
    sharing_facebook = "Available"

class Whatsapp_v3( Whatsapp_v2,Whatsapp_v1):
    status_feature = "Available"

user = Whatsapp_v3()
res=user.vc_feature

print(res) 

