"""Test that all modules can be imported."""

import pytest


def test_import_exceptions():
    """Test exception imports."""
    from grok_webapi.exceptions import GrokError, GrokAuthenticationError
    assert GrokError is not None
    assert GrokAuthenticationError is not None


def test_import_logging():
    """Test logging config."""
    from grok_webapi.logging_config import set_log_level
    assert callable(set_log_level)


def test_import_constants():
    """Test constants."""
    from grok_webapi.constants import GrokEndpoints, ImageQuality
    assert GrokEndpoints.BASE_URL == "https://grok.com"
    assert ImageQuality.HIGH.value == "high"


def test_import_main_module():
    """Test main module imports."""
    import grok_webapi
    assert hasattr(grok_webapi, 'GrokError')
    assert hasattr(grok_webapi, 'set_log_level')
