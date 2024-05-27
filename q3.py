#Importing important libraries
import numpy as np
from collections import deque
import heapq

def path(previous, s): 
    if s is None:
        return []
    else:
        return path(previous, previous[s])+[s]

def pathcost(path, step_costs):
    cost = 0
    for s in range(len(path)-1):
        cost += step_costs[path[s]][path[s+1]]
    return cost

state_space_graph_et = dict( {'Addis Ababa': {'Adama':3, 'Ambo':5, 'Debre Berhan':5,'Debre Markos':13},
             'Adama': {'Matahara':3, 'Asella':4, 'Batu':4, 'Addis Ababa':3}, 
             'Ambo': {'Wolkite':6, 'Addis Ababa':5, 'Nekemte':8}, 
             'Debre Berhan': {'Addis Ababa':5, 'Debre Sina':2},
             'Debre Markos':{'Addis Ababa':13,'Debre Sina':17,'Finote Selam':3},
                               
             'Matahara': {'Adama':3, 'Awash':1}, 
             'Asella': {'Adama':4, 'Assasa':4}, 
             'Batu': {'Adama':4, 'Buta Jirra':2, 'Shashamene':3}, 
             'Wolkite': {'Ambo':6, 'Worabe':5, 'Jimma':8,'Hossana':5,'Buta Jirra':4}, 
             'Nekemte': {'Ambo':9, 'Bedelle':5, 'Gimbi':4}, 
             'Debre Sina': {'Debre Berhan':2, 'Kemise':7, 'Debre Markos':17}, 
             'Finote Selam': {'Debre Markos':3, 'Bahirdar':6, 'Injibara':2},
                               
             'Awash': {'Chiro':4, 'Gobi Rasu':5, 'Matahara':1}, 
             'Assasa': {'Asella':4, 'Dodolla':1}, 
             'Buta Jirra': {'Batu':2,'Wolkite':4, 'Worabe':2}, 
             'Shashamene': {'Batu':3,'Dodolla':3, 'Hawassa':1, 'Hossana':7,'Worabe':6}, 
             'Worabe': {'Wolkite':5, 'Hossana':2,'Shashamene':6, 'Buta Jirra':2}, 
             'Jimma': {'Wolkite':8, 'Bonga':4, 'Bedelle':7}, 
             'Hossana': {'Shashamene':7, 'Worabe':2, 'Wolkite':5, 'Wolaita Sodo':4}, 
             'Bedelle': {'Nekemte':5, 'Gore':6, 'Jimma':7}, 
             'Gimbi': {'Nekemte':4, 'Dambidollo':6,'Assosa':8}, 
             'Kemise': {'Debre Sina':6, 'Dessie':4}, 
             'Bahirdar': {'Finote Selam':6, 'Injibara':4, 'Metekel':11, 'Azezo':7, 'Debre Tabor':4},
             'Injibara': {'Bahirdar':4, 'Finote Selam':2},
                               
                               
             'Chiro': {'Awash':4, 'Dire Dawa':8}, 
             'Gobi Rasu': {'Awash':5, 'Samara':10}, 
             'Dodolla': {'Assasa':1, 'Shashamene':3, 'Robe':13}, 
             'Hawassa': {'Shashamene':1, 'Dilla':3}, 
             'Bonga': {'Jimma':4, 'Dawro':10, 'Tepi':8, 'Mizan Teferi':4}, 
             'Wolaita Sodo': {'Arba Minchi':4, 'Dawro':6, 'Hossana':4}, 
             'Gore': {'Tepi':9, 'Gambella':5, 'Bedelle':6}, 
             'Dambidollo': {'Gimbi':6, 'Assosa':12, 'Gambella':4}, 
             'Assosa': {'Gimbi':8, 'Dambidollo':12}, 
             'Dessie': {'Kemise':4, 'Woldia':6},
             'Metekel': { 'Bahirdar':11},
             'Azezo': {'Gondar':1, 'Bahirdar':7, 'Metema':7}, 
             'Debre Tabor': {'Lalibella':8, 'Gondar':6, 'Bahirdar':4},
             
             'Dire Dawa': { 'Chiro':8, 'Harar':4}, 
             'Samara': { 'Gobi Rasu':10, 'Fanti Rasu':7, 'Alamata':11, 'Woldia':8},
             'Robe': {'Liben':11, 'Dodolla':13, 'Goba':18, 'Sof Oumer':23}, 
             'Dilla': {'Hawassa':3, 'Bulehora':4}, 
             'Dawro': { 'Bonga':10, 'Wolaita Sodo':6}, 
             'Tepi': {'Gore':9, 'Bonga':8, 'Mizan Teferi':4}, 
             'Mizan Teferi': {'Tepi':4, 'Bonga':4}, 
             'Gambella': {'Gore':5, 'Dambidollo':4}, 
             'Arba Minchi': {'Wolaita Sodo':5, 'Konso':4, 'Basketo':10},
             'Woldia': {'Dessie':6, 'Lalibella':7, 'Samara':8, 'Alamata':3},
             'Gondar': { 'Azezo':1, 'Humera':9, 'Metema':7, 'Debarke':4,'Debre Tabor':6},
             'Metema': { 'Azezo':7, 'Gondar':7}, 
             'Lalibella': {'Woldia':7, 'Debre Tabor':8, 'Sekota':6},
              
              
             'Harar': { 'Dire Dawa':4, 'Babile':2}, 
             'Fanti Rasu': {'Samara':7, 'Kilbet Rasu':6}, 
             'Alamata': {'Samara':11, 'Woldia':3, 'Mekelle':5, 'Sekota':6}, 
             'Liben': {'Robe':11}, 
             'Goba': {'Robe':18, 'Sof Oumer':6, 'Babile':28}, 
             'Sof Oumer': {'Goba':6, 'Robe':23, 'Gode':23}, 
             'Bulehora': { 'Dilla':4, 'Yabello':3}, 
             'Konso': {'Arba Minchi':4, 'Yabello':3}, 
             'Basketo': { 'Arba Minchi':10, 'Bench Maji':5}, 
             'Humera': { 'Shire':8, 'Gondar':9},
             'Debarke': { 'Gondar':4, 'Shire':7},
             'Sekota': {'Alamata':6, 'Mekelle':9, 'Lalibella':6}, 
             
             'Babile': { 'Harar':2, 'Jigjiga':3,'Goba':28}, 
             'Kilbet Rasu': {'Fanti Rasu':6}, 
             'Mekelle': {'Alamata':5, 'Adigrat':4, 'Adwa':7, 'Sekota':9},
             'Gode': { 'Dollo':17, 'Kebri Dehar':5, 'Sof Oumer':23 }, 
             'Yabello': { 'Bulehora':3, 'Konso':3, 'Moyale':6},
             'Bench Maji': { 'Basketo':5}, 
             'Shire': { 'Axum':2, 'Humera':8, 'Debarke':7},
                               
             'Jigjiga': { 'Babile':3, 'Dega Habur':5}, 
             'Adigrat': { 'Mekelle':4, 'Adwa':4},
             'Adwa': { 'Mekelle':7, 'Axum':1, 'Adigrat':4},
             'Dollo':{'Gode':17,'Moyale':18},
             'Kebri Dehar': {'Gode':5, 'Dega Habur':6, 'Werdez':6}, 
             'Moyale': { 'Dollo':18,'Liben':11,'Yabello':6}, 
             'Axum': {'Shire':2, 'Adwa':1},
             'Dega Habur': {'Jigjiga':5, 'Kebri Dehar':6}, 
             'Werdez': { 'Kebri Dehar':6}
                      }
                    )
