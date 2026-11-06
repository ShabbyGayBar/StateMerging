import argparse
import json
import os

from vic3_state_merger import ASSETS, StateMerger
from vic3_state_merger.logging_config import configure_logging

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
    parser = argparse.ArgumentParser(
        description="Rebuild States Merging, including spline topology."
    )
    parser.add_argument(
        "--game-root", default=os.environ.get("VIC3_GAME_ROOT", game_root_dir)
    )
    parser.add_argument("--output", default=mod_dir)
    parser.add_argument("--data-dir", default=os.path.join(THIS_DIR, "..", "data"))
    parser.add_argument(
        "--log-level",
        choices=("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"),
        default="INFO",
        help="Diagnostic verbosity for stderr and the optional log file (default: INFO).",
    )
    parser.add_argument(
        "--log-file", help="Also save diagnostics to a rotating UTF-8 log file."
    )
    args = parser.parse_args()
    configure_logging(args.log_level, log_file=args.log_file)
    with open(merge_file, "r", encoding="utf-8") as file:
        merge_dict = json.load(file)

    state_merger = StateMerger(
        args.game_root,
        args.output,
        merge_dict,
        args.data_dir,
    )
    state_merger.run(
        integration_traits=True,
        assets=ASSETS,
        ignore_small_states=True,
        small_state_limit=4,
    )
    result = state_merger.spline_result
    return 3 if result is not None and result.status == "draft" else 0


if __name__ == "__main__":
    raise SystemExit(main())
