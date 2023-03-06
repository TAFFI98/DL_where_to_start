# Where to start

This is a quick guide detailing what you should look at based on your background, skills and previous experiences with Machine Learning and Deep Learning.

**Content**:

- [Where to start](#where-to-start)
  - [Summary](#summary)
  - [Prerequisites](#prerequisites)
  - [General understanding](#general-understanding)
  - [Practical knowledge](#practical-knowledge)
  - [Resources](#resources)

## Summary

In summary there are three steps when studying ML/DL (or pretty much any topic).

1. Prerequisites: for ML and DL specifically we are talking about **linear algebra**, **statistics** and programming, mainly **Python**
2. General understanding: the basic concepts of DL such as **dense networks**, **loss**, **backpropagation**, **convolution** (CNN), **recurrence** (LSTM). Without delving too much into the maths, just getting a general understanding of their behavior and inner workings.
3. Practical and detailed knowledge: Python libraries such as **TensorFlow**, **Keras**, **PyTorch**, technical concepts such as **callbacks**, **optimizers**, **datasets**, best practices, common patterns and so on.

These steps should be followed in order: it does not make any sense to go in the specifics of Keras if you don't know what a neural network is or without having grasped the basics of Python.

This does not mean that you should necessarily start from the beginning or dedicate the same amount of time to each step. You might already be familiar with Python or you might already have an intuitive knowledge about the basics of DL. What you have to do is follow these steps and spend some time learning what you don't know yet.  
Note that step 2 and 3 in particular cannot be easily separated: you should definitely start with a general view of the most common concepts without looking at practical implementation and codes, but from a  certain point on the practical part becomes crucial and from that point onwards the two will go hand in hand. You will always find new concepts to learn.

## Prerequisites

Other than some bachelor level knowledge of linear algebra and statistics the most important prerequisite to learn DL is to know how to program in Python.  
It's hard to say exactly how confident you should feel before moving on, but for sure some things that you will need to know are:

- Basics of Python like syntax, how to use packages, how to write, run and debug a script.
- Data types, collections (lists, dictionaries, sets, comprehensions, iterators), common structures and patterns.
- File handling (opening, reading and writing files).
- Not necessarily mandatory, but can often be useful (depends on the application of DL): image handling (PIL package) and basic knowledge of the `panda` package.
- It's not as much of a prerequisite because it can be learnt along the way with DL packages, but the use of the packages `numpy` and `matplotlib`. If you already know `Matlab` they will look really familiar.
- The basics of Object Oriented Programming (OOP), classes and inheritance.

One brief note regarding the OS: there is not much preventing you from using Windows or MacOS for this kind of work, especially at the beginning, but the more you go deeper the more you will realize that Linux is the _de facto_ standard for programming and data science. Some programs might only be available for Linux, some models might be built on Linux and have no guarantee to work on other systems and so on.  
For Windows in particular it has to e said that it is not really programmer-friendly and some things might make your life more difficult.

You can choose to start with the system you are most familiar with and possibly switch at a later time or to switch immediately and learn Linux along with everything else. In any case the best thing to do is not replacing your current OS with a Linux OS, but to do what is called a dual-boot installation, where you place both systems on your computer and choose at startup which one to open. You will find lots of guides on how to do this online. Other alternatives to this, such as using the Windows Subsystem for Linux (WSL) or a virtual machine, are not as effective especially in teh DL field due to the intensive load on the system resources.

## General understanding

Deep Learning is a really complex topic, built on lots of math which can be quite difficult to digest, especially if you come from a more practical field such as engineering. The good news is most of the math is not *that* important.  
You should definitely try and understand it as much as you can, but an intuition-level understanding will usually be more than enough. Try focusing on understanding how things work and build upward from that. Most concepts in DL can be treated with a grey box approach: you should know what happens inside, but knowing how the output is correlated to the input should be your top priority. By doing this over time you will form a collection of "building blocks" that you will be able to use and put together without knowing too much about their inner workings (although at times some deeper research will definitely be needed).

This is a non-exhaustive list of concepts you should be familiar with, in no particular order:

- basic structure of a neuron and of a neural network (weights, bias, activation function)
- deep or fast-forward networks
- various types of loss functions, their characteristics and when they are used
- backpropagation, gradients and related problems (exploding/vanishing gradient, gradient descent)
- data pipelines, preprocessing, data labeling
- key concepts such as batches, epochs, checkpoints, datasets, input and output, training, validation and testing
- regression vs classification
- normalization and batch normalization
- transfer learning
- data augmentation
- data types (basic data types, images, series, time series)
- convolution and Convolutional Neural Networks (CNN)
- recurrence and Recurrent Neural Networks (RNN, LSTM)
- learning from demonstration
- unsupervised learning (GANs, autoencoders)

## Practical knowledge

Python is definitely the most used language for DL and the most used libraries are:

- **TensorFlow**: a package implementing tensor operations. It does not do DL by itself, but acts as a "back-end" other libraries use.
- **Keras**: a package implementing most common DL concepts. It requires a backend, TensorFlow most commonly.
- **PyTorch**: a package implementing both the tensor backend and the DL front-end in a single package.

TF+Keras and PyTorch have lots of similarities, but differences as well. The discussion online about which one is best are endless, but the truth is that they are both valid with advantages and disadvantages. My suggestion for a beginner is to go with TF+Keras because there are more structured resources that explain how to use them and they offer more intuitively packaged features.

If you have heard anything about using the GPU of your machine to run DL models faster you can 99% forget about it. Varying with the exact model of your computer and GPU it can be a real pain to correctly set up a GPU-based environment and it usually is not worth the time just for learning (it definitely is worth the time when you will be doing some serious work, but that will come later and you wil lbe far more knowledgeable).

A tool that is particularly useful for starters is [Google Colab](https://colab.research.google.com). It's a service provided by Google for free (premium paid services are available as well). It provides you with a fully configured Python working environment for machine and deep learning, accessible via web, running on Google's servers.  
This means that:

- The resources (CPU, RAM, GPU) of your machine are not a limitation since everything runs on Google servers. They even offer GPUs free to use (with some [very sensible limitations](https://research.google.com/colaboratory/faq.html#resource-limits)).
- You don't have to download, install or configure **anything** on your machine: you just open a web page and everything is there.
- Obviously this requires an internet connection.
- File management is a bit tricky: you do not have direct access to files stored on your computer, but can connect to your Google Drive account and access those files. Still, you won't need this for most of the basic tutorials/examples you might want to experiment with.
- Sessions expire after some hours, so you cannot leave files and expect them to still be there the next day. You will have to save them to Drive and learn how to load them to start from where you left. This can be a hassle, but once again, it won't be needed for most of your learning work.

## Resources

The [resource folder](learning-resources) contains a curated collection of useful resources to explore Deep Learning and Machine Learning. Feel free to browse around: the following is a short guide on which resources might be more helpful for each stage.

To start with Python most tutorials available online will be OK. [This](learning-resources/W3Schools%20Python%20reference.md) is a good reference to access and get answers quickly.

To explore the general understanding there are three great courses on neural networks and machine learning: [this one from MIT](learning-resources/MIT%206.S191%20-%20Intro%20to%20deep%20learning.md) , [this one from Coursera on ML/DL introduction](learning-resources/Coursera%20Machine%20Learning.md), [this one from  Washington State University](https://sites.wustl.edu/jeffheaton/t81-558/) and [this one from Coursera specific on DL ](learning-resources/Coursera%20Deep%20Learning%20Specialization.md) .  
They are all valid and offer quality insights to most basic DL concepts.

Finally, for the practical part, there is [this course from WU](learning-resources/WU%20T81%20558%20-%20Applications%20of%20Deep%20Neural%20Networks.md) which covers most topics very thoroughly and is very programming-oriented as well as [this blog](learning-resources/Machine%20learning%20mastery.md) which covers a multitude of topics in great details, with tutorials and examples.
