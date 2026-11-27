from textnode import TextType, TextNode


def main():
    link = TextType.LINK
    dummy = TextNode("anchor text", link, "https://www.boot.dev")
    print(dummy)


if __name__ == "__main__":
    main()
