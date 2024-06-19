
import heapq
class TravelingEthiopiaProblem:
    def __init__(self, initial_state, goal_states, graph, heuristic):
        self.initial_state = initial_state
        self.goal_states = goal_states
        self.graph = graph  # graph is a dictionary of cities and their neighbors with travel costs
        self.heuristic = heuristic  # heuristic is a function that estimates cost to goal

    def get_neighbors(self, state):
        return self.graph[state]

    def is_goal(self, state):
        return state in self.goal_states

    def get_cost(self, from_state, to_state):
        return self.graph[from_state][to_state]
		
class AStarSearch:
    def __init__(self, problem):
        self.problem = problem

    def search(self):
        frontier = []
        heapq.heappush(frontier, (0, self.problem.initial_state))
        came_from = {self.problem.initial_state: None}
        cost_so_far = {self.problem.initial_state: 0}

        while frontier:
            _, current = heapq.heappop(frontier)

            if self.problem.is_goal(current):
                return self.reconstruct_path(came_from, current)

            for neighbor, cost in self.problem.get_neighbors(current).items():
                new_cost = cost_so_far[current] + cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self.problem.heuristic(neighbor)
                    heapq.heappush(frontier, (priority, neighbor))
                    came_from[neighbor] = current

        return None

    def reconstruct_path(self, came_from, current):
        path = []
        while current is not None:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path

class GreedyBestFirstSearch:
    def __init__(self, problem):
        self.problem = problem

    def search(self):
        frontier = []
        heapq.heappush(frontier, (self.problem.heuristic(self.problem.initial_state), self.problem.initial_state))
        came_from = {self.problem.initial_state: None}

        while frontier:
            _, current = heapq.heappop(frontier)

            if self.problem.is_goal(current):
                return self.reconstruct_path(came_from, current)

            for neighbor, _ in self.problem.get_neighbors(current).items():
                if neighbor not in came_from:
                    priority = self.problem.heuristic(neighbor)
                    heapq.heappush(frontier, (priority, neighbor))
                    came_from[neighbor] = current

        return None

    def reconstruct_path(self, came_from, current):
        path = []
        while current is not None:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path

class SearchPlatform:
    def __init__(self, problem, strategy):
        self.problem = problem
        self.strategy = strategy

    def solve(self):
        search_algorithm = self.strategy(self.problem)
        return search_algorithm.search()

