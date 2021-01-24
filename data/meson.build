# SPDX-FileCopyrightText: 2020-2021 Stephan Lachnit <stephanlachnit@protonmail.com>
#
# SPDX-License-Identifier: CC0-1.0

# icon
icon_file = files('io.github.stephanlachnit.yaiden.svg')

install_data(
    icon_file,
    install_dir: join_paths(datadir, 'icons', 'hicolor', 'scalable', 'apps'),
)

# metainfo file
metainfo_file = files('io.github.stephanlachnit.yaiden.metainfo.xml')

appstreamcli = find_program('appstreamcli', required: false)
if appstreamcli.found()
    test(
        'validate metainfo file',
        appstreamcli,
        args: [
            'validate',
            '--no-net',
            '--pedantic',
            metainfo_file,
        ],
    )
endif

i18n.merge_file(
    input:  metainfo_file,
    output: 'io.github.stephanlachnit.yaiden.metainfo.xml',
    type: 'xml',
    po_dir: join_paths(meson.source_root(), 'po'),
    install: true,
    install_dir: join_paths(datadir, 'metainfo'),
)

# dekstop file
dekstop_file = files('io.github.stephanlachnit.yaiden.desktop')

desktopfv = find_program('desktop-file-validate', required: false)
if desktopfv.found()
    test(
        'valide desktop file',
        desktopfv,
        args: [dekstop_file],
    )
endif

i18n.merge_file(
    input:  dekstop_file,
    output: 'io.github.stephanlachnit.yaiden.desktop',
    type: 'desktop',
    po_dir: join_paths(meson.source_root(), 'po'),
    install: true,
    install_dir: join_paths(datadir, 'applications'),
)
