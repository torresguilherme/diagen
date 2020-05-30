import json

class DialogueTree:
    def __init__(self, root, language):
        self.root = root
        self.language = language

    def dump_to_json(self, filename):
        dump = {
            "language": self.language,
            "index": {},
            "nodes": []
        }
        for key in self.root.table.keys():
            node = self.root.get_node_for_state(key)
            dump["index"][key] = node._id
            DialogueTree.dump_node(dump, node)

        dump["nodes"].sort(key=lambda x: x["id"])

        with open(filename, "w") as f:
            json.dump(dump, f)

    def dump_node(full_dict, node):
        if not node.is_dumped:
            result = {}
            result["id"] = node._id
            result["line"] = node.main_line
            result["function"] = node.function
            result["parameters"] = node.parameters
            result["break"] = node.break_talk
            result["options"] = {}
            for key in node.options.keys():
                recursive_dump = DialogueTree.dump_node(full_dict, node.options[key])
                result["options"][key] = node.options[key]._id
            full_dict["nodes"].append(result)
            node.is_dumped = True

class DialogueRoot:
    def __init__(self, table):
        self.table = table

    def get_node_for_state(self, state):
        return self.table[state]

    
class DialogueNode:
    _id = 0

    def __init__(self, main_line, function=None, parameters=None, break_talk=False):
        self._id = DialogueNode._id
        DialogueNode._id += 1

        self.main_line = main_line
        self.function = function
        self.parameters = parameters
        self.break_talk = break_talk
        self.options = {}

        self.is_dumped = False

    def set_next(self, next_node, condition):
        self.options[condition] = next_node
