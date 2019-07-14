class parentclass():
    def send_message(self):
        print("bu alan icerisinde mesaj verilecektir.")

class baseclass(parentclass):
    def send_message(self):
        print("base class uzerinden gelen mesaj")

parent = parentclass()
parent.send_message()

base = baseclass()
base.send_message()

#bu alan icerisinde mesaj verilecektir.
#base class uzerinden gelen mesaj





