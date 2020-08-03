"""Test cascade_config."""

import pytest
import jsonschema

import cascade_config

TEST_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Test schema",
    "type": "object",
    "properties": {
        "config_example": {
            "type": "object",
            "properties": {
                "num_cpu": {
                    "type": "number",
                    "minimum": -1,
                },
                "log_level": {
                    "type": "string",
                    "enum": ["debug", "info", "warning", "error", "critical"]
                }
            }
        }
    }
}

TEST_SAMPLE = {
    "config_example": {"num_cpu": 1, "log_level": "info"}
}

TEST_SAMPLE_INVALID = {
    "config_example": {"num_cpu": "not_a_number", "log_level": "info"}
}

class TestCascadeConfig:
    def test_single_config(self):
        cc = cascade_config.CascadeConfig()
        cc.add_dict(TEST_SAMPLE)
        assert cc.parse() == TEST_SAMPLE

    def test_single_config_validation(self):
        """Test single valid dict source, with JSON Schema validation"."""
        cc = cascade_config.CascadeConfig(validation_schema=TEST_SCHEMA)
        cc.add_dict(TEST_SAMPLE)
        assert cc.parse() == TEST_SAMPLE

    def test_single_config_validation_invalid(self):
        """Test single invalid dict source, with JSON Schema validation"."""
        cc = cascade_config.CascadeConfig(validation_schema=TEST_SCHEMA)
        cc.add_dict(TEST_SAMPLE_INVALID)
        with pytest.raises(jsonschema.exceptions.ValidationError):
            cc.parse()
