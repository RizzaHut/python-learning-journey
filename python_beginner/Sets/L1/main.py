def remove_duplicates(spells):
    # convert method 
    unique_spells = set(spells)
    spell_list = list(unique_spells)

    # looping method 
    set_spells = set()
    list_spells = []
    for spell in spells:
        if spell not in set_spells:
            set_spells.add(spell)

    for spell in set_spells:
        list_spells.append(spell)

    return list_spells

