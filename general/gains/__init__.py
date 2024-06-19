from typing import Dict

from base.buff import Buff
from base.gain import Gain
from base.skill import Skill
from general.buffs.formation import BUFFS as FORMATION_BUFFS
from general.buffs.formation import GAINS as FORMATION_GAINS
from general.buffs.team import BUFFS as TEAM_BUFFS
from general.buffs.team import GAINS as TEAM_GAINS
from general.skills.formation import SKILLS as FORMATION_SKILLS
from general.skills.team import SKILLS as TEAM_SKILLS


class RealBonusGain(Gain):
    skill_ids = list(TEAM_SKILLS) + list(FORMATION_SKILLS)
    buff_ids = list(TEAM_BUFFS) + list(FORMATION_BUFFS)

    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.skill_ids:
            skills[skill_id].activate = True

    def add_buffs(self, buffs: Dict[int, Buff]):
        for buff_id in self.buff_ids:
            buffs[buff_id].activate = True

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.skill_ids:
            skills[skill_id].activate = False

    def sub_buffs(self, buffs: Dict[int, Buff]):
        for buff_id in self.buff_ids:
            buffs[buff_id].activate = False


GENERAL_GAINS: Dict[int, Buff] = {
    **FORMATION_GAINS,
    **TEAM_GAINS
}
