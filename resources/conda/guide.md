# Brief guide to `conda`

This is a brief guide to the use of `conda`.  
This guide assumes that you are using a Linux machine and have correctly installed `conda`. 

**Contents**:
- [Brief guide to `conda`](#brief-guide-to-conda)
  - [Activate `conda`](#activate-conda)
  - [Create a new virtual environment](#create-a-new-virtual-environment)
  - [Install and manage packages](#install-and-manage-packages)
  - [Find packages](#find-packages)
  - [Replicating environments](#replicating-environments)
  - [General advice](#general-advice)

## Activate `conda`

First of all look at your prompt, if it is something along the lines of the following you are all set and can skip to the next session:

```bash
(base) user@computer_name:/path/to/current$
```

If, instead, you are missing the `(base)` part at the start of the line, like here:

```bash
user@computer_name:/path/to/current$
```

you will need to activate `conda` by executing this command:

```bash
conda activate
```

This should change your prompt to the one at the beginning of this section.

## Create a new virtual environment

Now you are using the `base` environment, which is the default one. This can be used like a normal python installation for day-to-day use, especially if you installed `Anaconda` and have lots of packages already available.  
The most interesting feature, however, is creating a new virtual environment, which can be done with:

```bash
conda create --name "env_name"
```

Now you should still be in the `base` environment, but if you run

```bash
conda env list
```

you will see the new environment along with the `base` one.

You can switch to your new environment by executing:

```bash
conda activate env_name
```

You should see the prompt changed to:

```bash
(env_name) user@computer_name:/path/to/current$
```

If you wish to remove an environment run:

```bash
conda env remove --name env_name
```

## Install and manage packages

Now, to see a list of the packages available in your environment you can run:

```bash
conda list
```

Most probably you won't see any package. In fact, this new environment does not even have Python installed it's just an empty container!

Let's install Python and some packages by running

```bash
conda install python=3.8 numpy
```

Note that the `=3.8` is used to specify an exact version of the package to be installed. In this case Python 3.8 will be installed along with the most recent version of numpy that supports it.  

You can check that the packages were actually installed by running `conda list` once more or by trying to use the newly installed packages:

```bash
python -c "import numpy as np; print(np.sum([1, 1]))"
```

Removing an installed package is really simple as well:

```bash
conda uninstall numpy
```

Try to list the installed packages now or to use numpy again: it will say the module is not found anymore.

## Find packages

Most common packages can be installed just by trying `conda install package_name`, but more obscure ones might not be available in the default channel. For example this command will fail:

```bash
conda install ipdb
```

A brief search on Google for "conda ipdb" will bring you to [this page](https://anaconda.org/conda-forge/ipdb) which suggests running:

```bash
conda install -c conda-forge ipdb
```

The `-c conda-forge` part of the command tells `conda` to look for that package in the `conda-forge` channel. Channels are additional sources where packages can be distributed. `conda-forge` is one of the most common ones and is community. In general searching for "conda packagename" should tell you if that package is available in the default channel or if it lives in a different one.

## Replicating environments

One of the most powerful features of conda is the ability to replicate environments.

First of all, if you want to experiment with an environment without messing it up you can create a clone copy of that environment, do your experiments and then safely remove it.

```bash
conda create --name my_env_explore --clone my_env_original
conda activate my_env_explore
# Do your stuff here...
conda activate my_env_original
conda env remove my_env_explore
```

At the end `my_env_original` will be untouched.

Environments can be replicated across machines as well.  
You can create a single file collecting all the names and versions of the packages installed in an environment by running:

```bash
conda env export --name my_env >> my_env.yml
```

This will be create a `my_env.yml` file that can be sent to another user or added to a git repository.  
Any other user who want s to replicate this environment can just run:

```bash
conda env create --name my_env_new_name -f my_env.yml
```

This will create an environment named `my_env_new_name` which will contain exactly the same packages of `my_env`. 

## General advice

- Create a new environment for every project.
- Do not rely on the `base` environment too much, otherwise you will miss all the benefits of `conda`. Still, it's useful to treat it like a standard Python installation, where most common packages are installed and ready to use in a pinch.
- Avoid mixing `conda` and `pip` at all costs (i.e. do not run `pip install` inside a `conda` environment). If you must do so install all the packages with `conda` first and use `pip` only at the end.  
  See [here](https://www.anaconda.com/blog/using-pip-in-a-conda-environment) and [here](https://stackoverflow.com/questions/56134588/is-that-a-bad-idea-to-use-conda-and-pip-install-on-the-same-environment) for more details.