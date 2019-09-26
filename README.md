# PDF2Anki

This is a simple python script that converts PDF files to anki flashcards.
This works for PDFs which pages consist of alternating front- and backsides. An example can be found [here](example.pdf).

If you want to create flashcards on IPad with the Apple Pencil and import them into Anki, this is one of the easiest ways to achieve that.
Flashcards++ from the Appstore allows you to export flashcards in the exact format specified.



## Prerequisites

This script uses Python3.

After cloning this repo, use this to install the required python packages:

```
pip3 install -r requirements.txt
```

On top of these packages, poller is required for the pdf extraction to work.

On Linux, run 

```
sudo apt install poppler-utils
```

How to install it on [Mac](http://macappstore.org/poppler/) and [Windows](http://blog.alivate.com.au/poppler-windows/)



## Using the script

Place the PDF you want to convert into the same folder as the script and run


```
python3 pdf2anki.py [PDFNAME].pdf [DECKNAME]
```

After this both a file with the name "pdf2anki_DECKNAME.csv" and a folder names "pdf2anki_images_DECKNAME". The latter one contains the exported images, that will be used for the anki cards.

## Importing the results into Anki

You need to have the desktop version of [Anki](https://apps.ankiweb.net/).

Befor importing your cards, I highly recommend creating a [note-type](http://ankiguide.com/cards-and-notes-the-difference-in-anki/) that has 3 fields ("Id", "Front", "Back"). This prevents you from having to set the order of the fields manually with each import.

You can import your newly created cards in 2 steps:

1. Import the csv file into Anki via the provided menu actions in the application.

2. Move all of the exported images into the Anki media folder. Instructions on how to acces the media folder can be found [here](https://superuser.com/questions/963526/where-does-anki-store-media)

After this, your cards should work as intended and can be synced across your devices.

## Authors

* **Adrian Steffan** - [adriansteffan](https://github.com/adriansteffan)


## Acknowledgements

The image2anki part of the script is based on a superuser thread found [here](https://superuser.com/questions/1170355/import-images-to-anki-automatically-to-front-and-back-of-the-cards).


