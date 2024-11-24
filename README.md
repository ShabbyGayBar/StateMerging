# Victoria 3 States Merging Mod

[简体中文](README_zh-CN.md)

Pretty self-explanatory mod name. This mod combines multiple states in the game Victoria 3 together while keeping the overall pop & buildings unchanged. Barracks & naval base cap as well as taxation which were reduced due to less number of states will be compensated (partially) by granting state buffs.

Speaking of buffs, they were given according to how many vanilla states they merged, except several ultra-minor states that don't deserve being a state at all (no offense).

Merged states WILL LOSE THEIR CITY & BUILDING MODELS.

Merged states WILL LOSE THEIR STATE ID, which may cause problems with certain journal entries and such. please report issues when you encounter them.

## Which states will be merged

The following standards are sorted by significance:

- **Gaming performance**
- **Historical & cultural**
- **Outlook**

## Changelog

Please refer to [merge_states.json](merge_states.json) for all the changes in states.

The keys of the json are the state id of the existing states in the mod, and the values are lists of state ids in vanilla game that will be merged into the key state.

<details>

<summary>Update history</summary>

- 2024-11-21: Initial release

</details>

## Compatability

Incompatible with anything that modifies
- game\common\history\buildings
- game\common\history\pops
- game\common\history\states
- game\map_data\state_regions

## Contributors

Special thanks to user [思考的肺结核](https://steamcommunity.com/profiles/76561198104682926) who wrote the [original version](https://steamcommunity.com/sharedfiles/filedetails/?id=3254683348) of this mod.

## License

This mod is under [MIT LICENSE](LICENSE).
