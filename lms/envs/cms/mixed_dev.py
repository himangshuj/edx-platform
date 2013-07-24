"""
This configuration is to run the MixedModuleStore on a localdev environment
"""

from .dev import *

MODULESTORE = {
    'default': {
        'ENGINE': 'xmodule.modulestore.mixed.MixedModuleStore',
        'OPTIONS': {
            'mappings': {
                '6.002/a/a': 'xml',
                '6.002/b/b': 'xml'
            },
            'stores': {
                'xml': {
                    'ENGINE': 'xmodule.modulestore.xml.XMLModuleStore',
                    'OPTIONS': {
                        'data_dir': DATA_DIR,
                        'default_class': 'xmodule.hidden_module.HiddenDescriptor',
                    }
                },
                'default': {
                    'ENGINE': 'xmodule.modulestore.mongo.MongoModuleStore',
                    'OPTIONS': {
                        'default_class': 'xmodule.raw_module.RawDescriptor',
                        'host': 'localhost',
                        'db': 'xmodule',
                        'collection': 'modulestore',
                        'fs_root': DATA_DIR,
                        'render_template': 'mitxmako.shortcuts.render_to_string',
                    }
                }
            },
        }
    }
}