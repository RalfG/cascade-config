# cascade-config

*Cascading Python configuration from the CLI and multiple config files.*

cascade-config simplifies handling multiple configuration sources, such as multiple
config files, command line arguments, or even simple dictionaries.

## Installation

For development, clone the repository and run:
```
flit install
```

## Usage

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

See [Usage](https://cascade-config.readthedocs.io/en/latest/usage.html) for more info
and examples.


## Changelog

See [Changelog](https://cascade-config.readthedocs.io/en/latest/changelog.html).


## Contributing

Bugs, questions or suggestions? Feel free to post an issue in the
[issue tracker](https://github.com/RalfG/cascade-config/issues/) or to make a pull
request!
