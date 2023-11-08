info = {
    "name": "navneet",
    "age": 19,
    "eligible": True
}
# print(info)
# print(info["name"])
# print(info.get("age"))
# print(info.values())
# print(info.keys())
# for key in info.keys():
#     print(f"The value for the key {key} is {info[key]}")
# print(info.items())
for key, value in info.items():
    print(f"The value for the key {key} is {value}")
