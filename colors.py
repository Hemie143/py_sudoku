#!/usr/bin/python
# -*- coding: UTF-8 -*-

# https://gist.github.com/Jossef/0ee20314577925b4027f

styles = {
    # styles
    'reset': '\033[0m',
    'bold': '\033[01m',
    'disabled': '\033[02m',
    'underline': '\033[04m',
    'reverse': '\033[07m',
    'strike_through': '\033[09m',
    'invisible': '\033[08m',
    # text colors
    'fg_black': '\033[30m',
    'fg_red': '\033[31m',
    'fg_green': '\033[32m',
    'fg_orange': '\033[33m',
    'fg_blue': '\033[34m',
    'fg_purple': '\033[35m',
    'fg_cyan': '\033[36m',
    'fg_light_grey': '\033[37m',
    'fg_dark_grey': '\033[90m',
    'fg_light_red': '\033[91m',
    'fg_light_green': '\033[92m',
    'fg_yellow': '\033[93m',
    'fg_light_blue': '\033[94m',
    'fg_pink': '\033[95m',
    'fg_light_cyan': '\033[96m',
    # background colors
    'bg_black': '\033[40m',
    'bg_red': '\033[41m',
    'bg_green': '\033[42m',
    'bg_orange': '\033[43m',
    'bg_blue': '\033[44m',
    'bg_purple': '\033[45m',
    'bg_cyan': '\033[46m',
    'bg_light_grey': '\033[47m'
}

def color(text, *user_styles):
    color_text = ''
    for style in user_styles:
        try:
            color_text += styles[style]
        except KeyError:
            raise KeyError('def color: parameter `{}` does not exist'.format(style))

    color_text += text
    return '\033[0m{}\033[0m'.format(color_text)


def error(text):
    return color(text, "bold", "fg_red")


def warning(text):
    return color(text, "bold", "fg_orange")


def success(text):
    return color(text, "fg_green")

