# SCSS Compiler

A Sublime Text 3 plugin which compiles the selected SCSS to CSS in your document window.
This plugin depends on ruby being installed and the `scss` compiler binary being installed via ruby gems.

### Usage
Select the SCSS which you wish to compile, right click and select "Compile selected SCSS to CSS". You may need to wait a few seconds for the compilier to do it's thing, and then your SCSS should then be transformed into CSS!

---
# Installation on Linux & OS X 

Open a Terminal window and run the following command:
```
sudo gem install sass
```
This script assumes that the `scss` binary is installed in the following location: `/usr/local/bin`.

# Installation on Windows

Download and install the [Ruby installer](https://rubyinstaller.org/).

**Ensure the "Add Ruby executables to your PATH" is enabled during the installation process.**

Open an Admin Command or PowerShell window and run the following command:
```
gem install sass
```
