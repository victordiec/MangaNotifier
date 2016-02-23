# MangaNotifier
This is a widget for manga fans. Instead of RSS notifiers from different sites, this is a widget that polls from multiple sites.

Currently, we are trying to use Android visual studio to build this for android users.

We are using Python for the back end.

#Environment

We are using [Oracle VM VirtualBox](https://www.virtualbox.org) to run our virtual machines.

Development is being done on both [Ubuntu](https://www.ubuntu.com) and [Fedora](https://getfedora.org)

We are using the [Atom](https://atom.io/) text editor.

#Installation

##Prerequisites
* Python 3
* Pip
* Git

##Setup

1. Install virtualenv

    ```sudo pip install virtualenv```

2. Clone the repository

    ```git clone https://github.com/roberthluo/MangaNotifier.git```

3. Change to the project directory

    ```cd MangaNotifier```

4. Setup a new virtual environment

    ```virtualenv venv```

5. Activate the virtual environment

    ```source venv/bin/activate```

6. Install dependencies

    ```pip install -r setup/requirements.txt```

##Finishing up

When done working, you can exit the virtual environment using:

```deactivate```
