from tools import ATTRIBUTE_TYPE


def empty_function(*args):
    return


class Skill:
    skill_id = 0
    skill_level = 0
    skill_name = ""

    kind_type = None

    physical_damage_base = 0
    magical_damage_base = 0
    physical_damage_rand = 0
    magical_damage_rand = 0

    prepare_frame = 0
    channel_interval = 0
    weapon_damage_cof = 0
    global_damage_factor = 0

    physical_attack_power_gain = 0
    physical_critical_strike_rate = 0
    physical_critical_power_rate = 0
    physical_shield_gain = 0
    magical_attack_power_gain = 0
    magical_critical_strike_rate = 0
    magical_critical_power_rate = 0
    magical_shield_gain = 0
    pve_addition = 0

    physical_call = 0
    magical_call = 0
    surplus_call = 0

    def __init__(self, skill_id, skill_level, skill_name, kind_type, weapon_request):
        self.skill_id = skill_id
        self.skill_level = skill_level
        self.skill_name = skill_name
        self.kind_type = kind_type
        self.weapon_request = weapon_request
        if weapon_request:
            self.weapon_damage_cof = 1024
        self.channel_interval = 16

    @property
    def dwSkillID(self):
        return self.skill_id

    @dwSkillID.setter
    def dwSkillID(self, dwSkillID):
        self.skill_id = dwSkillID

    @property
    def dwLevel(self):
        return self.skill_level

    @dwLevel.setter
    def dwLevel(self, dwLevel):
        self.skill_level = dwLevel

    @property
    def nChannelInterval(self):
        return self.channel_interval

    @nChannelInterval.setter
    def nChannelInterval(self, nChannelInterval):
        self.channel_interval = nChannelInterval

    @property
    def nPrepareFrames(self):
        return self.prepare_frame

    @nPrepareFrames.setter
    def nPrepareFrames(self, nPrepareFrames):
        self.prepare_frame = nPrepareFrames

    @property
    def nWeaponDamagePercent(self):
        return self.weapon_damage_cof

    @nWeaponDamagePercent.setter
    def nWeaponDamagePercent(self, nWeaponDamagePercent):
        if self.weapon_request:
            self.weapon_damage_cof = nWeaponDamagePercent

    def AddAttribute(self, effect_mode, attr_type, param_1, param_2):
        if param_1 is None:
            return

        if attr := ATTRIBUTE_TYPE.get(attr_type):
            setattr(self, attr, param_1)
        elif attr_type == 1:
            self.physical_call += 1
        elif attr_type == 2:
            self.magical_call += 1
        elif attr_type == 3:
            self.surplus_call += 1

    def __getitem__(self, key):
        if key in dir(self):
            return getattr(self, key)
        else:
            return empty_function

    def __setitem__(self, key, value):
        if key in dir(self):
            setattr(self, key, value)


