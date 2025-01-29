def linear_search(dictionary, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key  # ভ্যালু পেলে সংশ্লিষ্ট কী রিটার্ন করবে
    return None  # ভ্যালু না পেলে None রিটার্ন করবে

# উদাহরণ ডিকশনারি
data = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}

# টার্গেট ভ্যালু
target = 30

# লিনিয়ার সার্চ
result = linear_search(data, target)

if result:
    print(f"Value {target} found at key '{result}'.")
else:
    print(f"Value {target} not found in the dictionary.")
