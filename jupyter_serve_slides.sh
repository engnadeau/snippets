#!/usr/bin/env bash

jupyter nbconvert $1 --to slides --post serve
