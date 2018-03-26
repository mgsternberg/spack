##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Transdecoder(MakefilePackage):
    """TransDecoder identifies candidate coding regions within transcript
       sequences, such as those generated by de novo RNA-Seq transcript
       assembly using Trinity, or constructed based on RNA-Seq alignments to
       the genome using Tophat and Cufflinks."""

    homepage = "http://transdecoder.github.io/"
    url      = "https://github.com/TransDecoder/TransDecoder/archive/v3.0.1.tar.gz"

    version('3.0.1', 'f62b86a15fcb78b1dada9f80cc25f300')

    depends_on('perl', type=('build', 'run'))

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('TransDecoder.LongOrfs', prefix)
        install('TransDecoder.Predict', prefix)
        install_tree('PerlLib', prefix.PerlLib)
        install_tree('util', prefix.util)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PATH', prefix.util.bin)
        run_env.prepend_path('PATH', prefix)
