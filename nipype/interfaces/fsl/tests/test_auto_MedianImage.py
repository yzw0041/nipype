# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..maths import MedianImage


def test_MedianImage_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        dimension=dict(
            argstr='-%smedian',
            position=4,
            usedefault=True,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='%s',
            mandatory=True,
            position=2,
        ),
        internal_datatype=dict(
            argstr='-dt %s',
            position=1,
        ),
        nan2zeros=dict(
            argstr='-nan',
            position=3,
        ),
        out_file=dict(
            argstr='%s',
            genfile=True,
            hash_files=False,
            position=-2,
        ),
        output_datatype=dict(
            argstr='-odt %s',
            position=-1,
        ),
        output_type=dict(),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
    )
    inputs = MedianImage.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_MedianImage_outputs():
    output_map = dict(out_file=dict(), )
    outputs = MedianImage.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