# Example usage
if __name__ == "__main__":
    # Define the graph
    graph = {
        'Addis Ababa': {'Adama': 3, 'Ambo': 5, 'Debre Berhan': 5},
        'Adama': {'Matahara': 3, 'Asella': 4, 'Batu': 4, 'Addis Ababa': 3},
        'Ambo': {'Wolkite': 6, 'Addis Ababa': 5, 'Nekemte': 8},
        'Debre Berhan': {'Addis Ababa': 5, 'Debre Sina': 2},
        'Debre Markos': {'Addis Ababa': 13, 'Debre Sina': 17, 'Finote Selam': 3},
        'Matahara': {'Adama': 3, 'Awash': 1},
        'Asella': {'Adama': 4, 'Assasa': 4},
        'Batu': {'Adama': 4, 'Buta Jirra': 2, 'Shashamene': 3},
        'Wolkite': {'Ambo': 6, 'Worabe': 5, 'Jimma': 8, 'Hossana': 5, 'Buta Jirra': 4},
        'Nekemte': {'Ambo': 9, 'Bedelle': 5, 'Gimbi': 4},
        'Debre Sina': {'Debre Berhan': 2, 'Kemise': 7, 'Debre Markos': 17},
        'Finote Selam': {'Debre Markos': 3, 'Bahirdar': 6, 'Injibara': 2},
        'Awash': {'Chiro': 4, 'Gobi Rasu': 5, 'Matahara': 1},
        'Assasa': {'Asella': 4, 'Dodolla': 1},
        'Buta Jirra': {'Batu': 2, 'Wolkite': 4, 'Worabe': 2},
        'Shashamene': {'Batu': 3, 'Dodolla': 3, 'Hawassa': 1, 'Hossana': 7, 'Worabe': 6},
        'Worabe': {'Wolkite': 5, 'Hossana': 2, 'Shashamene': 6, 'Buta Jirra': 2},
        'Jimma': {'Wolkite': 8, 'Bonga': 4, 'Bedelle': 7},
        'Hossana': {'Shashamene': 7, 'Worabe': 2, 'Wolkite': 5, 'Wolaita Sodo': 4},
        'Bedelle': {'Nekemte': 5, 'Gore': 6, 'Jimma': 7},
        'Gimbi': {'Nekemte': 4, 'Dambidollo': 6, 'Assosa': 8},
        'Kemise': {'Debre Sina': 6, 'Dessie': 4},
        'Bahirdar': {'Finote Selam': 6, 'Injibara': 4, 'Metekel': 11, 'Azezo': 7, 'Debre Tabor': 4},
        'Injibara': {'Bahirdar': 4, 'Finote Selam': 2},
        'Chiro': {'Awash': 4, 'Dire Dawa': 8},
        'Gobi Rasu': {'Awash': 5, 'Samara': 10},
        'Dodolla': {'Assasa': 1, 'Shashamene': 3, 'Robe': 13},
        'Hawassa': {'Shashamene': 1, 'Dilla': 3},
        'Bonga': {'Jimma': 4, 'Dawro': 10, 'Tepi': 8, 'Mizan Teferi': 4},
        'Wolaita Sodo': {'Arba Minchi': 4, 'Dawro': 6, 'Hossana': 4},
        'Gore': {'Tepi': 9, 'Gambella': 5, 'Bedelle': 6},
        'Dambidollo': {'Gimbi': 6, 'Assosa': 12, 'Gambella': 4},
        'Assosa': {'Gimbi': 8, 'Dambidollo': 12},
        'Dessie': {'Kemise': 4, 'Woldia': 6},
        'Metekel': {'Bahirdar': 11},
        'Azezo': {'Gondar': 1, 'Bahirdar': 7, 'Metema': 7},
        'Debre Tabor': {'Lalibella': 8, 'Gondar': 6, 'Bahirdar': 4},
        'Dire Dawa': {'Chiro': 8, 'Harar': 4},
        'Samara': {'Gobi Rasu': 10, 'Fanti Rasu': 7, 'Alamata': 11, 'Woldia': 8},
        'Robe': {'Liben': 11, 'Dodolla': 13, 'Goba': 18, 'Sof Oumer': 23},
        'Dilla': {'Hawassa': 3, 'Bulehora': 4},
        'Dawro': {'Bonga': 10, 'Wolaita Sodo': 6},
        'Tepi': {'Gore': 9, 'Bonga': 8, 'Mizan Teferi': 4},
        'Mizan Teferi': {'Tepi': 4, 'Bonga': 4},
        'Gambella': {'Gore': 5, 'Dambidollo': 4},
        'Arba Minchi': {'Wolaita Sodo': 5, 'Konso': 4, 'Basketo': 10},
        'Woldia': {'Dessie': 6, 'Lalibella': 7, 'Samara': 8, 'Alamata': 3},
        'Gondar': {'Azezo': 1, 'Humera': 9, 'Metema': 7, 'Debarke': 4, 'Debre Tabor': 6},
        'Metema': {'Azezo': 7, 'Gondar': 7},
        'Lalibella': {'Woldia': 7, 'Debre Tabor': 8, 'Sekota': 6},
        'Harar': {'Dire Dawa': 4, 'Babile': 2},
        'Fanti Rasu': {'Samara': 7, 'Kilbet Rasu': 6},
        'Alamata': {'Samara': 11, 'Woldia': 3, 'Mekelle': 5, 'Sekota': 6},
        'Liben': {'Robe': 11},
        'Goba': {'Robe': 18, 'Sof Oumer': 6, 'Babile': 28},
        'Sof Oumer': {'Goba': 6, 'Robe': 23, 'Gode': 23},
        'Bulehora': {'Dilla': 4, 'Yabello': 3},
        'Konso': {'Arba Minchi': 4, 'Yabello': 3},
        'Basketo': {'Arba Minchi': 10, 'Bench Maji': 5},
        'Humera': {'Shire': 8, 'Gondar': 9},
        'Debarke': {'Gondar': 4, 'Shire': 7},
        'Sekota': {'Alamata': 6, 'Mekelle': 9, 'Lalibella': 6},
        'Babile': {'Harar': 2, 'Jigjiga': 3, 'Goba': 28},
        'Kilbet Rasu': {'Fanti Rasu': 6},
        'Mekelle': {'Alamata': 5, 'Adigrat': 4, 'Adwa': 7, 'Sekota': 9},
        'Gode': {'Dollo': 17, 'Kebri Dehar': 5, 'Sof Oumer': 23},
        'Yabello': {'Bulehora': 3, 'Konso': 3, 'Moyale': 6},
        'Bench Maji': {'Basketo': 5},
        'Shire': {'Axum': 2, 'Humera': 8, 'Debarke': 7},
        'Jigjiga': {'Babile': 3, 'Dega Habur': 5},
        'Adigrat': {'Mekelle': 4, 'Adwa': 4},
        'Adwa': {'Mekelle': 7, 'Axum': 1, 'Adigrat': 4},
        'Dollo': {'Gode': 17, 'Moyale': 18},
        'Kebri Dehar': {'Gode': 5, 'Dega Habur': 6, 'Werdez': 6},
        'Moyale': {'Dollo': 18, 'Liben': 11, 'Yabello': 6},
        'Axum': {'Shire': 2, 'Adwa': 1},
        'Dega Habur': {'Jigjiga': 5, 'Kebri Dehar': 6},
        'Werdez': {'Kebri Dehar': 6}
    }

    # Define heuristic function (example heuristic)
    def heuristic(city):
        return 0  # This can be a more sophisticated heuristic

    # Create a TravelingEthiopiaProblem instance
    problem = TravelingEthiopiaProblem(initial_state='Addis Ababa', goal_states={'Moyale'}, graph=graph, heuristic=heuristic)

    # Create a SearchPlatform instance with A* Search
    search_platform = SearchPlatform(problem, AStarSearch)
    solution = search_platform.solve()
    print("A* Search Solution:", solution)

    # Create a SearchPlatform instance with Greedy Best-First Search
    search_platform = SearchPlatform(problem, GreedyBestFirstSearch)
    solution = search_platform.solve()
    print("Greedy Best-First Search Solution:", solution)
