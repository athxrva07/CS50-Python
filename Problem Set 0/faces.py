def main():
    text=input()
    print(convert(text))

def convert(text):
    text=text.replace(":)", "🙂").replace(":(", "🙁")
    return text

main()
