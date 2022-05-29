# Lost Princess
## Table of Content

* [Part of Team](#part-of-team)
* [About](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Run Game Locally Without Docker](#run-game-locally-without-docker-recommended)
* [Run Game Locally With Docker](#run-game-locally-with-docker-optional)
* [UML Diagram](#uml-diagram)
* [Screenshots](#screenshots)
* [Contributing](#contributing)
## Part of Team

| Name | StudentID | Role | GitHub |
| :---: | :---: | :---: | :---: |
| Muhammad Elang Permadani | 120140194 | Project Leader | [elang194](https://github.com/elang194) |
| Hendri Aldi Zulfan | 120140186 | Programer | [henhen02](https://github.com/henhen02) |
| Daffa Sandi Ramadhan | 120140193 | Charachter Design | [AsNodt](https://github.com/AsNodt) |
| Muhammad Nur Aziz | 120140175 | Game Designer | [mhhmadaziz](https://github.com/mhhmadaziz) |
| Bagus Ardin Saputra | 120140176 | Audio Engineer | [Bagusardin](https://github.com/Bagusardin) |
| Reyhan Gandaresta | 120140183 | Level Editor | [ReyhannGR](https://github.com/ReyhanGR) |
## About The Project

Lost Princess is a game that is about the adventures of a knight in a demon kingdom to save the princess who was kidnapped by the devil, and to defeat the evil king. This game is inspired by the popular game [Super Mario Bros](https://en.wikipedia.org/wiki/Mario_Bros.).
## Built With

![python](https://img.shields.io/pypi/pyversions/latest?color=green)

This game is developed with [Python 3.7](https://www.python.org/). And uses the following libraries:
* [PyGame](https://www.pygame.org/)
### Optional

If you want to use the game on your [Docker](https://www.docker.com/) container, you can install the following:

Linux
* [Docker Engine](https://www.docker.com/products/docker-engine)

Windows and MacOS
* [Docker Desktop](https://www.docker.com/products/docker-desktop)
## Getting Started

This is an example of how you may give instructions on setting up your project locally. To get a local copy up and running follow these simple example steps.
### Prerequisites

* A system running [Linux](https://www.linux.org/), [Windows](https://www.microsoft.com/en-us/windows/) or [MacOS](https://www.apple.com/macos/)
* [Git](https://git-scm.com/)
* [Python 3.7](https://www.python.org/)
* [Pygame](https://www.pygame.org/)
* [Docker](https://www.docker.com/) (Optional)
## Run Game Locally Without Docker (Recommended)
### Step 1: Clone the repository

First you need to install the [Git](https://git-scm.com/) client on your system. Then clone the repository.
```bash
git clone https://github.com/elang194/TUGAS-BESAR-PBO-ITERA-2021-2022.git
```
Then you can start working on your project.
```bash
cd TUGAS-BESAR-PBO-ITERA-2021-2022
```
### Step 2: Install the dependencies

Install dependencies by running the following command:
```bash
pip install -r requirements.txt
```
### Step 3: Run the game

Run the game by running the following command:
```bash
python main.py
```
or 
```bash
python3 main.py
```
### Step 4: Play the game

You can play the game by pressing the following keys:

|Keys|In Menu|In Game|
|:---:|:---:|:---:|
| `W` | move up | Jump |
| `S` | move down | - |
| `A` | move left | Run to left |
| `D` | move right | Run to right |
| `P` | - | Attack (not work yet) |
| `Space` or `Enter` | select | - |
| `Esc` | back | Pause |

To win the game and unlock the next level, you need to get the player into the predetermined point in each of level.
## Run Game Locally With Docker (Optional)
### Youtube Tutorial

Unfortunately, we make this video just in MacOs system, soon we will make how to run this game with Docker on Linux and Windows specifically on this repository as soon as possible.

`note : ` If sound is not working in your phone, you can try to play it in your Desktop.

[![Youtube](./Assets/Docs/YouTube%20Thumbnail.jpg)](https://youtu.be/FSOSgkzh_t0)
## UML Diagram

On progress
## Screenshots

This game is under development, so there is no screenshot yet.
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (e.g. `feature/new-feature`)
3. Commit your Changes (git commit -m 'message')
4. Push to the Branch (git push origin feature/new-feature)
5. Open a Pull Request