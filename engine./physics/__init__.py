#
# Entity
#

def make_particles():
    import engine.physics.entity.particles as part
    result = part.Particle()
    return result

def make_rectangle_collider(llc, urc):
    import engine.physics.entity.rectangle_collider as rc
    result = rc.RectangleCollider(llc,urc)
    return result

def make_gravity_force():
    import engine.physics.entity.gravity_force as gf
    result = gf.GravityForce()
    return result

def make_spring_force():
    import engine.physics.entity.spring_force as sf
    result = sf.SpringForce()
    return result

def make_drag_force():
    import engine.physics.entity.drag_force as df
    result = df.DragForce()
    return result

#
# Actions
#

def make_pick_position_action(i):
    import engine.physics.action.pick_position as pp
    return pp.PickPositionAction(i)

def make_position_solve_action():
    import engine.physics.action.position_solve as ps
    return ps.PositionSolveAction()

def make_activate_action():
    import engine.physics.action.activate as ae
    return ae.Activate()

def make_deactivate_action():
    import engine.physics.action.deactivate as de
    return de.Deactivate()

def make_euler_solve_action():
    import engine.physics.action.euler_solve as es
    result = es.EulerSolveAction()
    return result

def make_velocity_solve():
    import engine.physics.action.velocity_solve as vs
    result = vs.VelocitySolveAction()
    return result

### Colliders

def make_inside_rectangle_collision():
    import engine.physics.action.inside_rectangle_collision as irc
    result = irc.InsideRectangleCollisionAction()
    return result

def make_outside_rectangle_collision():
    import engine.physics.action.outside_rectangle_collision as orc
    result = orc.OutsideRectangleCollisionAction()
    return result

#
# Force Action
#

def make_gravity_action():
    import engine.physics.action.gravity_force_action as gfa
    result = gfa.GravityForceAction()
    return result


def make_spring_action():
    import engine.physics.action.spring_force_action as sfa
    result = sfa.SpringForceAction()
    return result


def make_drag_action():
    import engine.physics.action.drag_force_action as dfa
    result = dfa.DragForceAction()
    return result