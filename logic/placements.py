from typing import Any, List
from .constants import *
from .logic import Placement

# Single crystals
SINGLE_CRYSTAL_CHECKS = [
    "Knight Academy - Crystal in Link's Room",
    "Knight Academy - Crystal in Knight Academy Plant",
    "Knight Academy - Crystal in Zelda's Room",
    "Sparring Hall - Crystal",
    "Central Skyloft - Crystal between Wooden Planks",
    "Central Skyloft - Crystal on West Cliff",
    "Central Skyloft - Crystal in Orielle and Parrow's House",
    "Central Skyloft - Crystal on Light Tower",
    "Skyloft Village - Crystal near Pumpkin Patch",
    "Central Skyloft - Crystal after Waterfall Cave",
    "Central Skyloft - Crystal in Loftwing Prison",
    "Central Skyloft - Crystal on Waterfall Island",
    "Lumpy Pumpkin - Outside Crystal",
    "Lumpy Pumpkin - Inside Crystal",
    "Beedle's Island - Crystal",
]


# Tries to force an item to its vanilla location.
# Produces an error if this is not possible.
def norm_force_vanilla(list: List[str]):
    def norm_keys(norm: Callable[[str], EIN], checks: Dict[EIN, Any]) -> Placement:
        list2 = map(norm, list)
        dict = {k: EIN(checks[k]["original item"]) for k in list2}
        return Placement(locations=dict, items={v: k for k, v in dict.items()})

    return norm_keys


# Restricts an item to only be placeable in its vanilla location.
# This is always possible.
def norm_restrict_vanilla(locations: List[str]):
    def norm_keys(norm: Callable[[str], EIN], checks: Dict[EIN, Any]) -> Placement:
        locs2 = map(norm, locations)
        restriction = {EIN(checks[loc]["original item"]): loc for loc in locs2}
        return Placement(item_placement_limit=restriction)

    return norm_keys


SINGLE_CRYSTAL_PLACEMENT = norm_force_vanilla(SINGLE_CRYSTAL_CHECKS)


def norm_keys(dict: Dict[str, EIN]):
    def norm_keys(norm: Callable[[str], EIN]) -> Placement:
        dict2 = {norm(k): v for k, v in dict.items()}
        return Placement(locations=dict2, items={v: k for k, v in dict2.items()})

    return norm_keys


def norm_values(dict: Dict[EIN, str]):
    def norm_values(norm: Callable[[str], EIN]):
        dict2 = {k: norm(v) for k, v in dict.items()}
        return Placement(item_placement_limit=dict2)

    return norm_values


HARDCODED_PLACEMENT = norm_keys({})

BEEDLE_CHECKS = [
    "Beedle's Shop - 300 Rupee Item",
    "Beedle's Shop - 600 Rupee Item",
    "Beedle's Shop - 1200 Rupee Item",
    "Beedle's Shop - 800 Rupee Item",
    "Beedle's Shop - 1600 Rupee Item",
    "Beedle's Shop - First 100 Rupee Item",
    "Beedle's Shop - Second 100 Rupee Item",
    "Beedle's Shop - Third 100 Rupee Item",
    "Beedle's Shop - 50 Rupee Item",
    "Beedle's Shop - 1000 Rupee Item",
]
VANILLA_BEEDLE_PLACEMENT = norm_force_vanilla(BEEDLE_CHECKS)

SMALL_KEY_CHECKS = [
    "Skyview Temple - Chest behind Two Eyes",
    "Skyview Temple - Chest behind Three Eyes",
    "Lanayru Mining Facility - First Chest in Hub Room",
    "Ancient Cistern - Chest in East Part",
    "Ancient Cistern - Bokoblin",
    "Sandship - Chest behind Combination Lock",
    "Sandship - Robot in Brig's Reward",
    "Fire Sanctuary - Chest in First Room",
    "Fire Sanctuary - Chest near First Trapped Mogma",
    "Fire Sanctuary - Chest after Bombable Wall",
    "Sky Keep - Chest after Dreadfuse",
    "Lanayru Caves - Golo's Gift",
]
VANILLA_SMALL_KEYS_PLACEMENT = norm_restrict_vanilla(SMALL_KEY_CHECKS)

