def take_magic_damage(health, resist, amp, spell_power):
    amp_spell_power = amp * spell_power
    resisted_damage = amp_spell_power - resist
    return health - resisted_damage