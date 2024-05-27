
state_space_graph_et = {
    'Asmera': [('Axum', 3), ('Adigrat', 6)],
    'Axum': [('Shire', 2), ('Adwa', 1), ('Asmera', 5)],
    'Adigrat': [('Asmera', 6), ('Adwa', 4),('Mekelle', 7)],
    'Shire': [('Axum', 2),('Debarke', 7),('Humera', 8)],
    'Adwa': [('Axum', 1),('Adigrat', 4),('Mekelle', 7)],
    'Mekelle': [('Adwa', 7),('Adigrat', 4),('Sekota', 9),('Alamata', 5)],
    'Debarke':[('Shire', 7),('Gondar',4)],
    'Humera':[('Shire', 8),('Gondar', 9),('Kartum', 21)],
    'Sekota':[('Mekelle',9 ), ('Alamata', 6),('Lalibela',6)],
    'Alamata':[('Mekelle', 5),('Sekota',6),('Woldia',3),('Samara',11)],
    'Gondar': [('Debarke', 4),('Humera',9),('Azezo',1),('Metema',7)],
    'Kartum': [('Humera',21),('Metema',19)],
    'Lalibela':[('Sekota', 6),('Woldia', 7),('Debre_Tabor', 8)],
    'Woldia': [('Alamata', 3),('Lalibela', 7),('Dessie', 6),('Samara', 8)],
    'Samara':[('Alamata',11),('Fanti_Rasu',7),('Woldia',8),('Gabi_Rasu',9)],
    'Azezo':[('Gondar',1),('Metema',7),('Bahir_Dar',7)],
    'Metema':[('Gondar', 7),('Azezo', 7),('Kartum', 19)],
    'Debre_Tabor':[('Bahir_Dar', 4), ('Lalibela',8)],
    'Dessie': [('Woldia', 6),('Kemise',4)],
    'Fanti_Rasu': [('Samara',7), ('Kilbet_Rasu',6)],
    'Gabi_Rasu': [('Samara', 9),('Awash',5)],
    'Bahir_Dar': [('Azezo', 7),('Debre_Tabor',4),('Injibara',4),('Finote_Selam',6),('Metekel',11)],
    'Kemise': [('Dessie', 4),('Debre_Sina',6)],
    'Kilbet_Rasu': [('Fanti_Rasu', 6)],
    'Awash': [('Chiro', 4),('Gabi_Rasu',5),('Matahara', 1)],
    'Debre_Sina': [('Kemise', 6),('Debre_Markos',17),('Debre_Birhan',2)],
    'Chiro':[('Awash',4), ('Dire_Dawa',8)],
    'Matahara':[('Awash',1),('Adama',3)],
    'Debre_Markos':[('Debre_Sina',17),('Finote_Selam',3)],
    'Injibara': [('Finote_Selam',2),('Bahir_Dar',4)],
    'Finote_Selam': [('Debre_Markos',3),('Injibara',2),('Bahir_Dar',6)],
    'Metekel':[('Bahir_Dar',11)],
    'Debre_Birhan':[('Debre_Sina',2),('Addis_Abeba',5)],
    'Dire_Dawa': [('Chiro',8),('Harar',4)],
    'Adama': [('Matahara',3),('Addis_Abeba',3),('Batu',4),('Assella',4)],
    'Assosa':[('Dembi_Dollo',12)],
    'Addis_Abeba':[('Debre_Birhan', 2),('Adama',3),('Ambo',5)],
    'Harar':[('Dire_Dawa',4),('Babile',2)],
    'Batu': [('Buta_Jirra',2),('Adama',4),('Shashemene',3)],
    'Assella':[('Adama',4),('Assasa',4)],
    'Dembi_Dollo': [('Assosa',12),('Gimbi',6),('Gambella',4)],
    'Ambo':[('Addis_Abeba',5),('Nekemete',9),('Wolkite',6)],
    'Babile':[('Harar',2),('Jigjiga',3),('Goba',28)],
    'Buta_Jirra':[('Batu',2),('Worabe',2)],
    'Shashemene': [('Batu',3),('Hossana',7),('Dodolla',3),('Hawassa',1)],
    'Assasa':[('Assella',4),('Dodolla',1)],
    'Gimbi':[('Dembi_Dollo',6),('Nekemete',4)],
    'Gambella': [('Dembi_Dollo',4),('Gore',5)],
    'Nekemete': [('Gimbi',4),('Ambo',9),('Bedelle',1)],
    'Wolkite':[('Ambo',6),('Worabe',5),('Jimma',8)],
    'Jigjiga':[('Babile',3),('Dega_Habur',5)],
    'Worabe': [('Buta_Jirra',2),('Wolkite',5),('Hossana',2)],
    'Hossana':[('Shashemene',7),('Worabe',2), ('Wolaita_Sodo',4)],
    'Dodolla':[('Assasa',1),('Bale',13),('Shashemene',3)],
    'Hawassa':[('Shashemene',1),('Dilla',3)],
    'Gore':[('Gambella',5),('Tepi',9),('Bedelle',6)],
    'Bedelle': [('Nekemete',1),('Jimma',7),('Gore',6)],
    'Jimma':[('Wolkite',8),('Bedelle',7),('Bonga',4)],
    'Dega_Habur':[('Jigjiga',5),('Kebri_Dehar',6)],
    'Wolaita_Sodo': [('Hossana',4),('Dawro',6),('Arba_Minch',100)],
    'Bale':[('Dodolla',13),('Goba',18),('Sof_Oumer',23),('Liben',11)],
    'Dilla': [('Hawassa',3),('Bule_Hora',4)],
    'Tepi':[('Gore',10),('Mezan_Teferi',10),('Bonga',10)],
    'Bonga':[('Jimma',4),('Tepi',8),('Mezan_Teferi',4),('Dawro',10)],
    'Goba':[('Bale',18),('Sof_Oumer',6),('Babile',28)],
    'Kebri_Dehar':[('Dega_Habur',6),('Werder',6),('Gode',5)],
    'Dawro':[('Bonga',10),('Wolaita_Sodo',6)],
    'Arba_Minch':[('Wolaita_Sodo',100),('Basketo',10),('Konso',4)],
    'Sof_Oumer':[('Gode',23),('Goba',6),('Bale',23)],
    'Liben':[('Bale',11)],
    'Bule_Hora':[('Dilla',4),('Yabello',3)],
    'Mezan_Teferi':[('Tepi',4),('Bonga',4)],
    'Werder': [('Kebri_Dehar',6)],
    'Basketo':[('Arba_Minch',10),('Bench_Maji',5)],
    'Konso': [('Arba_Minch',4),('Yabello',4)],
    'Yabello':[('Bule_Hora',3),('Konso',3),('Moyale',6)],
    'Bench_Maji':[('Basketo',5),('Juba',22)],
    'Moyale':[('Yabello',6),('Narobi',22)],
    'Juba':[('Bench_Maji',22)],
    'Narobi':[('Moyale',22)],
    'Gode':[('Kebri_Dehar',5),('Dollo',17),('Mokadisho',22)],
    'Dollo':[('Gode',17)],
    'Mokadisho':[('Gode',22)]
}
import heapq
class Searcher:

    def __init__(self, state_space_graph, initial_state, goal_state):
        self.graph = state_space_graph
        self.initial_state = initial_state
        self.goal_state = goal_state

    def search(self, strategy):
        """
        Performs a search using the specified strategy.
        :param strategy: "bfs" or "dfs"
        :return: The path from the initial state to the goal state,
                or None if the goal state is not found.
        """
        if strategy == "bfs":
            return self.breadth_first_search()
        elif strategy == "dfs":
            return self.depth_first_search()
        else:
            raise ValueError("Invalid search strategy:", strategy)
    def uniform_cost_search(self, initial_state, goal_state):
        """
        Performs a Uniform Cost Search (UCS) on the state space graph.
        :param initial_state: The state where the search begins.
        :param goal_state: The state where the search ends.
        :return: The path from the initial state to the goal state and its cost,
                or None if the goal state is not found.
        """
        visited = set()
        queue = [(0, initial_state, [])]  # (cost, state, path)

        while queue:
            cost, state, path = heapq.heappop(queue)
            visited.add(state)

            if state == goal_state:
                return path + [state], cost

            for neighbor, neighbor_cost in self.graph[state]:
                if neighbor not in visited:
                    total_cost = cost + neighbor_cost
                    heapq.heappush(queue, (total_cost, neighbor, path + [state]))

        return None
    def greedy_tsp(self, goal_states):
        """
        Performs a Greedy Traveling Salesman Problem (TSP) search on the state space graph.
        :param goal_states: A list of goal states to visit.
        :return: The path from the initial state to each goal state,
                or None if a goal state is not found.
        """
        path = [self.initial_state]
        total_distance = 0
        while goal_states:
            current_city = path[-1]
            print(self.find_shortest_path(current_city, goal_states))
            print('\n')
            next_city, next_distance ,_ = self.find_shortest_path(current_city, goal_states)
            path.append(next_city)
            total_distance += next_distance
            goal_states.remove(next_city)
        return path, total_distance

    def find_shortest_path(self, current_city, unvisited):
        """
        Finds the shortest path from the current city to an unvisited city.
        :param current_city: The current city.
        :param unvisited: A list of unvisited cities.
        :return: The nearest unvisited city and the distance to it.
        """
        shortest_city = None
        shortest_distance = float('inf')
        shortest_path = None
        for city in unvisited:
            path, distance = self.uniform_cost_search(current_city, city)
            if distance < shortest_distance:
                shortest_city = city
                shortest_distance = distance
                shortest_path = path
        return shortest_city, shortest_distance, shortest_path
        
        
initial_state ='Addis_Abeba'
goal_state = 'Lalibela'
# Create a Searcher object
searcher = Searcher(state_space_graph_et, initial_state, goal_state)
path = searcher.uniform_cost_search(initial_state, goal_state)
print("Path:", path)

searcher = Searcher(state_space_graph_et, initial_state, None)

path, distance = searcher.greedy_tsp(["Axum", "Gondar", "Lalibela", "Babile", "Jimma","Sof_Oumer","Bale", "Arba_Minch"])
print("Path:", path)
print("Total distance:", distance)