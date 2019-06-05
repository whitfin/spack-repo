# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Watch(Package):
    """Executes a program periodically, showing output fullscreen."""

    homepage = "https://gitlab.com/procps-ng/procps"
    url      = "https://gitlab.com/procps-ng/procps/-/archive/v3.3.15/procps-v3.3.15.tar.bz2"

    version('3.3.15', sha256='191391fde24a1d3b9b0030d26f8dfdcbf641d36297aab7ecf2f941c5ca927e21')


    depends_on('autoconf',     type='build')
    depends_on('automake',     type='build')
    depends_on('libtool',      type='build')
    depends_on('pkgconfig',    type='build')
    depends_on('xz',           type='build')

    depends_on('gettext')

    phases = ['autogen', 'install']

    def autogen(self, spec, prefix):
        autogen = Executable('./autogen.sh')
        autogen('-fiv')

    def install(self, spec, prefix):
        configure('--disable-dependency-tracking',
                  '--disable-nls',
                  '--prefix=%s' % self.spec.prefix)
        make('watch')
        mkdir(prefix.bin)
        install('watch', prefix.bin)
