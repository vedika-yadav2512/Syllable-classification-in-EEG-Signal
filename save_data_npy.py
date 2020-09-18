import mne
import numpy

mne.utils.set_config('MNE_USE_CUDA', 'true')
mne.cuda.init_cuda(verbose=True)


def EEG_read(p, band_filters, low_frequency, high_frequency):
    raw_data = mne.io.read_raw_cnt(p, preload=True).load_data()
    raw_data.pick_channels(['FC6', 'FT8', 'C5', 'CP3', 'P3', 'T7', 'CP5', 'C3', 'CP1', 'C4'])
    raw_data = raw_data.copy()
    if band_filters:
        raw_data = raw_data.filter(low_frequency, high_frequency, n_jobs=4)
        return raw_data.get_data()
    return raw_data.get_data()


val = EEG_read(p="Data/p/Acquisition 283 Data.cnt", band_filters=True, low_frequency=4., high_frequency=40.)
print(val.shape)
numpy.save("complete_data.npy", val)

