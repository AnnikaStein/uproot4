# BSD 3-Clause License; see https://github.com/scikit-hep/uproot4/blob/master/LICENSE

"""
Defines a versionless model of ``TString``.
"""

from __future__ import absolute_import

import uproot4.model


class Model_TString(uproot4.model.Model, str):
    """
    A versionless :py:class:`~uproot4.model.Model` for ``TString``.

    This is also a Python ``str`` (string).
    """

    def read_numbytes_version(self, chunk, cursor, context):
        pass

    def read_members(self, chunk, cursor, context, file):
        if self.is_memberwise:
            raise NotImplementedError(
                """memberwise serialization of {0}
in file {1}""".format(
                    type(self).__name__, self.file.file_path
                )
            )
        self._data = cursor.string(chunk, context)

    def postprocess(self, chunk, cursor, context, file):
        out = Model_TString(self._data)
        out._cursor = self._cursor
        out._file = self._file
        out._parent = self._parent
        out._members = self._members
        out._bases = self._bases
        out._num_bytes = self._num_bytes
        out._instance_version = self._instance_version
        return out

    def __repr__(self):
        if self.class_version is None:
            version = ""
        else:
            version = " (version {0})".format(self.class_version)
        return "<{0}{1} {2} at 0x{3:012x}>".format(
            self.classname, version, str.__repr__(self), id(self)
        )

    def tojson(self):
        return str(self)

    @classmethod
    def awkward_form(cls, file, index_format="i64", header=False, tobject_header=True):
        return uproot4.containers.AsString(False, typename="TString").awkward_form(
            file, index_format, header, tobject_header
        )


uproot4.classes["TString"] = Model_TString
