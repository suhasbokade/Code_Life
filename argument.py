my_dict1 = {"Name": "Swami", "age": "29"}
my_dict2 = {"Name": "Bharat", "age": "30"}
print(my_dict1.get("Name"), my_dict1.get("age"))
print(my_dict2.get("Name"), my_dict2.get("age"))


def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["PYTHON", "C++", "DBMS", "INDIA"])
print("\nLongest word:", result[1])
print("Lenght of the longest word- ", result[0])