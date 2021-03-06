# cascade-config

[![](https://flat.badgen.net/pypi/v/cascade-config?icon=pypi)](https://pypi.org/project/cascade-config)
[![](https://flat.badgen.net/github/release/ralfg/cascade-config)](https://github.com/ralfg/cascade-config/releases)
[![](https://flat.badgen.net/github/checks/ralfg/cascade-config/)](https://github.com/ralfg/cascade-config/actions)
[![](https://flat.badgen.net/codecov/c/github/ralfg/cascade-config)](https://codecov.io/gh/RalfG/cascade-config)
![](https://flat.badgen.net/github/last-commit/ralfg/cascade-config)
![](https://flat.badgen.net/github/license/ralfg/cascade-config)


*Cascading Python configuration from the CLI and multiple config files.*

cascade-config simplifies handling multiple configuration sources, such as config files, command line arguments, or even simple dictionaries. Configuration sources can be added
one-by-one and will be parsed in hierarchical order, with each new source updating the
existing configuration.

## Installation

Install with pip
```
pip install cascade-config
```

## Quickstart

Multiple configuration sources can be added to a `cascade_config.CascadeConfig`
object. When parsed, each configuration will be added in hierarchical order and update
the existing configuration. The result is a single dictionary containing the cascaded
configuration.

```python
from cascade_config import CascadeConfig

# Setup CascadeConfig instance with JSON schema for validation
cascade_conf = CascadeConfig(validation_schema="config_schema.json")

# Add default and user configurations in cascading order
cascade_conf.add_json("config_default.json")
cascade_conf.add_json("config_user.json")

# Parse the configuration files into a dictionary
config = cascade_conf.parse()
```

See [Usage](https://cascade-config.readthedocs.io/en/latest/usage.html) for more
information and examples.


## Contributing

Bugs, questions or suggestions? Feel free to post an issue in the
[issue tracker](https://github.com/RalfG/cascade-config/issues/) or to make a pull
request! See [Contributing](https://cascade-config.readthedocs.io/en/latest/contributing.html)
for more info.


## Changelog

See [Changelog](https://cascade-config.readthedocs.io/en/latest/changelog.html).