DUNGEON_SMALL_KEYS_RESTRICTION = norm_values(
    {
        number(SMALL_KEY[SV], 0): SV + sep + "Main",
        number(SMALL_KEY[SV], 1): SV + sep + "Main",
        number(SMALL_KEY[LMF], 0): LMF + sep + "Main",
        number(SMALL_KEY[AC], 0): AC + sep + "Main",
        number(SMALL_KEY[AC], 1): AC + sep + "Main",
        number(SMALL_KEY[SSH], 0): SSH + sep + "Main",
        number(SMALL_KEY[SSH], 1): SSH + sep + "Main",
        number(SMALL_KEY[FS], 0): FS + sep + "Main",
        number(SMALL_KEY[FS], 1): FS + sep + "Main",
        number(SMALL_KEY[FS], 2): FS + sep + "Main",
        number(SMALL_KEY[SK], 0): SK,
    }
)

CAVES_KEY_RESTRICTION = norm_values({CAVES_KEY: "Lanayru - Caves"})


BOSS_KEY_CHECKS = [
    "Skyview Temple - Chest after Vines",
    "Earth Temple - Chest before Boulder Chase",
    "Lanayru Mining Facility - Chest after Double Armos Fight",
    "Ancient Cistern - Chest under Stone Statue",
    "Sandship - Chest in Captain's Cabin",
    "Fire Sanctuary - Chest after Winged Torches",
]
VANILLA_BOSS_KEYS_PLACEMENT = norm_restrict_vanilla(BOSS_KEY_CHECKS)

DUNGEON_BOSS_KEYS_RESTRICTION = norm_values(
    {
        BOSS_KEY[SV]: SV,
        BOSS_KEY[ET]: ET,
        BOSS_KEY[LMF]: LMF,
        BOSS_KEY[AC]: AC,
        BOSS_KEY[SSH]: SSH,
        BOSS_KEY[FS]: FS,
    }
)

MAP_CHECKS = [
    "Skyview Temple - Chest on Tree Branch",
    "Earth Temple - Chest in West Room",
    "Lanayru Mining Facility - Chest after Armos Fight",
    "Ancient Cistern - Chest after Whip Hooks",
    "Sandship - Chest before 4-Door Corridor",
    "Fire Sanctuary - Rescue Second Trapped Mogma Chest",
    "Sky Keep - First Chest",
]
VANILLA_MAPS_PLACEMENT = norm_restrict_vanilla(MAP_CHECKS)

DUNGEON_MAPS_RESTRICTION = norm_values(
    {
        MAP[SV]: SV,
        MAP[ET]: ET,
        MAP[LMF]: LMF,
        MAP[AC]: AC,
        MAP[SSH]: SSH,
        MAP[FS]: FS,
        MAP[SK]: SK,
    }
)
DUNGEON_MAPS_RESTRICTED_RESTRICTION = norm_values(
    {
        MAP[SV]: SV + sep + "Main",
        MAP[ET]: ET + sep + "Main",
        MAP[LMF]: LMF + sep + "Main",
        MAP[AC]: AC + sep + "Main",
        MAP[SSH]: SSH + sep + "Main",
        MAP[FS]: FS + sep + "Main",
        MAP[SK]: SK + sep + "Main",
    }
)

VANILLA_TRIFORCES_PLACEMENT = norm_values(
    {
        TRIFORCE_OF_COURAGE: "Sky Keep - Sacred Power of Farore",
        TRIFORCE_OF_WISDOM: "Sky Keep - Sacred Power of Nayru",
        TRIFORCE_OF_POWER: "Sky Keep - Sacred Power of Din",
    }
)

TRIFORCES_RESTRICTION = norm_values(
    {TRIFORCE_OF_COURAGE: SK, TRIFORCE_OF_WISDOM: SK, TRIFORCE_OF_POWER: SK}
)


VANILLA_RUPEES = norm_force_vanilla(RUPEE_CHECKS)
VANILLA_QUICK_BEETLE_RUPEES = norm_force_vanilla(QUICK_BEETLE_CHECKS)

