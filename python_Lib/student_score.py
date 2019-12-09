
## class 정의
class Student:
    # class variable 공통변수 : 현재는 실습파일에는 공통변수가 없기때문에 잡을 필요 없음
    
    # 생성자(constructor)
    def __init__ (self,n,k,e,m):
        self.sName = n
        self.sKor = int(k)
        self.sEng = int(e)
        self.sMath = int(m)
        self.sAvg = self.calcul_avg()  #아예 평균 변수명을 만들어서 계산해서 넣어주기 
    
    # method
    def calcul_avg(self) : 
        return (self.sKor+self.sEng+self.sMath)/3 
        
    def print_student(self):
        print("학생의 이름은:{},평균은:{:.2f}".format(self.sName,self.sAvg)) # {:.2f} 소숫점 둘째 자리까지 출력해