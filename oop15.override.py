class parentclass():
    def send_message(self):
        print("bu alan icerisinde mesaj verilecektir.")

class baseclass(parentclass):
    pass

parent = parentclass()
parent.send_message()

base = baseclass()
base.send_message()

#bu alan icerisinde mesaj verilecektir.
#bu alan icerisinde mesaj verilecektir.





