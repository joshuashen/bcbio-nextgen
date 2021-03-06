#!/usr/bin/env python
"""Setup file and install script for NextGen sequencing analysis scripts.
"""
import os
from setuptools import setup, find_packages

version_py = os.path.join(os.path.dirname(__file__), 'bcbio', 'pipeline', 'version.py')
version = open(version_py).read().strip().split('=')[-1].replace('"','')

setup(name = "bcbio-nextgen",
      version = version,
      author = "Brad Chapman",
      author_email = "chapmanb@50mail.com",
      description = "Best-practice pipelines for fully automated high throughput sequencing analysis",
      license = "MIT",
      url = "https://github.com/chapmanb/bcbio-nextgen",
      namespace_packages = ["bcbio"],
      dependency_links = ['http://github.com/ipython/ipython/tarball/master#egg=ipython-1.0.dev'],
      packages = find_packages(),
      package_data={'bcbio': ['bam/data/*']},
      scripts = ['scripts/bcbio_nextgen.py',
                 'scripts/bam_to_wiggle.py',
                 'scripts/barcode_sort_trim.py',
                 'scripts/illumina_finished_msg.py',
                 'scripts/nextgen_analysis_server.py',
                 'scripts/solexa_qseq_to_fastq.py',
                 ],
      install_requires = [
          "boto >= 2.8.0",
          "cutadapt >= 1.2.1",
          "psutil >= 0.6.1",
          "biopython >= 1.61",
          "Mako >= 0.7.3",
          "PyYAML >= 3.10",
          "sh >= 1.07",
          "Logbook >= 0.4.1",
          "Cython >= 0.18",
          "pysam >= 0.7.4",
          "fabric >= 1.6.0",
          "ipython-cluster-helper >= 0.1.5",
          "pyzmq >= 13.1.0",
          "ipython >= 1.0.dev",
          "bioblend >= 0.2.3",
          "pybedtools >= 0.6.2",
          "py_descriptive_statistics >= 0.2",
          #"paramiko >= 1.9.0",
          #"celery >= 2.2.7,<3.0.0",
          #"rpy2 >= 2.0.7"
      ])
