
print("IMPORTED MODULE")

test='Test String'

def find_index(to_search,target):
    for i ,value in enumerate(to_search):
        if value== target:
            return 1
    return -1