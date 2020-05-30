from dialogue_generator import *

node1 = DialogueNode("Hi I'm a dialogue line!")
node2 = DialogueNode("This is another dialogue line! Do you like this dialogue?")
node3 = DialogueNode("This is the end of the dialogue...", break_talk=True, function="talk_test", parameters=["debug"])
node4 = DialogueNode("You're a complicated person...", break_talk=True)

node1.set_next(node2, "")
node2.set_next(node3, "Yes!")
node2.set_next(node4, "No!")

root = DialogueRoot({"global": node1})

tree = DialogueTree(root, "en")
tree.dump_to_json("TestDialogue.json")
