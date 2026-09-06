"""টাস্ক: একটি ডেকোরেটর বানাও double_result নামে। এটি কোনো গাণিতিক ফাংশনের রিটার্ন করা ফলাফলকে দ্বিগুণ ($result * 2$) করে রিটার্ন করবে। দুটি সংখ্যার যোগফল নির্ণয়ের একটি ফাংশনে এই ডেকোরেটরটি অ্যাপ্লাই করে টেস্ট করো।"""


def double_result(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        return original_result * 2
    return wrapper

@double_result
def add(a, b):
    return a + b

final_output = add(5, 10)
print (f"Result after decorator: {final_output}")
