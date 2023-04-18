# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install gurobi
#
# You can edit this file again by typing:
#
#     spack edit gurobi
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os


class Gurobi(Package):

    """gurobi The Gurobi Optimizer is a state-of-the-art solver for mathematical programming"""

    version('10.0.1', sha256='a0b551156df2c94107b3428cae278716a0a6c913f63ac132573852b9725b6c59')

    license_required = True
    license_comment  = '#'
    license_files    = ['licenses/gurobi.lic']
    license_vars     = ['GRB_LICENSE_FILE ']
    license_url      = 'https://www.gurobi.com/academia/academic-program-and-licenses'

    extendable = True


    def url_for_version(self, version):
        return "file://{0}/gurobi{1}_linux64.tar.gz".format(os.getcwd(), version)


    def setup_run_environment(self, env):
        env.set('GUROBI_HOME', join_path(self.prefix,'linux64'))
        env.set('GRB_LICENSE_FILE', join_path(self.prefix,'licenses','gurobi.lic'))
        env.prepend_path('PATH', join_path(self.prefix,'linux64','bin'))
        env.prepend_path('LD_LIBRARY_PATH', join_path(self.prefix,'linux64','lib'))
 
    def setup_build_environment(self, env):
        env.set('GUROBI_HOME', join_path(self.prefix,'linux64'))
 
    def install(self, spec, prefix):
        install_tree('.', self.prefix)
