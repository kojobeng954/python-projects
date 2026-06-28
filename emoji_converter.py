def emoji_converter(message):
    word = message.split()
    emojis = {
        ":)": "😁",
        ":(": "😔",
        ":*": "😘",
        "XD": "🤣",
        ":|": "😑",
        ";)": "😉",
        ";P": "😜",
    }
    output = ""

    for char in word:
        output += emojis.get(char, char) + " "
        return output


message = input(">>>")
result = emoji_converter(message)
print(result)
