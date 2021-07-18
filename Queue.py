# 클래스와 함수 선언
class Node():
    def __init__ (self):
        self.data = None # 노드의 데이터 값
        self.link = None # 뒤의 노드를 가르킴
        
class Queue:

    def __init__(self): # 생성자
        self.front = None  # 큐의 삭제할 노드(맨 앞노드)
        self.rear = None # 큐의 가장 나중에 추가된 노드(마지막 노드)
        

    # 삽입
    def enQueue(self, new_data):
        
        newNode = Node()  #노드 생성
        newNode.data = new_data  # 노드 데이터입력
        
        # 첫 번째 노드일 때
        if self.front == None:
            self.front = newNode #front가 새노드를 가르킴
            self.rear = newNode  # rear가 새노드를 가르킴
            
        else: 
            self.rear.link = newNode  # 현재 rear의 값이 새 노드를 가르킴
            self.rear = newNode  # rear가 새노드를 가르킴
        

    # 삭제
    def deQueue(self):

       # 큐가 비어있을 때
        if self.front == None:
            print("큐가 비어있습니다!!")
            return
        
        else:
            delete_node = self.front # front값을 삭제 노드로 지정
            self.front = self.front.link # 두번째 노드를 첫 노드로 
            if(self.front == None): # 마지막 노드를 삭제한 경우
                self.rear = None
        
        print("%s를 삭제했습니다 \n" % delete_node.data)
        del(delete_node)
        
    
    # 출력        
    def printQueue(self):

        if self.front == None: #큐가 비었을 때
            print("큐가 비어있습니다!!")
            return
        
        
        current = self.front # 큐의 첫 노드를 current에 줌
        while current != None: # current가 마지막 노드일 때 까지
            print(current.data, end = ' ')
            print(" ")
            current = current.link # 출력후 다음 노드값 출력을 위해
                                       # current값을 다음 노드값을 줌
        print()    
    


## 메인 코드 부분 ##
if __name__ == "__main__" :
    queue = Queue()
    
    while True:
        print("==================================================\n")
        print(" [0: 종료] [1: enQueue] [2: deQueue] [3: 출력] \n")
        print("==================================================\n")
        menu = int(input("메뉴 입력: "))

        # 종료
        if menu == 0:
            quit()
            
        # enQueue(삽입)
        elif menu == 1:
            add_data = (input('입력할 자료: '))
            queue.enQueue(add_data)
            queue.printQueue()
            
        # deQueue(삭제)
        elif menu == 2:
            queue.deQueue()
            queue.printQueue()       

        # 출력
        elif menu == 3:
            queue.printQueue()

        # 오류
        else:
            print("[Error]다시 입력!!")
