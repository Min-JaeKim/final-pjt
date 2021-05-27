#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# 시작
# from optparse import make_option

# from django.core.management.commands.dumpdata import Command as Dumpdata

# class Command(Dumpdata):
#     option_list = Dumpdata.option_list + (
#         make_option('--pretty', default=False, action='store_true', 
#             dest='pretty', help='Avoid unicode escape symbols'
#         ),
#     )
    
#     def handle(self, *args, **kwargs):
#         data = super(Command, self).handle(*args, **kwargs)
#         if kwargs.get('pretty'):
#             data = data.decode("unicode_escape").encode("utf8")
#         return data

# 끝

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mypjt.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
