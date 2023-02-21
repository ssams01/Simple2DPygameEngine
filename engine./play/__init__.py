################## ENTITY MAKERS ######################################

def make_frame_viewer(x, y):
    import engine.play.entity.frameviewer as fv
    frameViewer = fv.FrameViewer(x, y)
    return frameViewer
    
def make_game_looper(content = None):
    import engine.play.entity.gameloop as gl
    v = gl.GameLooper()
    v.verbose = True
    if content != None:
        for c in content: 
            v.insert_entity(c)
    return v

################## ACTIONS ############################################

def make_screen_display_action():
    import engine.play.action.updateDisplay as us
    return us.ScreenDisplay()

def make_terminate_action():
    import engine.play.action.quit as tg
    return tg.Terminate()

def make_screen_resize_action():
    import engine.play.action.screen_resize as sr
    return sr.ScreenResize()