import json
import os.path


def get_config():
    default_path = 'configuration/default.json'

    if os.path.isfile(default_path):
        return json.load(open(default_path))

def _merge_dicts(merge_into, merge_from):
	merged = merge_into.copy()
	merged.update(merge_from)

	return merged
