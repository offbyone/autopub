from importlib import import_module
from typing import List, Optional, Type

from autopub.plugins import AutopubPlugin


def _find_plugin(module: object) -> Optional[Type[AutopubPlugin]]:
    for obj in module.__dict__.values():
        if (
            isinstance(obj, type)
            and issubclass(obj, AutopubPlugin)
            and obj is not AutopubPlugin
        ):
            return obj

    return None


def find_plugins(names: List[str]) -> List[Type[AutopubPlugin]]:
    plugins: List[Type] = []

    for plugin_name in names:
        try:
            # TODO: find plugins outside the autopub namespace
            plugin_module = import_module(f"autopub.plugins.{plugin_name}")

            plugin_class = _find_plugin(plugin_module)

            if plugin_class is None:
                print(f"Could not find plugin {plugin_name}")
                # TODO: raise
                continue

            plugins.append(plugin_class)
        except ImportError as e:
            print(f"Error importing plugin {plugin_name}: {e}")

    return plugins
