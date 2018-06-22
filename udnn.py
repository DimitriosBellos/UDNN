import numpy as np
import udnn.trainer as ut
import udnn.upscaler as ur

model = ut.train('../Diamond/tomo_p1_dark_flat_field_correction.h5', '/1-DarkFlatFieldCorrection-tomo/data', 'demo', output_folder=None, validation_filename=None,
                 validation_dataset=None, size=128, H=None, W=None, train_sinograms=np.arange(1,2159,2),
                 validation_sinograms=np.arange(2,2159,2), down_scale=40, scale=2, stride=1, sub_size=401,
                 batch=10, workers=8, num_val_patches=10, stop=60, valfreq=16, display=False, gpu=True)

model_name = ('demo/Checkpoints/CP%03d.pt' % model)

ur.upscale('../Diamond/tomo_p1_dark_flat_field_correction_2.h5', '/1-DarkFlatFieldCorrection-tomo/data', model_name, 'test.h5',
           out_dataset=None, size=128, H=None, W=None, sinograms=np.arange(1, 2160, 10), down_scale=40, scale=2, stride=1, sub_size=401, batch=10, workers=8, do_CI=True, gpu=True)
