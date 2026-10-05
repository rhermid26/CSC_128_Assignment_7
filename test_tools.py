from tools import check_availability, get_hours, book_room, AVAILABLE_TOOLS


TEST_TOOLS_DATA = [
    {
        "function_name" : "check_availability",
        "arguments" : {
            "day" : "tuesday"
        }
    },
    {
        "function_name" : "get_hours",
        "arguments" : {
            "day" : "tuesday"
        }
    }
]
def test_tool(function_name, args):
    return AVAILABLE_TOOLS[function_name](**args) 


for func_data in TEST_TOOLS_DATA:
    print(test_tool(func_data["function_name"], func_data["arguments"]))