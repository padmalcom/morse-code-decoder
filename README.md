# Morse Code Decoder
Is Morse code without spaces uniquely decipherable? Unfortunately, not. But this recursive python application calculates all possible combinations of characters including letters, numbers and punctuation.

It furthermore inferes spaces between those words and filter uncommon combination of words with few characters. The spaces inference is based on a german dictionary (source https://gist.github.com/MarvinJWendt/2f4f4154b8ae218600eb091a5706b5f4). If you want to use the app for another language, replace the txt file.

## Memory consumption
The basic recusion decipher function works memory efficient, even for longer sentences it requires less than 100mb memory. In contranst, infering spaces allocates more memory due to reoccuring loop call in the main function. You have to keep in mind that even shorter words like '-.-.-.-....' = 'Käse' (cheese) could have 1024 possible space combinations according to https://www.cachesleuth.com/unmorse.html.

## Credits
Thanks to MarvinJWendt for the german word list and to Generic Human for the infer_spaces function.