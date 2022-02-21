# FOA-MEIR dataset
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6088574.svg)](https://doi.org/10.5281/zenodo.6088574)

FOA-MEIR is an impulse response (IR) dataset recorded in over 100 environments for use in sound event localization and detection (SELD) tasks. This dataset is set up to develop a robust SELD system in an unknown environment, and the IRs for the inferred environment are recorded at a different location from that of training data. The dataset also contains dry source recordings that can be combined with IR recordings to generate audio clips for training the SELD task.

## Download
You can download the dataset [here](https://doi.org/10.5281/zenodo.6088574). 

## Details of dataset
The dataset has following folder structure:

<pre>
FOA_MEIR_Dataset
├── placeinfo.csv
├── DrySounds
│   ├── eventsources
│   ├── soundeventinfo.csv
│   └── swept_sine_20ms.wav
├── IRrecordings
│   ├── anechoic
│   ├── echo
│   │   ├── anechoic
│   │   ├── reverb-s
│   │   └── test
│   ├── reverb-c
│   ├── reverb-s
│   └── test
└── Noise
    ├── reverb-c
    ├── reverb-s
    └── test
</pre>

### IRrecordings
This folder contains IR recordings. All IR recordings were recorded with a 4-channel FOA microphone (A-Format), _Sennheiser AMBEO VR MIC_. The sampling rate was 48 kHz in all recordings. Recording of IR was carried out by using two times synchronous addition of TSP signals of 131,072 samples in signal length. In all recordings, the noise level of the circumference was monitored, and SNR over 30 dB was ensured. 

The naming convention for IR recording is as follows. 
<pre>
imp_d[distance]_azi[azimuth angle]_ele[elevation angle]_pid[place id].bin
</pre>
Here, _distance_, _azimuth angle_ and _elevation angle_ are the relative position of sound source related to microphones. The _place id_ is the index of the recording position.　Please refer to placeinfo.csv to see what kind of environment each _place id_ refers to.


The IR recordings consist of the five subsets shown in the table below. See Sec. 4.1 in [1] for details on each subset.

| Subset                 | Anechoic                         |             Reverb-S             |               Test               | Echo |             Reverb-C             |
|------------------------|----------------------------------|:--------------------------------:|:--------------------------------:|:----:|:--------------------------------:|
| \# of environment      | 1                                |                96                |                 5                |  102 |                 2                |
| \# of IR / environment | 216                              |                 3                |                216               |   1  |                216               |
| Azimuth range          | $[-\pi,\pi)$                     |           $[-\pi,\pi)$           |           $[-\pi,\pi)$           |  $0$ |           $[-\pi,\pi)$           |
| Azimuth interval       | $10^{\circ}$                     |              random              |           $10^{\circ}$           |   -  |           $10^{\circ}$           |
| Elevation range        | $[-\frac{\pi}{2},\frac{\pi}{2})$ | $[-\frac{\pi}{2},\frac{\pi}{2})$ | $[-\frac{\pi}{2},\frac{\pi}{2})$ |  $0$ | $[-\frac{\pi}{2},\frac{\pi}{2})$ |
| Elevation interval     | $20^{\circ}$                     |              random              |           $20^{\circ}$           |   -  |           $20^{\circ}$           |
| Distance [cm]          | 75\,150                         |             75\,150             |             75\,150             |  150 |             75\,150             |
| Noise / environment    | -                                |              2.5 min             |              15 min              |   -  |              15 min              |

### Noise
This folder contains ambient noise that recorded at same position of _Reverb-S_,_Test_ and _Reverb-C_, using the 4-channel FOA microphone (A-Format). Ambient noise includes air conditioning, walking, talking, etc. 

The naming convention for the ambient noise recordings is as follows. 
<pre>
BG_pid[place id]_ch[channel of microphone].wav
</pre>
Here, the _place id_ is the index of the recording position (same with IR recordings). The _channel of microphone_ indicates the channel number (1 to 4) of the FOA microphone. For the _reverb-c_, since there is two types of noise recordings, white noise and walking noise, the naming convertion is as follows:

<pre>
BG_pid[place id]_whitenoise_ch[channel of microphone].wav
BG_pid[place id]_walknoise_ch[channel of microphone].wav
</pre>

### DrySounds
To synthesize a dataset for SELD using the above IR and ambient noise recordings, dry sounds were recorded in an anechoic room using a monaural microphone. These dry sounds contain 12 different sound event classes (see ```soundeventinfo.csv```), and each class has 20 variations of sound.

The naming convention for the dry sound recordings is as follows. 
<pre>
sample[sound event index]_[sample index].wav
</pre>
Here, _sound event index_ is the index of the sound event defined in ```soundeventinfo.csv```(1 to 12), _sample index_ is the index of the variations of each sound event (0 to 19).

## Usage

For the synthesis of SELD data sets using these impulse responses, environmental noise, and dry sound recordings, sample code will be available soon. 

### extract the IR data from binary file.
```` python
import utils

filepath = ".FOA_MEIR_Dataset/IRrecordings/reverb-s/imp_d150_azi100_ele0_pid0046.bin"
n_mic = 4 
irs = utils.fetch_imp(filepath,n_mic)
# irs.shape => (4,48000)
````

###  convert FOA A-format to FOA B-format.
```` python
import utils

#A.shape => (4,T): FOA A-Format signal
B = utils.convertAB(A)
# B.shape => (4,T): FOA B-Format signal
````
## License
See this [license](LICENSE.pdf) file.

## Authors and Contact
        
* Masahiro Yasuda (Email: masahiro.yasuda@ieee.org)
* Yasunori Ohishi
* Shoichiro Saito

## Citing this work

If you'd like to cite this work, you may use the following. 

> Masahiro Yasuda, Yasunori Ohishi, Shoichiro Saito, “Echo-aware Adaptation of Sound Event Localization and Detection in Unknown Environments,” in IEEE Int. Conf. Acoust. Speech Signal Process. (ICASSP), 2022.

## Link

Paper: [arXiv](https://arxiv.org/abs/2202.09121)
