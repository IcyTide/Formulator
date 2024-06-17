from collections import defaultdict

SLASH = "/"
COMMA = ","
SEMICOLON = ";"


def serialize(records):
    result = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
    for player_id in records:
        for target_id in records[player_id]:
            for skill, status in records[player_id][target_id].items():
                skill = SEMICOLON.join(SLASH.join(str(e) for e in t) for t in skill)
                for (current_status, snapshot_status, target_status), timeline in status.items():
                    if not timeline:
                        continue
                    current_status = COMMA.join(SLASH.join(str(e) for e in buff) for buff in current_status)
                    snapshot_status = COMMA.join(SLASH.join(str(e) for e in buff) for buff in snapshot_status)
                    target_status = COMMA.join(SLASH.join(str(e) for e in buff) for buff in target_status)
                    concat_status = SEMICOLON.join((current_status, snapshot_status, target_status))
                    result[player_id][target_id][skill][concat_status] = timeline

    return result


def unserialize(data: dict):
    records = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
    for player_id in data:
        for target_id in data[player_id]:
            for skill, status in data[player_id][target_id].items():
                skill = tuple(tuple(int(e) for e in t.split(SLASH)) for t in skill)
                for status_set, timeline in status.items():
                    current_status, snapshot_status, target_status = status_set.split(SEMICOLON)
                    current_status = tuple(
                        tuple(int(e) for e in buffs.split(SLASH)) for buffs in current_status.split(COMMA)
                    ) if current_status else tuple()
                    snapshot_status = tuple(
                        tuple(int(e) for e in buffs.split(SLASH)) for buffs in snapshot_status.split(COMMA)
                    ) if snapshot_status else tuple()
                    target_status = tuple(
                        tuple(int(e) for e in buffs.split(SLASH)) for buffs in target_status.split(COMMA)
                    ) if target_status else tuple()
                    concat_status = (current_status, snapshot_status, target_status)
                    records[player_id][target_id][skill][concat_status] = timeline
    return records
