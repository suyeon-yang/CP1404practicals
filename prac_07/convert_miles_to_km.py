from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60


class ConvertMilesToKm(App):

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root

    def calculate_km(self):
        input_value = self.do_validation()
        result = input_value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, delta):
        input_value = self.do_validation()
        self.root.ids.input_label.text = str(input_value + delta)

    def do_validation(self):
        try:
            input_value = float(self.root.ids.input_label.text)
            return input_value
        except ValueError:
            return 0


ConvertMilesToKm().run()
