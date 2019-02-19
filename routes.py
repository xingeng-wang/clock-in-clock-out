from webapp2 import Route

routes = [
    Route('/', name='home', handler='src.app.views.home.HomeHandler'),
    Route('/create-clock-event', name='create-clock-event', handler='src.app.views.clock_event.CreateClockEventHandler'),
    Route('/list-clock-event', name='list-clock-event', handler='src.app.views.clock_event.ListClockEventHandler')
]
