import numpy as np
import pywt
import pathlib
import scipy.signal as signal
from biosppy import ecg


class Detectors:

    def __init__(self, sampling_frequency):
        self.fs = sampling_frequency    

    def two_average_detector(self, unfiltered_ecg):

        # bandpass filter (butterworth)
        f1 = 8/self.fs
        f2 = 20/self.fs

        b, a = signal.butter(2, [f1*2, f2*2], btype='bandpass')

        filtered_ecg = signal.lfilter(b, a, unfiltered_ecg)

        # generate potential blocks
        window1 = int(0.12*self.fs)
        mwa_qrs = MWA(abs(filtered_ecg), window1)

        window2 = int(0.6*self.fs)
        mwa_beat = MWA(abs(filtered_ecg), window2)

        blocks = np.zeros(len(unfiltered_ecg))
        block_height = np.max(filtered_ecg)

        for i in range(len(mwa_qrs)):
            if mwa_qrs[i] > mwa_beat[i]:
                blocks[i] = block_height
            else:
                blocks[i] = 0

        QRS = []

        for i in range(1, len(blocks)):
            if blocks[i-1] == 0 and blocks[i] == block_height:
                start = i
            elif blocks[i-1] == block_height and blocks[i] == 0:
                end = i-1
                if end-start>int(0.08*self.fs):
                    detection = np.argmax(filtered_ecg[start:end+1])+start
                    if QRS:
                        if detection-QRS[-1]>int(0.3*self.fs):
                            QRS.append(detection)
                    else:
                        QRS.append(detection)
        # thresholding
        r_peaks = searchBack(QRS, unfiltered_ecg, window1)

        return r_peaks

def MWA(input_array, window_size):

    mwa = np.zeros(len(input_array))
    for i in range(len(input_array)):
        if i < window_size:
            section = input_array[0:i]
        else:
            section = input_array[i-window_size:i]
        
        if i!=0:
            mwa[i] = np.mean(section)
        else:
            mwa[i] = input_array[i]

    return mwa

def searchBack(detected_peaks, unfiltered_ecg, search_samples):

    r_peaks = []
    window = search_samples

    for i in detected_peaks:
        if i<window:
            section = unfiltered_ecg[:i]
            r_peaks.append(np.argmax(section))
        else:
            section = unfiltered_ecg[i-window:i]
            r_peaks.append(np.argmax(section)+i-window)

    return np.array(r_peaks)