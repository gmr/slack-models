"""
# slack-models

Pydantic Models for working with the Slack API

"""

from importlib import metadata

try:
    version = metadata.version('slack-models')
except metadata.PackageNotFoundError:
    # Fallback when running from source without installation
    version = '0.0.0-dev'

__all__ = ['version']
