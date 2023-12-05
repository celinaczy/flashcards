# Flashcards 

Project made on day 31 and enhanced on day 43 of 100 Days of Code. 
It is a GUI app which helps user study vocabulary in a foreign language. 

## Installation

1. Clone the repository: `git clone https://github.com/celinaczy/flashcards.git`
2. Navigate to the project directory: `cd flashcards`
3. Install required dependencies: `pip install -r requirements.txt`
4. Run the app: `python main.py`

## Usage 
- The app displays a word in French (could be easily customized to other languages) and after 3 seconds its translation to English
- User marks if they know the word or not
- The app continues to show new words (and the ones previously marked as unknown) until the user learns the whole deck or exits the app
- The progress is saved into to_learn.csv file so even after the program is closed the app 'remembers' which words are already known to the user.

## Demo
https://github.com/celinaczy/flashcards/assets/48793247/e3538de2-1ad1-4091-a605-7a1775c06970

## Custom word lists 
To run the app with a different set of words:
* change the `target_language` and `native_language` variables in lines 7 and 8 to the desired languages 
* make sure there's no to_learn.csv file in your folder (if there is, delete it)
* change the directory in line 9 to your .csv file formatted in the same way: 
```commandline
    target_language,native_language
    word1,translation1
    word2,translation2
    word3,translation3
    ...
    word99,translation99
```
Make sure that the spelling of `target_language` and `native_language` variables is the same in main.py and the .csv file 

## Acknowledgments

This project utilizes the following libraries:
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [pandas](https://pandas.pydata.org/)