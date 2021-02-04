from math import sqrt

total_arm_length = 25

def distance(p0, p1):
    return sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

class Astrobot:
    def __init__(self, x_astrobot, y_astrobot):
        self.x_astrobot, self.y_astrobot = x_astrobot, \
                                           y_astrobot
class Target:
    def __init__(self, x_target, y_target):
        self.x_target, self.y_target = x_target, y_target

    def get_reachable_set(self, unassinged_astrobots):
        return [astrobot for astrobot in
                unassinged_astrobots if distance(self,
                                                 astrobot) <= total_arm_length]
    def avg_coord(self, assingned_astrobots):
        x_avg, y_avg = sum(e[0] for e in assingned_astrobots), sum(e[1] for e
                                             in assingned_astrobots)/len(assingned_astrobots)
        return x_avg, y_avg

    def assign(self, unassigned_astrobots,
               assinged_astrobots):
        min = 100000
        minimizer = unassigned_astrobots[0]
        reachable_set = self.get_reachable_set(unassigned_astrobots)
        avg = self.avg_coord(assinged_astrobots)
        for astrobot in reachable_set:
            eval = distance(self, astrobot)/ distance(
                avg, astrobot)
            if eval < min:
                min = eval
                minimizer = astrobot
        return [self, minimizer]

astrobots = []
targets = []

astrobot1 = Astrobot(0,0)
astrobot2 = Astrobot(2,2)
astrobots.append(astrobot1)
astrobots.append(astrobot2)

target1 = Target(0.5,1)
target2 = Target(1,0.5)
targets.append(target1)
targets.append(target2)

pairings = []

assert(len(astrobots) == len(targets))

assigned_astrobots = []
unassigned_astrobots = astrobots

for target in targets:
    pair = target.assign(unassigned_astrobots,
                     assigned_astrobots)
    pairings.append(pair)
