# Bot Framework

Bot framework aims to provide a declarative way of creating bots for various chat platforms.

## Idea

Every conversation can be defined as a Directed Acyclic Graph (DAG) consisting of both input and output nodes. Input nodes are responsible for receiving messages from the user and output nodes are responsible for sending messages to the user. The graph is traversed in a depth-first manner, starting from the root node.

## How to contribute

### Setup

* Install poetry
* Run `poetry install`
* Run the sample project with `poetry run python bot_framework`

## Authors

* Damian Akpan <damiakpan@gmail.com>
