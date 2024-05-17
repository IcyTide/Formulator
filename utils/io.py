import json
from collections import defaultdict
from utils.parser import COLUMNS

DELIMITER = "-"
COMMA = ","
SEMICOLON = ";"


def serialize(records):
    result = {}
    for player_id in records:
        result[player_id] = records[player_id][COLUMNS].to_dict(orient="records")

    return result


def unserialize(data: dict):
    records = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
    for player_id in data:
        for target_id in data[player_id]:
            for skill, status in data[player_id][target_id].items():
                skill = tuple(int(e) for e in skill.split(DELIMITER))
                for status_set, timeline in status.items():
                    current_status, snapshot_status, target_status = status_set.split(SEMICOLON)
                    current_status = tuple(
                        tuple(int(e) for e in buffs.split(DELIMITER)) for buffs in current_status.split(COMMA)
                    ) if current_status else tuple()
                    snapshot_status = tuple(
                        tuple(int(e) for e in buffs.split(DELIMITER)) for buffs in snapshot_status.split(COMMA)
                    ) if snapshot_status else tuple()
                    target_status = tuple(
                        tuple(int(e) for e in buffs.split(DELIMITER)) for buffs in target_status.split(COMMA)
                    ) if target_status else tuple()
                    concat_status = (current_status, snapshot_status, target_status)
                    records[player_id][target_id][skill][concat_status] = timeline
    return records
