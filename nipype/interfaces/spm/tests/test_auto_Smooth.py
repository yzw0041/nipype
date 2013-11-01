# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.spm.preprocess import Smooth
def test_Smooth_inputs():
    input_map = dict(implicit_masking=dict(field='im',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    mfile=dict(usedefault=True,
    ),
    data_type=dict(field='dtype',
    ),
    paths=dict(),
    use_v8struct=dict(min_ver='8',
    usedefault=True,
    ),
    in_files=dict(copyfile=False,
    mandatory=True,
    field='data',
    ),
    out_prefix=dict(field='prefix',
    usedefault=True,
    ),
    matlab_cmd=dict(),
    use_mcr=dict(),
    fwhm=dict(field='fwhm',
    ),
    )
    inputs = Smooth.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_Smooth_outputs():
    output_map = dict(smoothed_files=dict(),
    )
    outputs = Smooth.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
