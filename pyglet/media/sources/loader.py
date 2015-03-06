# ----------------------------------------------------------------------------
# pyglet
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions 
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright 
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import pyglet

debug = pyglet.options['debug_media']


class AbstractSourceLoader(object):
    def load(self, filename, file):
        raise NotImplementedError('abstract')


class AVbinSourceLoader(AbstractSourceLoader):
    def load(self, filename, file):
        import pyglet.media.sources.avbin as avbin
        return avbin.AVbinSource(filename, file)


class RIFFSourceLoader(AbstractSourceLoader):
    def load(self, filename, file):
        import pyglet.media.sources.riff as riff
        return riff.WaveSource(filename, file)


def get_source_loader():
    global _source_loader

    if _source_loader:
        return _source_loader

    try:
        import pyglet.media.sources.avbin
        _source_loader = AVbinSourceLoader()
    except ImportError:
        _source_loader = RIFFSourceLoader()
    return _source_loader

_source_loader = None

try:
    import pyglet.media.sources.avbin
    have_avbin = True
except ImportError:
    have_avbin = False
