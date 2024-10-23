import json
import os
from typing import Dict, List, Tuple, Literal

from assets.constant import SPECIAL_ENCHANT_MAP
from kungfus import SUPPORT_KUNGFU

path = "../jx3_exp_src"


def build_mapping():
    import pandas as pd
    kungfu2event = {
        kungfu_id: (
            list(kungfu.gains)[0][0], list(kungfu.gains)[1][0], list(kungfu.gains)[2][0],
            list(SPECIAL_ENCHANT_MAP[6].values())[0][0]
        )
        for kungfu_id, kungfu in SUPPORT_KUNGFU.items()
    }

    df = pd.read_csv(os.path.join(path, "settings/skill/skills.tab"), sep="\t", low_memory=False,
                     encoding="utf-8").fillna(0)
    skill2mask = {}
    for row in df.itertuples():
        skill2mask[row.SkillID] = [int(row.SkillEventMask1), int(row.SkillEventMask2)]

    df = pd.read_csv(os.path.join(path, "settings/skill/skillevent.tab"), sep="\t", low_memory=False,
                     encoding="utf-8").fillna(0)
    kungfu2mask = {}
    kungfu2prob = {}
    for kungfu_id, event_ids in kungfu2event.items():
        event_masks = kungfu2mask[kungfu_id] = []
        event_probs = kungfu2prob[kungfu_id] = []
        for event_id in event_ids:
            row = df[df.ID == event_id].iloc[0]
            event_masks.append([int(row.EventMask1), int(row.EventMask2)])
            event_probs.append(int(row.Odds))

    json.dump(kungfu2mask, open("kungfu2mask.json", "w", encoding="utf-8"))
    json.dump(kungfu2prob, open("kungfu2prob.json", "w", encoding="utf-8"))
    json.dump(skill2mask, open("skill2mask.json", "w", encoding="utf-8"))


class Calculator:
    id2kungfu: Dict[str, str]
    id2name: Dict[str, str]

    rows: List[str]
    records: List[Tuple[int, list]]
    counts: Dict[str, Dict[int, int]]
    probs: Dict[str, Dict[int, float]]

    def __init__(self):
        self.kungfu2mask = json.load(open("kungfu2mask.json", "r", encoding="utf-8"))
        self.skill2mask = json.load(open("skill2mask.json", "r", encoding="utf-8"))
        self.kungfu2prob = json.load(open("kungfu2prob.json", "r", encoding="utf-8"))

    def reset(self, rows):
        self.rows = rows

        self.id2kungfu = {}
        self.id2name = {}

        self.records = []
        self.counts = {}
        self.probs = {}

    def prepare(self):
        for row in self.rows:
            columns = row.split("\t")
            if columns[4] == "4":
                details = columns[-1].strip("{").split(",")
                player_id, player_name, kungfu_id = details[0], details[1], details[3]
                self.id2kungfu[player_id] = kungfu_id
                self.id2name[player_id] = player_name
                self.counts[player_id] = {}
            elif columns[4] == "21":
                details = columns[-1].strip("{").split(",")
                self.records.append((int(columns[1]), details))

    def parse(self, tag):
        for frame, details in self.records:
            player_id = details[0]
            if player_id not in self.id2kungfu:
                continue
            react, damage_type = details[2], details[3]
            if react == "1" or damage_type == "2":
                continue

            skill_id = details[4]
            skill_mask_1, skill_mask_2 = self.skill2mask.get(skill_id, (0, 0))
            event_mask_1, event_mask_2 = self.kungfu2mask[self.id2kungfu[player_id]][tag]
            if skill_mask_1 & event_mask_1 or skill_mask_2 & event_mask_2:
                if frame not in self.counts[player_id]:
                    self.counts[player_id][frame] = 0
                self.counts[player_id][frame] += 1

    def calculate(self, tag):
        for player_id, counts in self.counts.items():
            player_name = self.id2name[player_id]
            probs = self.probs[player_name] = {frame: 0 for frame in counts}
            event_prob = self.kungfu2prob[self.id2kungfu[player_id]][tag] / 1024
            for frame, count in counts.items():
                if not count:
                    continue
                probs[frame] += event_prob * count

    def calculate_overlap(self, tag):
        for player_id, counts in self.counts.items():
            player_name = self.id2name[player_id]
            probs = self.probs[player_name] = {frame: 0 for frame in counts}
            event_prob = self.kungfu2prob[self.id2kungfu[player_id]][tag] / 1024
            for frame, count in counts.items():
                if not count:
                    continue
                prob = 1 - (1 - event_prob) ** count
                for i in range(frame, frame + self.duration):
                    if i not in probs:
                        continue
                    probs[i] += (1 - probs[i]) * prob

    def calculate_interval(self, tag):
        for player_id, counts in self.counts.items():
            player_name = self.id2name[player_id]
            probs = self.probs[player_name] = {frame: 1 for frame in counts}
            event_prob = self.kungfu2prob[self.id2kungfu[player_id]][tag] / 1024
            for frame, count in counts.items():
                if not count:
                    continue
                prob = 1 - (1 - event_prob) ** count
                probs[frame] *= prob
                for i in range(frame, frame + self.interval):
                    if i == frame or i not in probs:
                        continue
                    probs[i] *= 1 - prob

    def calculate_hybrid(self, tag):
        self.calculate_interval(tag)
        for player_name, probs in self.probs.items():
            final_probs = {frame: 0 for frame in probs}
            for frame, prob in probs.items():
                if not prob:
                    continue
                for i in range(frame, frame + self.duration):
                    if i not in final_probs:
                        continue
                    final_probs[i] += (1 - final_probs[i]) * prob
            self.probs[player_name] = final_probs

    def __call__(self, file_name, tag: Literal[0, 1, 2, 3] = 0):
        rows = open(file_name, encoding="gbk").readlines()
        self.reset(rows)
        self.prepare()
        self.parse(tag)
        if tag == 0:
            self.duration = 6 * 16
            self.calculate_overlap(tag)
        elif tag == 1:
            self.interval = 40 * 16
            self.calculate_interval(tag)
        elif tag == 2:
            self.calculate(tag)
        elif tag == 3:
            self.duration = 8 * 16
            self.interval = 30 * 16
            self.calculate_hybrid(tag)

        return self.probs


def plot(data):
    import matplotlib.pyplot as plt
    for name, points in data.items():
        xs = list(points)
        xs = [x - xs[0] for x in xs]
        ys = list(points.values())
        print(sum(ys) / len(ys))
        plt.plot(xs, ys, label=name)
    plt.title('Plot of Prob')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # build_mapping()
    calculator = Calculator()
    result = calculator("logs/wf-2.jcl", 3)
    plot(result)
