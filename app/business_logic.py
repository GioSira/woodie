
def compute_scores_od(user_id, date, form):

    d1 = form.getlist("d1")

    d2_1 = form.get("d2_1")
    d2_2 = form.get("d2_2")
    d2_3 = form.get("d2_3")
    d2_4 = form.get("d2_4")
    d2_5 = form.getlist("d2_5")
    d2_6 = form.get("d2_6")
    d2_7 = form.get("d2_7")
    d2_8 = form.get("d2_8")

    d3_1 = form.get("d3_1")
    d3_2 = form.get("d3_2")

    d4 = form.get("d4")

    d5 = form.get("d5")

    d = {"user_id": user_id, "created_at": date}

    if "d1.a" in d1:
        d["d1_1"] = 10
    else:
        d["d1_1"] = 0
    if "d1.b" in d1:
        d["d1_2"] = 10
    else:
        d["d1_2"] = 0
    if "d1.c" in d1:
        d["d1_3"] = 5
    else:
        d["d1_3"] = 0
    if "d1.d" in d1:
        d["d1_4"] = 5
    else:
        d["d1_4"] = 0

    if d2_1 == "d2_1.a":
        d["d2_1"] = 10
    elif d2_1 == "d2_1.b":
        d["d2_1"] = 5
    else:
        d["d2_1"] = 0

    if d2_2 == "d2_2.a":
        d["d2_2"] = 5
    elif d2_2 == "d2_2.b":
        d["d2_2"] = 3
    else:
        d["d2_2"] = 0

    if d2_3 == "d2_3.a":
        d["d2_3"] = 5
    else:
        d["d2_3"] = 0

    if d2_4 == "d2_4.a":
        if "d2_5.a" in d2_5:
            d["d2_4_1"] = 2
        else:
            d["d2_4_1"] = 0
        if 'd2_5.b' in d2_5:
            d["d2_4_2"] = 2
        else:
            d["d2_4_2"] = 0
        if "d2_5.c" in d2_5:
            d["d2_4_3"] = 2
        else:
            d["d2_4_3"] = 0
        if "d2_5.d" in d2_5:
            d["d2_4_4"] = 2
        else:
            d["d2_4_4"] = 0
        if "d2_5.e" in d2_5:
            d["d2_4_5"] = 2
        else:
            d["d2_4_5"] = 0
    else:
        d["d2_4_1"] = 0
        d["d2_4_2"] = 0
        d["d2_4_3"] = 0
        d["d2_4_4"] = 0
        d["d2_4_5"] = 0

    if d2_6 == "d2_6.a":
        d["d2_5"] = 5
    else:
        d["d2_5"] = 0

    if d2_7 == "d2_7.a":
        d["d2_6"] = 5
    else:
        d["d2_6"] = 0

    if d2_8 == "d2_8.a":
        d["d2_7"] = 5
    else:
        d["d2_7"] = 0

    if d3_1 == "d3_1.a":
        d["d3_1"] = 5
    else:
        d["d3_1"] = 0

    if d3_2 == "d3_2.a":
        d["d3_2"] = 10
    else:
        d["d3_2"] = 0

    if d4 == "d4.a":
        d["d4"] = 5
    else:
        d["d4"] = 0

    if d5 == "d5.a":
        d["d5"] = 5
    else:
        d["d5"] = 0

def compute_scores_wb(user_id, date, form):

    d6 = form.get("d6")

    d7 = form.get("d7")

    d8 = form.get("d8")

    d9 = form.getlist("d9")

    d10 = form.get("d10")

    d11 = form.get("d11")

    d12 = form.getlist("d12")

    d13 = form.get("d13")

    d14 = form.get("d14")

    d15 = form.get("d15")

    d16 = form.get("d16")

    d17 = form.get("d17")

    d18 = form.get("d18")

    d19 = form.get("d19")

    d20 = form.get("d20")

    d21 = form.get("d21")

    d22 = form.get("d22")

    d23 = form.get("d23")

    d = {"user_id": user_id, "created_at": date}

    d["d6_1"] = 0
    d["d6_2"] = 0
    d["d6_3"] = 0
    d["d6_4"] = 0
    if d6 == "d6.a":
        d["d6_1"] = 10
    if d6 == "d6.b":
        d["d6_2"] = 10
    if d6 == "d6.c":
        d["d6_3"] = 3
        if d7 == "d7.a":
            d["d6_4"] = 3

    if d8 == "d8.a":
        d["d7"] = 2
    else:
        d["d7"] = 4

    if "d9.a" in d9:
        d["d8_1"] = 2
    else:
        d["d8_1"] = 0
    if "d9.b" in d9:
        d["d8_2"] = 2
    else:
        d["d8_2"] = 0
    if "d9.c" in d9:
        d["d8_3"] = 2
    else:
        d["d8_3"] = 0
    if "d9.d" in d9:
        d["d8_4"] = 1
    else:
        d["d8_4"] = 0

    if d10 == "d10.a":
        d["d9"] = 2
    else:
        d["d9"] = 1

    if d11 == 'd11.a':
        if 'd12.a' in d12:
            d["d10_1"] = 3
        else:
            d["d10_1"] = 0
        if 'd12.b' in d12:
            d["d10_2"] = 3
        else:
            d["d10_2"] = 0
        if 'd12.c' in d12:
            d["d10_3"] = 3
        else:
            d["d10_3"] = 0
    else:
        d["d10_1"] = 0
        d["d10_2"] = 0
        d["d10_3"] = 0

    if d13 == "d13.a":
        d["d11"] = 3
    else:
        d["d11"] = 6

    if d14 == "d14.a":
        d["d12"] = 10
    elif d14 == "d14.b":
        d["d12"] = 3
    else:
        d["d12"] = 0

    if d15 == "d15.a":
        d["d13"] = 8
    else:
        d["d13"] = 0

    if d16 == "d16.a":
        d["d14"] = 4
    else:
        d["d14"] = 0

    if d17 == "d17.a":
        d["d15"] = 5
    elif d17 == "d17.b":
        d["d15"] = 2
    else:
        d["d15"] = 0

    if d18 == "d18.a":
        d["d16"] = 5
    else:
        d["d16"] = 0

    if d19 == "d19.a":
        d["d17"] = 5
    else:
        d["d17"] = 0

    if d20 == "d20.a":
        d["d18"] = 10
    else:
        d["d18"] = 0

    if d21 == "d21.a":
        d["d19"] = 5
    else:
        d["d19"] = 0

    if d22 == "d22.a":
        d["d20"] = 5
    else:
        d["d20"] = 0

    if d23 == "d23.a":
        d["d21"] = 5
    else:
        d["d21"] = 0

    return d