TADTONE_CHECKS = [
    "Flooded Faron Woods - Yellow Tadtone under Lilypad",
    "Flooded Faron Woods - 8 Light Blue Tadtones near Viewing Platform",
    "Flooded Faron Woods - 4 Purple Tadtones under Viewing Platform",
    "Flooded Faron Woods - Red Moving Tadtone near Viewing Platform",
    "Flooded Faron Woods - Light Blue Tadtone under Great Tree Root",
    "Flooded Faron Woods - 8 Yellow Tadtones near Kikwi Elder",
    "Flooded Faron Woods - 4 Light Blue Moving Tadtones under Kikwi Elder",
    "Flooded Faron Woods - 4 Red Moving Tadtones North West of Great Tree",
    "Flooded Faron Woods - Green Tadtone behind Upper Bombable Rock",
    "Flooded Faron Woods - 2 Dark Blue Tadtones in Grass West of Great Tree",
    "Flooded Faron Woods - 8 Green Tadtones in West Tunnel",
    "Flooded Faron Woods - 2 Red Tadtones in Grass near Lower Bombable Rock",
    "Flooded Faron Woods - 16 Dark Blue Tadtones in the South West",
    "Flooded Faron Woods - 4 Purple Moving Tadtones near Floria Gate",
    "Flooded Faron Woods - Dark Blue Moving Tadtone inside Small Hollow Tree",
    "Flooded Faron Woods - 4 Yellow Tadtones under Small Hollow Tree",
    "Flooded Faron Woods - 8 Purple Tadtones in Clearing after Small Hollow Tree",
]

VANILLA_TADTONE_PLACEMENT = norm_restrict_vanilla(TADTONE_CHECKS)

TRIAL_RELIC_CHECKS = [
    "The Goddess's Silent Realm - Relic 1",
    "The Goddess's Silent Realm - Relic 2",
    "The Goddess's Silent Realm - Relic 3",
    "The Goddess's Silent Realm - Relic 4",
    "The Goddess's Silent Realm - Relic 5",
    "The Goddess's Silent Realm - Relic 6",
    "The Goddess's Silent Realm - Relic 7",
    "The Goddess's Silent Realm - Relic 8",
    "The Goddess's Silent Realm - Relic 9",
    "The Goddess's Silent Realm - Relic 10",
    "Farore's Silent Realm - Relic 1",
    "Farore's Silent Realm - Relic 2",
    "Farore's Silent Realm - Relic 3",
    "Farore's Silent Realm - Relic 4",
    "Farore's Silent Realm - Relic 5",
    "Farore's Silent Realm - Relic 6",
    "Farore's Silent Realm - Relic 7",
    "Farore's Silent Realm - Relic 8",
    "Farore's Silent Realm - Relic 9",
    "Farore's Silent Realm - Relic 10",
    "Nayru's Silent Realm - Relic 1",
    "Nayru's Silent Realm - Relic 2",
    "Nayru's Silent Realm - Relic 3",
    "Nayru's Silent Realm - Relic 4",
    "Nayru's Silent Realm - Relic 5",
    "Nayru's Silent Realm - Relic 6",
    "Nayru's Silent Realm - Relic 7",
    "Nayru's Silent Realm - Relic 8",
    "Nayru's Silent Realm - Relic 9",
    "Nayru's Silent Realm - Relic 10",
    "Din's Silent Realm - Relic 1",
    "Din's Silent Realm - Relic 2",
    "Din's Silent Realm - Relic 3",
    "Din's Silent Realm - Relic 4",
    "Din's Silent Realm - Relic 5",
    "Din's Silent Realm - Relic 6",
    "Din's Silent Realm - Relic 7",
    "Din's Silent Realm - Relic 8",
    "Din's Silent Realm - Relic 9",
    "Din's Silent Realm - Relic 10",
]


def SOME_VANILLA_RELICS(
    max_relics: int, norm: Callable[[str], EIN], checks: Dict[EIN, Any]
) -> Placement:
    list = [k for k in TRIAL_RELIC_CHECKS if int(k[-2:].strip()) > max_relics]
    list2 = map(norm, list)
    dict = {k: EIN(checks[k]["original item"]) for k in list2}
    return Placement(locations=dict, items={v: k for k, v in dict.items()})
