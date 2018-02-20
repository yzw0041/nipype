# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..gtract import gtractInvertDisplacementField


def test_gtractInvertDisplacementField_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        baseImage=dict(argstr='--baseImage %s', ),
        deformationImage=dict(argstr='--deformationImage %s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        numberOfThreads=dict(argstr='--numberOfThreads %d', ),
        outputVolume=dict(
            argstr='--outputVolume %s',
            hash_files=False,
        ),
        subsamplingFactor=dict(argstr='--subsamplingFactor %d', ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
    )
    inputs = gtractInvertDisplacementField.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_gtractInvertDisplacementField_outputs():
    output_map = dict(outputVolume=dict(), )
    outputs = gtractInvertDisplacementField.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
