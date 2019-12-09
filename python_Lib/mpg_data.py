
## class 정의
class Mpg:
    
    def __init__(self,manufacturer,model,displ,year,cyl,trans,drv,cty,hwy,fl,cl):
        self.m_manu= manufacturer
        self.m_model=model
        self.m_displ=float(displ)
        self.m_year=int(year)
        self.m_cyl=int(cyl)
        self.m_trans=trans
        self.m_drv=drv
        self.m_cty=int(cty)
        self.m_hwy=int(hwy)
        self.m_fl=fl
        self.m_class=cl
        self.m_avg=self.avgmpg()
        
    
    
    
    
    def avgmpg(self):
        return (self.m_cty+self.m_hwy)/2
    
    def printd(self):
        print(self.m_manu,self.m_model,self.m_displ,self.m_year,self.m_cyl,self.m_trans,self.m_drv,self.m_cty,self.m_hwy,self.m_fl,self.m_class)
        
    #method
#    # 1. displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.
#     def num1(self):
#         be4=[]
#         up5=[]
#         if self.m_displ<=4:
#             be4.append(self.m_hwy)
            
#         elif self.m_displ>=5:
#             up5.append(self.m_hwy)
            
#         b4=sum(be4)/len(be4)
#         u5=sum(up5)/len(up5)
        
#         if b4>u5
        
        
        