Moyale_dist=dict({
             'Addis Ababa':26,
             'Adama':23,
             'Ambo':31,
             'Debre Berhan':31,
             'Debre Markos':39,
             'Matahara':26,
             'Asella':22, 
             'Batu':19,  
             'Wolkite':25,  
             'Nekemte':39, 
             'Debre Sina':33,
             'Finote Selam':42,
             'Awash':27, 
             'Assasa':18, 
             'Buta Jirra':21, 
             'Shashamene':16, 
             'Worabe':22, 
             'Jimma':33,
             'Hossana':21,
             'Bedelle':40, 
             'Gimbi':43, 
             'Kemise':40,  
             'Bahirdar':48, 
             'Injibara':44,
                               
             'Chiro':31,
             'Gobi Rasu':32, 
    
              'Dodolla':19, 
             
              'Hawassa':15, 
             
              'Bonga':33,
              'Wolaita Sodo':17, 
              'Gore':46,  
              'Dambidollo':49,
              'Assosa':51, 
              'Dessie':44, 
              'Metekel':59, 
              'Azezo':55, 
              'Debre Tabor':52,
             
                               
                               
             'Dire Dawa':31, 
             'Samara':42, 
              'Robe':13, 
             'Dilla':12, 
             'Dawro':23, 
             'Tepi':41,
             'Mizan Teferi':37, 
             'Arba Minchi':13, 
             'Gambella':51,  
              
             
             'Woldia':50,
             'Gondar':56, 
             'Metema':62, 
             'Lalibella':57,
             
             'Harar':35, 
             'Fanti Rasu':49, 
             'Alamata':53, 
             'Liben':11, 
             'Goba':40, 
             'Sof Oumer':45, 
              'Bulehora':8, 
              
              'Konso':9, 
             'Basketo':23,
             'Bench Maji':28,
    
             
             'Humera':65, 
             'Debarke':60,
             
             'Sekota':59,
              
              
             'Babile':37, 
             'Kilbet Rasu':55, 
             'Mekelle':58, 
            
             
             'Gode':35, 
             'Yabello':6, 
             'Shire':67, 
             
             
             
            
              'Adigrat':62,
             'Adwa':65, 
              'Dollo':18,
             'Kebri Dehar':40, 
             'Moyale':0,
             
             'Axum':66, 
                               
             'Jigjiga':40,
             'Dega Habur':45, 
             
            
             
             'Kebri Dehar': 40,
             'Werdez':4
        }
        
       )    


