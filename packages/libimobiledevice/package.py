# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libimobiledevice(Package):
    """Library to communicate with iOS devices natively."""

    homepage = "https://www.libimobiledevice.org/"
    url      = "https://www.libimobiledevice.org/downloads/libimobiledevice-1.2.0.tar.bz2"
    git      = "https://git.libimobiledevice.org/libimobiledevice.git"

    version('master', branch='master')
    version('1.2.0',  sha256='786b0de0875053bf61b5531a86ae8119e320edab724fc62fe2150cc931f11037')

    depends_on('autoconf',   type='build', when='@master')
    depends_on('automake',   type='build', when='@master')
    depends_on('libtool',    type='build', when='@master')
    depends_on('pkg-config', type='build')
    depends_on('libplist')
    depends_on('libtasn1')
    depends_on('libusbmuxd')
    depends_on('openssl')

    def install(self, spec, prefix):
        if self.spec.satisfies('@master'):
            autogen = Executable('./autogen.sh')
            autogen()
        configure('--disable-dependency-tracking',
                  '--disable-silent-rules',
                  '--enable-debug-code',
                  '--prefix=%s' % self.spec.prefix,
                  '--without-cython')
        make('install')
