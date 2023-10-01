year="鸡"
name="老胡"
message_content = """
金{0}贺岁，欢乐祥瑞。
给{1}及家人送祝福拜年啦！
""".format(year,name)
print(message_content)

current_year = "虎"
message_receiver = "老王"
message_content = """
金{current_year}贺岁，欢乐祥瑞。
给{message_receiver}及家人送祝福拜年啦！
""".format(current_year,message_receiver)
print(message_content)

name = "老王"
year = "虎"
message_receiver = "老王"
message_content = f"""
金{year}贺岁，欢乐祥瑞。
给{name}及家人送祝福拜年啦！
"""
print(message_content)