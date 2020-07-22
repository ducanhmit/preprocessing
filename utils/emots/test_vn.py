from .core import convert_emojis_vn, convert_emoticons_vn, convert_emojis

text = "Hello ❤️, tat ca moi nguoi"

res = convert_emojis_vn(text)
print(res)

text2 = "hello :D :( toi la emoticons"
res2 = convert_emoticons_vn(text2)
print(res2)