class Frontier_PQ():
    def __init__(self, start, cost = 0):
        self.start = start
        self.cost = cost
        self.states = {start:cost} # the explored nodes
        self.q = [[cost, start]] # the can-be-explored nodes
    
    def add(self,state,cost):
        self.states[state]=cost
        heapq.heappush(self.q,[cost,state])
    
    def pop(self):
        return heapq.heappop(self.q)
    
    def replace(self,state,cost):
        self.states[state]=cost
        for i,tup in enumerate(self.q):
            if tup[1]==state:
                self.q[i][0]=cost


def AStar(start, goal, state_graph,  return_cost, return_nexp):
    frontier = Frontier_PQ(start)
    visited = set()
    prev = {start:None}
   
    while frontier.q:
        cost, curr = frontier.pop()
        visited.add(curr)
        if curr == goal:
            p = path(prev, curr)
            if return_nexp == False:
                return (p, pathcost(p, state_graph)) if return_cost else p
            else:
                return (p, pathcost(p, state_graph), len(visited)) if return_cost else (p,len(visited))
       
        for adj in state_graph[curr]:
            if adj not in visited:
                new_cost = cost + state_graph[curr][adj] + Moyale_dist[adj] - Moyale_dist[curr]
                if adj not in frontier.states:
                    prev[adj] = curr
                    frontier.add(adj, new_cost)
                elif frontier.states[adj] > new_cost:
                    prev[adj] = curr
                    frontier.replace(adj, new_cost)

initial_state = 'Addis Ababa'
goal_state = "Moyale"

ret = AStar(initial_state, goal_state, state_space_graph_et,  True, True)
print("path:", ret[0])
print("cost", ret[1])
