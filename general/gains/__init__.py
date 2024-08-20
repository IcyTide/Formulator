from base.gain import Gain
from general.buffs.formation import BUFFS as FORMATION_BUFFS
from general.buffs.team import BUFFS as TEAM_BUFFS
from general.skills.formation import SKILLS as FORMATION_SKILLS
from general.skills.team import SKILLS as TEAM_SKILLS


class RealBonusGain(Gain):
    skill_ids = list(TEAM_SKILLS) + list(FORMATION_SKILLS)
    buff_ids = list(TEAM_BUFFS) + list(FORMATION_BUFFS)
