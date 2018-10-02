from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import MeshLinePlot
from kivy.clock import Clock
from math import sin, pi


class Logic(BoxLayout):
    def __init__(self, ):
        super(Logic, self).__init__()
        self.flag_start_stop = False
        self.theta = 0
        self.plot = list()
        self.plot.append(MeshLinePlot(color=[1, 0, 0, 1]))
        self.plot.append(MeshLinePlot(color=[0, 1, 0, 1]))

    def start(self):
        if self.flag_start_stop is False:
            for plot in self.plot:
                self.ids.graph.add_plot(plot)

            Clock.schedule_interval(self.get_value, 1 / 60)
            self.flag_start_stop = True

    def stop(self):
        if self.flag_start_stop is True:
            Clock.unschedule(self.get_value)
            self.flag_start_stop = False

    def get_value(self, dt):
        self.plot[0].points = [(x, sin(x / 10 + self.theta)) for x in range(0, 180)]
        self.plot[1].points = [(x, sin(x / 10 + ((2 * pi) / 2) + self.theta)) for x in range(0, 180)]
        self.theta += dt


class MotionGraph(App):
    def build(self):
        return Builder.load_file("MotionGraph.kv")


if __name__ == "__main__":
    MotionGraph().run()
