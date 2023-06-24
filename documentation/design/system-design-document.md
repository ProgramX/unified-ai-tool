
## "Unified AI Tool": System Design Document

`Author: Mujtaba`
`Date: 24/6/2023`



### System Design

Here, system architecture is discussed using program graph.

#### Context (Scene)

Context is a scene. It is a collection of nodes. It is the starting point of the program. It is the home to the root node. It has an igniter that starts the main node.


For example, if a ButtonNode defines a button's functionality,how can it be displayed if there is no Qt-instance and a main window with some frame etc is running? So, we neeed to keep everything instanced, approipriate and so on.

#### Igniter

Program starts with "igniter", which is responsible for initializing the system and starting the main loop. It ignites the root node.

#### Node

Everything you see is a node!

"Node", is a basic functional unit capable of rendering itself. A node can have links with
any other node in the program. It can access the data of any other node it is connected to.
E.g. `this.get("some_other_node").any_data_variable = xyz;`


Consider an interesting use-case: Suppose we have a search-bar and a button arranged horizontally. We define this functionality in class extending from base node. Now we simply instance that class at any other GUI node, and it will work exavtly identically. This is exactly the design principle of Godot Engine, which allows scene instancing.


The program works like this: We have a scene as the starting point. It establishes the framework for the "Node" to execute. The node can have its own functionality, as well as attached nodes which add their own functionality to the parent node.

Now if we make an entire scene as a child of some node in current scene, the current scene already has context, so it will only be inheriting the nodes from other scene, not the scene itself. Essentially, everything below the root node will be transferred, but root itself, which communicates with, or is being triggered by the igniter/context will be ignored.

