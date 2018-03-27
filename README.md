# Menu

Create command-line arrow key selection menus .


Install
-

    pip install Menu

Create the Menu
-

The Menu constructor arguments are all optional. The arguments are options, title, message, prompt, and refresh. Options is a list of tuples consisting of a name and a handler. Refresh is a handler called before showing the menu.

    choices=["Red","Blue"]
	ArrowMenu(options=choices) # customize the options
	ArrowMenu("Title", options=choices) # customize the title
	ArrowMenu(options=choices, arrow="->" ) # customize the user selection indicator
	ArrowMenu(options=choices, search_enabled=refreshHandler) # enable search for long list of options

Open the Menu
-

    menu = ArrowMenu()
    menu.show()

Edit the menu
-

    menu = ArrowMenu()
    menu.options([("new option name", newOptionHandler)])
    menu.title = "Title"
    menu.arrow = ">>"

Testing
-

    pytest
