import api_servie
aObj    = api_servie.api_servie()
class cmd_handler:
    def __init__(self):
        pass

    def run(self, request):
        
        cmd_id  = request.json.get('cmd_id', '')
        if cmd_id == 'get_data':
            pin = request.json.get('pin','')
            return aObj.get_data(pin)
        elif cmd_id== 'get_pins':
            return aObj.get_pins()
        elif cmd_id=='get_plot':
            return aObj.plotter()
        else:
            return {}


if __name__ == "__main__":
    obj = cmd_handler()
    # obj.run()