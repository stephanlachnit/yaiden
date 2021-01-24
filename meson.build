# SPDX-FileCopyrightText: 2020-2021 Stephan Lachnit <stephanlachnit@protonmail.com>
#
# SPDX-License-Identifier: CC0-1.0

project(
    'yaiden',
    license: 'EUPL-1.2',
    version: 'v1',
)

# paths
prefix = get_option('prefix')
bindir = get_option('bindir')
pymdir = import('python').find_installation().get_install_dir()
datadir = join_paths(prefix, get_option('datadir'))
localedir = join_paths(prefix, get_option('localedir'))

# install exectuable
install_data(
    files('yaiden.py'),
    install_dir: bindir,
    rename: 'yaiden',
)

# install python module
install_subdir(
  'yaiden',
  install_dir: pymdir,
)

# flake8
flake8 = find_program('flake8', required: false)
if flake8.found()
    test(
        'flake8',
        flake8,
        workdir: meson.source_root(),
    )
endif

# pylint
pylint = find_program('pylint', required: false)
if pylint.found()
    test(
        'pylint',
        pylint,
        args: [
            'yaiden',
            'yaiden.py',
        ],
        workdir: meson.source_root(),
        timeout: 300
    )
endif

# generate translation
subdir('po')

# program data
subdir('data')
