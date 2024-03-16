class Edge:
    def __init__(self, start, end):
        self.start: int = start
        self.end: int = end


class Logic:
    def __init__(self):
        self.vertexes = [None for i in range(1000001)]
        self.edges = []

    def create_vertex(self, num):
        return {
            "num": num,
            "edge_in": [],
            "edge_out": [],
            "edge_in_cnt": 0,
            "edge_out_cnt": 0,
            # 모든 점에 대해서 검사할때는 이미 검사된 점에 속하는지 체크 필요하나, 시작점의 도착점들에 대해서만 검사하면 됨. 문제조건상 해당 도착점들이 곧 그래프개수.
            # "is_cycle_family": False,
        }

    def setup(self, raw_edges):
        # 여러 차례 제출하여 추론한 결과 O(N) 시간 안에 가공 및 판별되어야 함.
        # 그러기 위해서는 객체생성은 100만개 무리있고, None판별 로직 추가 필요
        for raw_edge in raw_edges:
            start, end = raw_edge
            edge = Edge(start, end)
            self.edges.append(edge)
            # 기존에 없던 정점 번호라면 추가 및 각 정점별 인풋 검사
            self.register_start_end_if_not_registered(edge)
        # 아래 주석처리한것과 같이 하면 O(N^2)라서 시간초과로 안됨
        # 각 정점별 인풋 검사
        # for vertex in self.vertexes.values():
        #     self.cnt_vertex_input(vertex)
        #     self.cnt_vertex_output(vertex)

    #
    # def cnt_vertex_input(self, vertex):
    #     for edge in self.edges:
    #         if edge.end == vertex.num:
    #             vertex.edge_in.append(edge)
    #             vertex.edge_in_cnt += 1
    # def cnt_vertex_output(self, vertex):
    #     for edge in self.edges:
    #         if edge.start == vertex.num:
    #             vertex.edge_out.append(edge)
    #             vertex.edge_out_cnt += 1

    def register_start_end_if_not_registered(self, edge):
        if self.vertexes[edge.start] is None:
            self.vertexes[edge.start] = self.create_vertex(edge.start)  # Vertex(edge.start)
        self.vertexes[edge.start]["edge_out"].append(edge)
        self.vertexes[edge.start]["edge_out_cnt"] += 1
        if self.vertexes[edge.end] is None:
            self.vertexes[edge.end] = self.create_vertex(edge.end)  # Vertex(edge.end)
        self.vertexes[edge.end]["edge_in"].append(edge)
        self.vertexes[edge.end]["edge_in_cnt"] += 1

        # 아래 주석처리한것과 같이 하면 O(N^2)라서 시간초과로 안됨. keys()에서 in 연산자로 존재여부 검사시 내부적으로 최악의 경우 O(N) 소요될 수 있음.
        # start_exists = start in self.vertexes.keys()
        # end_exists = end in self.vertexes.keys()
        # for vertex in self.vertexes.values():
        #     if vertex.num == start:
        #         start_exists = True
        #     if vertex.num == end:
        #         end_exists = True
        # if not start_exists:
        #     self.vertexes[str(start)] = Vertex(start)
        # if not end_exists:
        #     self.vertexes[str(end)] = Vertex(end)

    def solve_answer(self):
        appended_vertex_num = 0
        cycle_graph_cnt = 0
        linear_graph_cnt = 0
        eight_shape_graph_cnt = 0
        # 추가된 정점 번호 탐색
        appended_vertex_num = self.find_appended_vertex()
        # 도넛그래프 계수
        cycle_graph_cnt = self.cnt_cycle_graph(self.vertexes[appended_vertex_num])
        # 선형그래프 계수
        linear_graph_cnt = self.cnt_linear_graph()
        # 8자그래프 개수
        eight_shape_graph_cnt = self.cnt_eight_shape_graph()
        return [appended_vertex_num, cycle_graph_cnt, linear_graph_cnt, eight_shape_graph_cnt]

    def check_cycle(self, origin, start_vertex):
        stack = []
        if start_vertex["edge_out_cnt"] == 1:
            current_vertex = start_vertex
            while len(current_vertex["edge_out"]) == 1:
                stack.append(start_vertex)
                if current_vertex["edge_out"][0].end == origin:
                    return True
                current_vertex = self.vertexes[current_vertex["edge_out"][0].end]
        return False

    # 아래와 같이 해도 이론상 되는데, 최대 100만개다보니 재귀함수 사용시 스택오버플로우로 추정되는 런타임 에러 발생.
    # 위와 같이 스택 자료구조로 풀면 깔끔.
    # def check_cycle(self, origin, current_vertex):
    #     if current_vertex["edge_out_cnt"] == 1:
    #         current_vertex["visited"] = True
    #         if current_vertex["edge_out"][0].end == origin:
    #             current_vertex["is_cycle_family"] = True
    #             return True
    #         else:
    #             next_vertex_result = self.check_cycle(origin, self.vertexes[current_vertex["edge_out"][0].end])
    #             if next_vertex_result:
    #                 current_vertex["is_cycle_family"] = True
    #             return next_vertex_result
    #     else:
    #         return False

    def cnt_cycle_graph(self, start_vertex):
        cycle_graph_cnt = 0
        for out_edge in start_vertex["edge_out"]:
            vertex = self.vertexes[out_edge.end]
            if self.check_cycle(vertex["num"], vertex):
                cycle_graph_cnt += 1

            # 기존에 검출한 도넛그래프 소속 정점이 아니면 도넛그래프 존재여부 검사
            # -> 할 필요없음. 시작점의 간선들 도착점들에 대해서만 평가 하면 됨. 나머지 점들은 조사 불필요.
            # if vertex is not None and not vertex["is_cycle_family"]:
            #     if self.check_cycle(vertex["num"], vertex):
            #         cycle_graph_cnt += 1
        return cycle_graph_cnt

    def cnt_linear_graph(self):
        linear_graph_cnt = 0
        for vertex in self.vertexes:
            if vertex is not None and vertex["edge_in_cnt"] > 0 and vertex["edge_out_cnt"] == 0:
                linear_graph_cnt += 1
        return linear_graph_cnt

    def cnt_eight_shape_graph(self):
        eight_shape_graph_cnt = 0
        for vertex in self.vertexes:
            if vertex is not None and vertex["edge_in_cnt"] >= 2 and vertex["edge_out_cnt"] == 2:
                eight_shape_graph_cnt += 1
        return eight_shape_graph_cnt

    def find_appended_vertex(self):
        for vertex in self.vertexes:
            if vertex is not None and vertex["edge_in_cnt"] == 0 and vertex["edge_out_cnt"] > 1:
                return vertex["num"]

    # 생성된 점 확인용 메소드. 채점시에는 최대 100만개에 대해 수행하므로, 과다출력 에러발생하므로 사용하면 안됨.
    # def debug_print(self):
    # for vertex in global_logic.vertexes:
    #     if vertex is not None:
    #         print("정점 번호: {}, 입력: {}개, 출력: {}개, 사이클 여부:{}".format(vertex.num, vertex.edge_in_cnt, vertex.edge_out_cnt, vertex.is_cycle_family))


global_logic = Logic()


def solution(edges):
    global global_logic
    global_logic.setup(edges)
    answer = global_logic.solve_answer()
    return answer
