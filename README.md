[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-shield]

# OneShot - Italian Translation

This project is a translation of the game "OneShot".

<sup><sub>Progress (line): 270/7105 (3.80%)</sub></sup>

## Requirements

- OneShot (Obviously)

## Installation

1. Download the it.loc file (not ready yet).
2. Move the it.loc file to the OneShot game folder (inside steamapps/common).
3. Execute the following commands inside the OneShot languages folder:

   ```sh
   mv en.loc en.loc.bak
   mv it.loc en.loc
   ```
4. Open the OneShot game and enjoy!

## Build (Buggy and unfinished)

1. Download the it.txt file (beta).
2. Download the mklang.rb file from the OneShot mkxp github repository [here](https://github.com/elizagamedev/mkxp-oneshot/blob/master/mklang.rb)
3. Clone this repository
   ```sh
   git clone https://www.github.com/ImJstNickDev/OneShot-ITA.git
   ```
4. Install the get_pomo gem with
   ```sh
   gem install get_pomo
   ```
5. Run the following command inside the OneShot languages folder
   ```sh
   ruby mklang.rb it.txt it.loc
   ```
6. Proceed with the installation process.
<br>
<br>

## Credits

Special thanks to this repository: [elizagamedev/mkxp-oneshot](https://github.com/elizagamedev/mkxp-oneshot) for sharing the OneShot mkxp repository and code. Without it, this project would not have been possible.

## License


[GPL-3.0](LICENSE) © [ImJstNickDev](https://www.github.com/ImJstNickDev).


[contributors-shield]: https://img.shields.io/github/contributors/ImJstNickDev/OneShot-ITA.svg?style=for-the-badge
[contributors-url]: https://github.com/ImJstNickDev/OneShot-ITA/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ImJstNickDev/OneShot-ITA.svg?style=for-the-badge
[forks-url]: https://github.com/ImJstNickDev/OneShot-ITA/network/members
[stars-shield]: https://img.shields.io/github/stars/ImJstNickDev/OneShot-ITA.svg?style=for-the-badge
[stars-url]: https://github.com/ImJstNickDev/OneShot-ITA/stargazers
[issues-shield]: https://img.shields.io/github/issues/ImJstNickDev/OneShot-ITA.svg?style=for-the-badge
[issues-url]: https://github.com/ImJstNickDev/SCL_SmartphoneManagerSite/issues
[license-shield]: https://img.shields.io/github/license/ImJstNickDev/OneShot-ITA.svg?style=for-the-badge
[license-url]: https://github.com/ImJstNickDev/SCL_SmartphoneManagerSite/blob/master/LICENSE