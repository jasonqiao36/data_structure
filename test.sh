#!/usr/bin/env bash

watchmedo auto-restart -d . -p '*.py' -R -- pytest -s $1
