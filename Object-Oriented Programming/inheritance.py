# পিতামাতা ক্লাস (Parent Class)
class SmartDevice:
    def recharge(self):
        print('Eating Electricity 😊')
        print('Electrons are Yummy!')

# Phone ক্লাসটি পিতামাতা ক্লাস থেকে সম্পদ উত্তরাধিকারসূত্রে পেয়েছে
class Phone(SmartDevice):
    def __init__(self, brand, price, network):
        self.brand = brand
        self.price = price
        self.network = network

# Watch ক্লাসটি পিতামাতা ক্লাস থেকে বৈশিষ্ট্য পেয়েছে
class Watch(SmartDevice):
    def __init__(self, brand, price, has_gps):
        self.brand = brand
        self.price = price
        self.has_gps = has_gps

# পিতামাতা থেকে সন্তানদের কার্যাবলী পাওয়া
my_phone = Phone('Apple', 800, 'TMobile')
print("Phone:")
my_phone.recharge()  # পিতামাতা ক্লাস থেকে পাওয়া

my_watch = Watch('Fitbit', 200, False)
print("\nWatch:")
my_watch.recharge()  # পিতামাতা ক্লাস থেকে পাওয়া
