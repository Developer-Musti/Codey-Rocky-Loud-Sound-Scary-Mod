import codey, event, time, rocky

@event.start
def on_start():
    while True:
      codey.display.show_image("00003c7e7e3c000000003c7e7e3c0000")
      if codey.sound_sensor.get_loudness() > 15:
        codey.emotion.startle()