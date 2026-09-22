def main():
    text = input("")
    print(convert(text))

#replacing the emoticons with emojis
def convert(text):
    text1 = text.replace(":)","🙂")
    return text1.replace(":(","🙁")

main()