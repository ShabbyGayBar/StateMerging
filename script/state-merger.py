import json
import os
from vic3_state_merger import StateMerger

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
merge_file = os.path.join(THIS_DIR, "..", "merge_states.json")
# Determine the game root directory based on the operating system
if os.name == "nt":  # Windows
    game_root_dir = (
        "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Victoria 3\\game"
    )
elif os.name == "posix":  # macOS or Linux
    game_root_dir = os.path.expanduser(
        "~/.local/share/Steam/steamapps/common/Victoria 3/game/"
    )
mod_dir = os.path.join(THIS_DIR, "..", "mod")


def main():
    with open(merge_file, "r", encoding="utf-8") as file:
        merge_dict = json.load(file)

    state_merger = StateMerger(
        game_root_dir,
        mod_dir,
        merge_dict,
    )
    state_merger.merge_state_data(ignoreSmallStates=True, smallStateLimit=4)
    state_merger.merge_misc_data()
    state_merger.merge_loc_data()


if __name__ == "__main__":
    main()
