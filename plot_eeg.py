import mne
mne.viz.set_browser_backend('qt')
datafile = './data/sub-NDARAA948VFH_task-EC_run-1_eeg.set'
EEG = mne.io.read_raw_eeglab(datafile, preload=True)
EEG.filter(l_freq=1, h_freq=None).plot(block=True)
