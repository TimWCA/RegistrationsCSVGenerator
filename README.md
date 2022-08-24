# Registrations CSV Generator
This program generates registrations.csv file (for WCA) from FunCubing. You can use it for Grouppifier on Russian competitions.

## Launch
### On Windows
Just launch generator.exe from Releases page:)

### On Linux
For linux you should install Python 3. Example for Fedora Linux:
```bash
$ dnf install python3
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
