# syllable-classification-in-EEG-Signal
Classifying 11-syllables from imagined speech EEG signal.

1. First preprocessing is done on the data to remove artifacts.

2. Data is epoched and saved to a csv file after it feature extraction is done and the 11 syllables/words with features as columns are saved for all subjects in seperate csv file.

3. A Multi-layer perceptron is trained and used for the prediction of the classes.

  Dataset used in this project - KARA ONE(Link-http://www.cs.toronto.edu/~complingweb/data/karaOne/karaOne.html)
