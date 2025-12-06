def calculate_love_score(name_1, name_2):
    combined_names = (name_1 + name_2).lower()

    t = combined_names.count("t")
    r = combined_names.count("r")
    u = combined_names.count("u")
    e = combined_names.count("e")
    first_half_count = t + r + u + e

    l = combined_names.count("l")
    o = combined_names.count("o")
    v = combined_names.count("v")
    e = combined_names.count("e")
    second_half_count = l + o + v + e

    total_score = int (str(first_half_count) + str(second_half_count))
    print(total_score)


calculate_love_score("Kanye West", "Kim Kardashian")