# =====================================
# BOBBY AI STUDIO v2.7
# Plugin Manager
# =====================================

import os
import importlib


PLUGIN_FOLDER = "plugins"


def load_plugins():

    plugins = []

    if not os.path.exists(PLUGIN_FOLDER):
        return plugins


    for file in os.listdir(PLUGIN_FOLDER):

        if file.endswith(".py") and file != "__init__.py":

            plugin_name = file[:-3]

            try:

                module = importlib.import_module(
                    f"{PLUGIN_FOLDER}.{plugin_name}"
                )

                plugins.append(module)

            except Exception as error:

                print("Plugin loading error:", error)


    return plugins



def show_plugins():

    print("\n--- INSTALLED PLUGINS ---")

    plugins = load_plugins()


    if plugins:

        for plugin in plugins:
            print(plugin.__name__)

    else:

        print("No plugins installed.")



def run_plugins():

    print("\n--- RUNNING PLUGINS ---")

    plugins = load_plugins()

    for plugin in plugins:

        if hasattr(plugin, "run"):

            plugin.run()