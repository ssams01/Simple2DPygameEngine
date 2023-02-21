################## ENTITY MAKERS ######################################

def make_rect(nx, ny, width, height, red, green, blue):
    import engine.actor.entity.rect as r
    return r.Rectangle((red, green, blue), nx, ny, width, height)

def make_circ(nx, ny, radius, red, green, blue):
    import engine.actor.entity.circ as c
    return c.Circle((red, green, blue), nx, ny, radius)

def make_letter(nx, ny, red,green,blue, letter):
    import engine.actor.entity.letter as l
    return l.Letter(nx, ny, (red,green,blue),letter)

def make_word(nx, ny, red,green,blue, letter,name):
    import engine.actor.entity.word as w
    return w.Word(nx, ny, (red,green,blue),letter,name)

################## DISPLAY ACTIONS #################################### 

def make_draw_rect():
    import engine.actor.action.drawRect as dr
    return dr.DrawRectangle()

def make_draw_circ():
    import engine.actor.action.drawCirc as dc
    return dc.DrawCircle()

def make_draw_letter():
    import engine.actor.action.drawLetter as dl
    return dl.DrawLetter()

def make_draw_word():
    import engine.actor.action.drawWord as dw
    return dw.DrawWord()

#makes the call to checkLetter action and passes in the generated word
def make_check_letter(word):
    import engine.actor.action.checkLetter as cl
    return cl.CheckLetter(word)   

def make_put_position_action():
    import engine.actor.action.put_position as pp
    return pp.PutPositionAction()

def make_is_inside_action():
    import engine.actor.action.is_inside as ii
    return ii.IsInside()