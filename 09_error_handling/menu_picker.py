from pick import pick

def menu_picker(options, title = "Select An Option", indicator = "->", default_index = 0):
     option, index = pick(options, title, indicator='=>', default_index=0)
     return index;