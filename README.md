# physical-constant

A module for physical constant in Python, along with unit conversion feature.

## 0. Introduction

The following definition is extracted from Wikipedia page [physical constant](https://en.wikipedia.org/wiki/Physical_constant):

> A physical constant, sometimes fundamental physical constant or universal constant, is a physical quantity that is generally believed to be both universal in nature and have constant value in time. It is contrasted with a mathematical constant, which has a fixed numerical value, but does not directly involve any physical measurement.

There are two parts in this project: 

* a module including physics constant;
* a module doing unit conversion.

This project is available in my GitHub repository [physics-constant](https://github.com/JackRBlack/physics-constant).

The **constant** module will be organized in such manner:
``` python
VAR = value # <symbol> [unit] {relative standard uncertainty} <explanation>
```
where the value is refered to Wikipedia page [physical constant](https://en.wikipedia.org/wiki/Physical_constant).