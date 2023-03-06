# `conda`

This is a brief introduction to `conda`, `Anaconda` and `Miniconda`.

For a good `conda` cheat sheet see [here](https://kapeli.com/cheat_sheets/Conda.docset/Contents/Resources/Documents/index).

**Contents:**

- [`conda`](#conda)
  - [What is `conda`?](#what-is-conda)
  - [What is a virtual environment?](#what-is-a-virtual-environment)
  - [What's the difference among `conda`, `Anaconda` and `Miniconda`?](#whats-the-difference-among-conda-anaconda-and-miniconda)
    - [`conda`](#conda-1)
    - [`Anaconda`](#anaconda)
    - [`Miniconda`](#miniconda)
    - [Which one should I choose?](#which-one-should-i-choose)
  - [How do I install one of them?](#how-do-i-install-one-of-them)
  - [How do I use `conda`?](#how-do-i-use-conda)

## What is `conda`?

`conda` is a "package, dependency and environment management" software for many languages, but most importantly for Python.

One of the great features of Python is the multitude of packages (libraries) available, which cover almost any possible need, from web browsing, to file management, data science, plots and graphs, advanced math, image processing and so on.

Such packages can be installed using Python default package manager: `pip`. You might have seen it used simply as `pip install package_name`. What this does is download the necessary files from a registry and install them on your computer. From that moment on you Python installation will have access to that package and you can use it in a script like `import package_name`.

Easy enough isn't it? Definitely, but what about some more complex use cases?

 - What if you are working on two projects: one of them uses `package_A` version `1.1.0` and the other uses `package_A` version `2.0.0`? You cannot have two versions of the same package installed at the same time
 - What if you are working on two projects: one of them runs on Python 3.6 and the other on Python 3.8? You cannot have two versions of Python installed at the same time.
 - You have finally finished working on your project and want to archive everything. You push the final version of the code to your GitHub repository, delete your local copy and now want to remove all the packages that you had installed for that project. But how do you know exactly which packages you had installed? how do you know that you can safely remove them and they are not required for some other project?

There are many solutions to these problems and most of them involve the concept of _virtual environments_.

## What is a virtual environment?

You can think of a virtual environment as a self-contained box. You do anything you want inside it and you can rest assured that nothing on the outside will be affected.

In the specific context of Python virtual environments let you install packages and even different Python versions inside them so that you can:

- have different versions of the same package installed in different environments
- have different Python versions running in different environments
- completely and safely remove an environment once you don't need it anymore

## What's the difference among `conda`, `Anaconda` and `Miniconda`?

### `conda`

`conda` is the name of the program (which you invoke with `conda COMMAND --options`). However, you do not install `conda` by itself: instead you have two options, `Anaconda` or `Miniconda`.

### `Anaconda`

`Anaconda` is a bundle which installs and configures `conda` together with over 7500 data science and machine learning packages as well as some GUI tools.

This means that the `base` virtual environment (the one that is active by default) will already contain 99% of all packages you will need.  
The installation requires approximately 500 MB of disk space.

### `Miniconda`

`Miniconda`, on the other hand, installs and configures `conda` with just the bare minimum to have Python running.

This means that the `base` virtual environment (the one that is active by default) will only contain a standard Python installation and any other package will have to be installed by hand.  
The installation requires approximately 50 MB of disk space.

### Which one should I choose?

Most guides suggest that you should probably go with `Anaconda` if you are just starting and use `Miniconda` only if you know what you are doing or have strict disk space limits.  
However, this is only true if you are planning on using the `base` environment, since the advantage of `Anaconda` is to have it already full of useful packages. If you are planning on creating a dedicated environment for every project (as you probably should) then there is no big difference since all new environments start empty with both `Anaconda` and `Miniconda` and you will have to manually install the required packages anyway.

## How do I install one of them?

Installation of either `Anaconda` or `Miniconda` is quite easy:

- for `Anaconda` download and install the package for your platform [here](https://www.anaconda.com/products/individual#Downloads)
- for `Miniconda` download and install the package for your platform [here](https://docs.conda.io/en/latest/miniconda.html) (note the Python version you are choosing here only affects the `base` virtual environment: you can still use any Python version in the other environments) then follow the [installation instructions](https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation) for your platform.

## How do I use `conda`?

This is just a quick reference of the most used `conda` commands: for a more extensive guide please see the [guide page](guide.md).  
For a good `conda` cheat sheet see [here](https://kapeli.com/cheat_sheets/Conda.docset/Contents/Resources/Documents/index).  

We'll assume that you are on a Linux machine. There might some small differences in a Windows environment.

To activate `conda` execute:

```bash
conda activate
```

This should change your prompt to:

```bash
(base) user@computer_name:/path/to/current$
```

Create a new virtual environment:

```bash
conda create --name "env_name"
```

List all environments:

```bash
conda env list
```

You can switch to another environment:

```bash
conda activate env_name
```

You should see the prompt changed to:

```bash
(env_name) user@computer_name:/path/to/current$
```

See the list of packages available in your environment:

```bash
conda list
```

Most probably you won't see any package: install Python and some packages by running

```bash
conda install python=3.8 package_name
```

You can check that the packages were actually installed by running `conda list` one more time.

Removing an installed package:

```bash
conda uninstall numpy
```

Install a package from a third-party channel:

```bash
conda install -c conda-forge ipdb
```

The `-c conda-forge` part of the command tells `conda` to look for that package in the `conda-forge` channel. Channels are additional sources where packages can be distributed. `conda-forge` is one of the most common ones and is community.