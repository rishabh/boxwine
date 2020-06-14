
example_config = r"""
# This is an example configuration file that can be used
# with boxwine to create Mac apps from wine apps.

# USAGE:
# "host" refers to the computer that is using
#    boxwine to create the app.
# "client" refers to the computer that is going to be
#    running the Mac app
# "wineprefix" refers to the virtual windows installation where all
#    of the windows files are stored. Think of it as C:/

# name of your app, default: My App
name: My App

# path to the icon to be used, default empty
# icon: path/to/icon.png

# programs that you want to run/install in the wineprefix, default empty.
# - can specify programs on the host
# - and can specify programs that are located in the wineprefix
run:
  - on/host/Setup.exe
  - ["on/host/other-file.exe", "--some-arg"]    # use a list to specify arguments that you want to pass in
  - $WINEPREFIX/in/wine/some-file.exe           # Use $WINEPREFIX to access the C:/ in wineprefix

# the program to start when you run the app, required.
# - can be a path to the program in the form of a string
# - or it can be a list, where the first element is the path
#   to the program with subsequent elements as arguments
entrypoint: ["C:/to/run/in/wine/program.exe", "--some-arg"]

# if you want to copy any files or folders over to the wineprefix,
# you can specify the file/folder on the host to copy
# into the wineprefix. Both Windows paths with backslashes and
# forward slashes are supported. Default empty
# volumes:
#   - on/host/file.txt:C:\in\wine\file.txt
#   - on/host/folder:C:/in/wine/folder

# if you want to install any verbs from winetricks, you can
# specify the verbs to install here, default empty
winetricks_verbs:
  - directshow    # for some sound fixes
  - directplay    # for local multiplayer

# if you want to bundle winetricks into the app, default false
# bundle_winetricks: false

# if you want to bundle wine into the app. If you do not bundle wine,
# the client is responsible for having wine installed
bundle_wine:
  version: 5.0    # default 5.0
  build: stable   # default stable
  arch: 64        # default 64

# if you want to use an existing wineprefix as the base, you can specify its
# path, default empty
# base_prefix: path/to/existing/wineprefix/on/host

# you can also specify the windows architecture, default win64.
# If you use a base prefix, this will be ignored
wine_arch: win64

# sandbox the wineprefix by , default true.
# Can also be enabled by specifying "sandbox" as a verb to winetricks
sandbox: true
"""


def get_example_config():
    return example_config
