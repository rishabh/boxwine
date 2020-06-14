import subprocess

blacklist = ["good", "bad"]


def is_blacklisted(entry):
    return entry in blacklist


def get_categories_and_verbs():
    verbs_list = subprocess.run(
        ["winetricks", "list-all"],
        stdout=subprocess.PIPE,
        stderr=None,
        encoding="utf-8",
    ).stdout.splitlines()

    categories = {}
    current_category = ""
    for line in verbs_list:
        # skip blanks and warnings
        if not line or line.startswith("warning:"):
            continue

        # get category
        if line.startswith("====="):
            current_category = line.split("=====")[1].strip()
            continue

        # initialize verb dict for this category
        if current_category not in categories:
            categories[current_category] = {}

        # parse the entry
        entry = line.split(maxsplit=1)
        verb = entry[0].strip()

        # skip blacklisted verbs
        if is_blacklisted(verb):
            continue

        # get the description
        desc = entry[1].strip() if len(entry) == 2 else ""

        # for this category, add the verb and description
        categories[current_category][verb] = desc

    return categories
