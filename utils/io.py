from collections import defaultdict

from base.constant import FRAME_PER_SECOND

DELIMITER = "-"
COMMA = ","
SEMICOLON = ";"


def serialize(record, duration):
    duration *= FRAME_PER_SECOND
    result = defaultdict(lambda: defaultdict(list))
    for skill, status in record.items():
        skill = DELIMITER.join(str(e) for e in skill)
        for (current_status, snapshot_status, target_status), timeline in status.items():
            if not (timeline := [t for t in timeline if t[0] < duration]):
                continue
            current_status = COMMA.join(DELIMITER.join(str(e) for e in buff) for buff in current_status)
            snapshot_status = COMMA.join(DELIMITER.join(str(e) for e in buff) for buff in snapshot_status)
            target_status = COMMA.join(DELIMITER.join(str(e) for e in buff) for buff in target_status)
            concat_status = SEMICOLON.join((current_status, snapshot_status, target_status))

            result[skill][concat_status].append(timeline)

    return result
