# physical-constant

A module for physical constant in Python, along with unit conversion feature.

## Introduction

The following definition is extracted from Wikipedia page [physical constant](https://en.wikipedia.org/wiki/Physical_constant):

> A physical constant, sometimes fundamental physical constant or universal constant, is a physical quantity that is generally believed to be both universal in nature and have constant value in time. It is contrasted with a mathematical constant, which has a fixed numerical value, but does not directly involve any physical measurement.

There are two parts in this project: 

* **constant**: a module including physics constant;
* **conversion**: a module doing unit conversion.

## Module: constant

The **constant** module will be organized in such manner:
``` python
VAR = value # <symbol> [unit] {relative standard uncertainty} <explanation>
```
where the value is refered to Wikipedia page [physical constant](https://en.wikipedia.org/wiki/Physical_constant).

## Module: conversion

The **conversion** module will be organized in such manner:
``` python
def UNITA_2_UNITB(varA):
    '''
        description
    '''
    {conversion program}
    return varB
```
where `varA` is a value in `UNITA` and `varB` is a value in `UNITB`.