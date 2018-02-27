from arrow_menu import ArrowMenu


option = ["red", "blue"]
menu = ArrowMenu("Which pill ?",
                 options=["red", "blue"])
choosen = menu.show()
print("\nYou choose", option[choosen], "\n")
