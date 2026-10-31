def take_magic_damage(health, resist, amp, spell_power):
    max_damage = spell_power * amp
    total_damage = max_damage - resist
    new_health = health - total_damage
    return new_health
