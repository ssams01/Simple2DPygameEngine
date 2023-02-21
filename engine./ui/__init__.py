 ### 
###  Entities 
### 
 
def make_basic_button( bounds, color ): 
    import engine.ui.entity.basicButton as bu 
    result = bu.Button(bounds,color) 
    return result 
 
def make_hud():
    import engine.ui.entity.hud as hd
    hud = hd.hud()
    return hud
 
### 
### Actions 
### 
 
def make_button_press_action(): 
    import engine.ui.action.press_button as bp 
    return bp.ButtonPressed() 
 
def make_draw_button_action(): 
    import engine.ui.action.draw_button as db 
    return db.DrawRectButtonAction() 

def make_draw_hud_action():
    import engine.ui.action.draw_hud as dh
    return dh.DrawHud()
 