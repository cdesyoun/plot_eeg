import mne
mne.viz.set_browser_backend('qt')

datafile = '/Users/cyoun/plot_eeg_mne/sub-NDARAA948VFH_task-EC_run-1_eeg.set'

EEG = mne.io.read_raw_eeglab(datafile, preload=True)

print("display start")
EEG.filter(l_freq=1, h_freq=None).plot(block=True)
print("display end")

