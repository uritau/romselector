# No-intro romset selector

Tired of getting thousands of repeated games with USA, Europe, Asia ... versions and Rev 1, Alphas, etc?
This app will help you to select only the desired games.

## Getting Started

git clone the repo and
### Prerequisites

Download the RomSet and uncompress in a folder. Use this folder as a origin folder.
Create a new folder (where desired games will be copied). Use this folder as destination folder.

### Installing

Copy the script and launch using python3

```
python3 romselector.py origin-folder destination-folder
```

## Running the tests

TO DO

## Built With
l
* Python

## Contributing

Create your pull request!

## Authors

* **Oriol Tauleria** - [uritau](https://github.com/uritau)

## To Do
* Create the "copy" function 
* Check if the parameters are correct
* Update the flow: 
    * Ask if would to copy only games under certain tags, all unique games or all of them.
    * If only certain tags: follow the current flow.
    * All of them: Copy all the games
    * All unique games: Ask about order preference (USA / EUROPE /JAPAN ) and ask about special tags (beta, Unl, Rev A, Rev X, etc. )