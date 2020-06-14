from ruamel.yaml import YAML
from .example_config import get_example_config
from .default_config import get_default_config

yaml = YAML(typ="safe")


class InvalidConfigException(Exception):
    pass


class Config(object):
    def __init__(self, path):
        loaded_config = yaml.load(path)
        self.config = extract_and_merge_defaults(loaded_config)

    def get_name(self):
        return self.config["name"]

    def get_wine_portable_url(self):
        bundle_wine_opt = self.config["bundle_wine"]

        if "version" not in bundle_wine_opt:
            raise InvalidConfigException('Missing version field in "bundle_wine"')
        if "build" not in bundle_wine_opt:
            raise InvalidConfigException('Missing build field in "bundle_wine"')
        if "arch" not in bundle_wine_opt:
            raise InvalidConfigException('Missing arch field in "bundle_wine"')

        url = "https://dl.winehq.org/wine-builds/macosx/pool/portable-winehq-{build}-{version}-osx{arch}.tar.gz".format(
            build=bundle_wine_opt["build"],
            version=bundle_wine_opt["version"],
            arch=bundle_wine_opt["arch"],
        )
        return url


def extract_and_merge_defaults(loaded_config):
    # load default config
    config = yaml.load(get_default_config())

    config["name"] = loaded_config["name"] or config["name"]
    config["icon"] = loaded_config["icon"] or config["icon"]
    config["wine_arch"] = loaded_config["wine_arch"] or config["wine_arch"]
    config["base_prefix"] = loaded_config["base_prefix"] or config["base_prefix"]

    config["bundle_wine"] = loaded_config["bundle_wine"] or config["bundle_wine"]
    if not isinstance(config["bundle_wine"], dict):
        raise InvalidConfigException(
            "bundle_wine must be dictionary of {version, build, arch}"
        )

    run_opt = loaded_config["run"] or config["run"]
    if not (isinstance(run_opt, str) and isinstance(run_opt, list)):
        raise InvalidConfigException("run must be a string or a list")
    config["run"] = [run_opt] if isinstance(run_opt, str) else run_opt

    entrypoint_opt = loaded_config["entrypoint"] or config["entrypoint"]
    config["entrypoint"] = (
        [entrypoint_opt] if isinstance(entrypoint_opt, str) else entrypoint_opt
    )

    volumes_opt = loaded_config["volumes"] or config["volumes"]
    config["volumes"] = [volumes_opt] if isinstance(volumes_opt, str) else volumes_opt

    winetricks_verbs_opt = (
        loaded_config["winetricks_verbs"] or config["winetricks_verbs"]
    )
    config["winetricks_verbs"] = (
        [winetricks_verbs_opt]
        if isinstance(winetricks_verbs_opt, str)
        else winetricks_verbs_opt
    )

    config["bundle_winetricks"] = (
        loaded_config["bundle_winetricks"] or config["bundle_winetricks"]
    )
    config["sandbox"] = loaded_config["sandbox"] or config["sandbox"]

    return config


def save_example_config(path):
    with open(path, "w") as out:
        out.writelines(get_example_config())
