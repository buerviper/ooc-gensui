# No Context Suikoden Mastodon bot
This bot posts (more or less) random images from the Suikoden JRPG series to the Mastodon account [botsin.space/@oocgensui](https://botsin.space/@oocgensui). At the moment, it posts two pictures per day.

## Structure

The `/images` folder contains all the images from which the `run.py` script randomly selects one. The filenames follow the pattern `game-gamenumber-description-imagenumber`:
* `game`: can be suikoden or suikogaiden. 
* `gamenumber`: can be a number between `01` and `05`, `tierkreis` or `tsumuji` (for Tsumugareshi Hyakunen no Toki). `cardstories` and `pachisuro` will be added once pictures of these games will be added.
* `description`: a meaningful description of the image, seperated by `-`. At the moment, there's not a real pattern, but it should include the character(s) involved in the image(s) and either the main points of the dialogue (if there's any) or of the picture in general.
* `imagenumber` (''optional''): if there's a series of images which belong together and should be posted together, the imagenumber (value `1-4`) indicates the index of the image (i.e., imagenumber = 1 will be the first image in a post, 2 the second etc.).

The `/image/descriptions` folder contains the images' metadata as `.yaml` files. It contains the following field:
* `status`: The text of the post. Default is `"#suikoden #jrpg"`.
* `spoiler_warning`: If the image needs a content warning, the text can be added. Default is `None` (does not need to be stated explicitly).
* `description`: Alt-text of the image. Default is `"Screenshot of Suikoden."`
* `language`: ISO 639-1 language code for the text in the image. Default is `en`.
* `sensitivity`: Marks image as sensitive content. Default is `False`.

## To do

### Alt text
In addition to adding more images, the biggest to do is adding meaningful alt-text to every image which is currently lacking.

### HD images

A lot of the images were taken (with permission) from the no context suikoden twitter account. This means that a lot of them are low definition, sometimes even photos from TVs. The goal is to have HD (as HD as it gets) screenshots for each post in the original aspect ratio of the games (4:3 for PS1 and PS2).

# Copyright 

All images (c) Konami 1995–2023. 

All images are used under a [Fair Use clause (Section 107 U.S. Copyright Law)](https://www.copyright.gov/title17/92chap1.html#107) without commercial interests.

Die Verwendung geschützter Materialien des bots verfolgt keine finanziellen Interessen, sondern dient einem dokumentarischen Zweck als Bildzitat nach [§ 51 UrhG](https://www.gesetze-im-internet.de/urhg/__51.html). 

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

The No Context Suikoden Mastodon bot is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
