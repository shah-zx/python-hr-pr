from traceback import print_tb


# def print_names(a, b, c, d):
#     print(a, b, c, d)


# print_names("hamza", "shanu", "rahul", "saurav")

# In the above given function if we pass more than the given args then it will throw error :

# For that purpose we can use args :


def print_name(*args, **kwargs):
    for i in args:
        print(i)
    for key, val in kwargs.items():
        print(key, val)


har = ["hamza", "shanu", "rahul", "saurav", "shivam", "kailash"]
kw = {"bmw": "Excellent", "audi": "Very good", "honda": "good"}
print_name(*har)
print_name(*kw)


