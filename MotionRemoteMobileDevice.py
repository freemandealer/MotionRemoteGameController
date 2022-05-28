#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from plyer import accelerometer
import socket

interface = Builder.load_string('''
#:import facade plyer.compass
<CompassInterface>:
    facade: facade
    orientation: 'vertical'
    padding: '20dp'
    spacing: '10dp'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, .1
            Button:
                id: enable_button
                text: 'Enable Sensor'
                disabled: False
                on_release:
                    root.enable()
                    disable_button.disabled = not disable_button.disabled
                    enable_button.disabled = not enable_button.disabled
            Button:
                id: disable_button
                text: 'Disable Sensor'
                disabled: True
                on_release:
                    root.disable()
                    disable_button.disabled = not disable_button.disabled
                    enable_button.disabled = not enable_button.disabled
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: "Earth's Magnetic Field"
            Label:
                text: 'including hard iron calibration'
            Label:
                text: '(' + str(root.x_calib) + ','
            Label:
                text: str(root.y_calib) + ','
            Label:
                text: str(root.z_calib) + ')'
            Label:
                text: "Earth's Magnetic Field"
            Label:
                text: 'w/o hard iron calibration'
            Label:
                text: '(' + str(root.x_field) + ','
            Label:
                text: str(root.y_field) + ','
            Label:
                text: str(root.z_field) + ')'
            Label:
                text: 'Hard Iron Calibration'
            Label:
                text: '(' + str(root.x_iron) + ','
            Label:
                text: str(root.y_iron) + ','
            Label:
                text: str(root.z_iron) + ')'
            Label:
                text: 'All the values are in μT'
''')


class CompassInterface(BoxLayout):

    x_calib = NumericProperty(0)
    y_calib = NumericProperty(0)
    z_calib = NumericProperty(0)
    x_field = NumericProperty(0)
    y_field = NumericProperty(0)
    z_field = NumericProperty(0)
    x_iron = NumericProperty(0)
    y_iron = NumericProperty(0)
    z_iron = NumericProperty(0)

    facade = ObjectProperty()

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('192.168.43.56',8080))
    #client.connect(('192.168.1.8',8096))
    client.send("hello".encode('utf-8'))

    def enable(self):
        self.facade.enable()
        accelerometer.enable()
        Clock.schedule_interval(self.get_field, 1 / 40.)
        Clock.schedule_interval(self.get_field_uncalib, 1 / 40.)

    def disable(self):
        self.facade.disable()
        Clock.unschedule(self.get_field)
        Clock.unschedule(self.get_field_uncalib)

    def get_field(self, dt):
        if self.facade.field != (None, None, None):
            self.x_calib, self.y_calib, self.z_calib = self.facade.field
            msg_orient = "1 1 " + format('%.2f' % self.x_calib + " 0000000000000000")
            self.client.send(msg_orient.encode('utf-8')[:16])
        val = accelerometer.acceleration[:3]
        if val != (None, None, None):
            msg_accel = "1 0 " + format('%.2f' % val[1]) + " 0000000000000000"
            self.client.send(msg_accel.encode('utf-8')[:16])

    def get_field_uncalib(self, dt):
        if self.facade.field_uncalib != (None, None, None, None, None, None):
            self.x_field, self.y_field, self.z_field, self.x_iron,\
                self.y_iron, self.z_iron = self.facade.field_uncalib


class CompassTestApp(App):
    def build(self):
        return CompassInterface()


if __name__ == '__main__':
    CompassTestApp().run()
