from utils.emots.core import convert_emojis_vn, convert_emoticons_vn, remove_emoji, remove_emoticons

# Ham convert_emojis_vn(text) chuyen mot so emoji pho bien thanh van ban tieng viet
text = "Hello ❤️, tat ca moi nguoi"
res = convert_emojis_vn(text)
print(res)
# Hello thả tim️, tat ca moi nguoi


# Ham convert_emojis_vn(text) chuyen mot so emoticon pho bien thanh van ban tieng viet
text2 = "hello :D :( toi la emoticons"
res2 = convert_emoticons_vn(text2)
print(res2)
# hello vui vẻ buồn toi la emoticons

# Ham remove_emoji(text) xoa toan bo emoji co mat trong doan string
text3 = "Các emoji sau:❤️ 🤩 🇩🇪 sẽ bị loại bỏ"
res3 = remove_emoji(text3)
print(res3)
# Các emoji sau:   sẽ bị loại bỏ


# Ham remove_emoticon(text) xoa toan bo emoji co mat trong doan string
text4 = "Các emoticon sau: :‑) :-)) D‑': sẽ bị loại bỏ"
res4 = remove_emoticons(text4)
print(res4)
# Các emoticon sau:   sẽ bị loại bỏ
