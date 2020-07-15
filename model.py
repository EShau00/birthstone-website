# Month-to-Gemstone global dictionary
month_to_gemstone = {
    "january":"garnet",
    "february":"amethyst",
    "march":"aquamarine",
    "april":"diamond",
    "may":"emerald",
    "june":"pearl",
    "july":"ruby",
    "august":"peridot",
    "september":"sapphire",
    "october":"opal",
    "november":"citrine",
    "december":"topaz",
}

# Matches months to gemstone
def find_gemstone(month):
    return month_to_gemstone[month]

# Makes a data ditionary
def find_data(first_name, month):
    data= {
        "first_name":first_name,
        "month":month,
        "gemstone":find_gemstone(month)
    }
    for item in data:
        data[item] = data[item].capitalize()
    return data