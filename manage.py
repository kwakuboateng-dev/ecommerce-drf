#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from emia_ecommerce.settings import base_settings


def main():
    """Run administrative tasks."""

    if base_settings.DEBUG:
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "emia_ecommerce.settings.local_settings"
        )
    else:
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "emia_ecommerce.settings.production_settings"
        )

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
