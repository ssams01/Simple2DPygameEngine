def make_counter(number,name):
    import engine.utility.entity.counter as ct
    counter = ct.Counter(number, name)
    return counter

def make_timer(allottedTime, startTime, currentTime, elapsedTime):
    import engine.utility.entity.timer as ti
    timer = ti.Timer(allottedTime, startTime, currentTime, elapsedTime)
    return timer

def increment_counter_action():
    import engine.utility.action.increment as it
    return it.Increment()

def start_timer_action():
    import engine.utility.action.start_timer as st
    return st.StartTimer()

def update_timer_action():
    import engine.utility.action.update_timer as ut
    return ut.UpdateTimer()

def alarm_action(alottedTime):
    import engine.utility.action.alarm as al
    return al.Alarm(alottedTime)

def activate_action():
    import engine.utility.action.activate as ac
    return ac.Activate()

def deactivate_action():
    import engine.utility.action.deactivate as de
    return de.Deactivate()
