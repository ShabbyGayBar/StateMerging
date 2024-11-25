# Victoria 3 States Merging Mod

![Steam Views](https://img.shields.io/steam/views/3371693463?style=flat&logo=steam&label=steam)

[简体中文](README_zh-CN.md)

Pretty self-explanatory mod name. This mod combines multiple states in the game Victoria 3 together while keeping the overall pop & buildings unchanged.

Barracks & naval base cap as well as taxation which were reduced due to less number of states will be compensated (partially) by granting state buffs.

Speaking of buffs, they were given according to how many vanilla states they merged, except several ultra-minor states that don't deserve being a state at all (no offense).

Merged states WILL LOSE THEIR CITY & BUILDING MODELS.

Merged states WILL LOSE THEIR STATE ID, which may cause problems with certain journal entries and such. please report issues when you encounter them.

## Which states will be merged

The following criteria are sorted by significance:

- **Province Numbers**: 
  - Any state with provinces less than 10 shall be merged.
  - States with 10-20 provinces will be considered for merging.
  - States with <5 provinces won't be counted as a state when giving buffs.

- **Historical & cultural ties**
  - States that belong to different nations today will not be merged unless the above conditions are met.
  - States with similar cultural homelands are more likely to be merged.

- **Aesthetics**

## Changelog

Please refer to [merge_states.json](merge_states.json) for all the changes in states.

The keys of the json are the state id of the existing states in the mod, and the values are lists of state ids in vanilla game that will be merged into the key state.

## Compatability

Incompatible with anything that modifies
- game\common\history\buildings\
- game\common\history\pops\
- game\common\history\states\
- game\map_data\state_regions\

<details>

<summary>Other modified files that doesn't affect gameplay as much</summary>

- game\common\ai_strategies\00_default_strategy.txt
- game\common\buildings\11_private_infrastructure.txt
- game\common\company_types\
- game\common\country_definitions\00_countries.txt
- game\common\customizable_localization\02_events.txt
- game\common\decisions\manifest_destiny.txt
- game\common\history\global\00_global.txt
- game\common\history\military_formations\
- game\common\journal_entries\
- game\common\scripted_triggers\00_scripted_triggers.txt
- game\events\native_resettlement.txt
- game\events\oregon_events.txt

</details>

## Acknowledgments

Special thanks to user [思考的肺结核](https://steamcommunity.com/profiles/76561198104682926) who wrote the [original version](https://steamcommunity.com/sharedfiles/filedetails/?id=3254683348) of this mod.

## License

This mod is under [MIT LICENSE](LICENSE).
