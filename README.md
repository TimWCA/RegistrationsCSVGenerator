# Registrations CSV Generator

Copyright (C) 2022–2023 Timofei Vikhrianov  
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. 
 
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. 
 
You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>. 
 
_This program generates registrations.csv file (for WCA) from FunCubing. You can use it for Grouppifier on Russian competitions._

## Launch
### On Windows
Just download and launch RegistrationsCSVGenerator.exe from the Releases page :)

### On Linux
For linux you should install Python 3. Example for Fedora Linux:
```bash
$ sudo dnf install python3
```
Next launch RegistrationsCSVGenerator.py:
```bash
$ python3 RegistrationsCSVGenerator.py
```

## Usage
![image](https://user-images.githubusercontent.com/52562657/186472149-7fa94ae0-d934-47bf-90a5-e22bbe0862df.png)
Enter your competetion ID here. You can see ID in competition URL. Example:
```
https://funcubing.org/competitions/ID
```
You should have an Internet connection. 
Program will generate registrations.csv file and save it in program directory. 
Everyone has the same gender and date of birth. You can change it manually, but this is not necessary for Grouppifier to work.
