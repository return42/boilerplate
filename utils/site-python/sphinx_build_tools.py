# -*- coding: utf-8; mode: python -*-
"""Implement some sphinx-build tools.

"""

import os
import sys
from sphinx.util.osutil import fs_encoding

# ------------------------------------------------------------------------------
def load_sphinx_config(namespace):
# ------------------------------------------------------------------------------

    """Load an additional configuration file into *namespace*.

    The name of the configuration file is taken from the environment
    ``SPHINX_CONF``. The external configuration file extends (or overwrites) the
    configuration values from the origin ``conf.py``.  With this you are able to
    maintain *build themes*.  To your docs/conf.py add::

        from sphinx_build_tools import load_sphinx_config
        ...

        # Since loadConfig overwrites settings from the global namespace, it has to be
        # the last statement in the conf.py file

        load_sphinx_config(globals())

    """

    config_file = os.environ.get("SPHINX_CONF", None)
    if (
            config_file is not None
            and os.path.normpath(namespace["__file__"]) != os.path.normpath(config_file)
    ):
        config_file = os.path.abspath(config_file)

        if os.path.isfile(config_file):
            sys.stdout.write(f"load additional sphinx-config: {config_file}\n")
            config = namespace.copy()
            config['__file__'] = config_file
            with open(config_file, 'rb') as cfg:
                code = compile(cfg.read(), fs_encoding, 'exec')
                exec(code, config)  # pylint: disable=exec-used
            del config['__file__']
            namespace.update(config)
        else:
            sys.stderr.write(
                f"WARNING: additional sphinx-config not found: {config_file}\n"
            )
