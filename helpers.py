from printing import print_in_color



def cleanse(text: str) -> str:
    return text.lower().strip()


def get_user_choice() -> str:
    print_in_color("Which direction wouldst thee liketh to traverse?", "purple")
    return cleanse(input())
