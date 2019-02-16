from webapp2 import Route

routes = [
    Route('/', name='home', handler='app.views.clock_event.CreateClockEventHandler'),
    Route('/create-clock-event', name='create-clock-event', handler='app.views.clock_event.CreateClockEventHandler')
]
