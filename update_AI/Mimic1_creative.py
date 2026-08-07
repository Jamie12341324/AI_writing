import random
# import hard_coded_training_data_maker
info="12345678"
# LW maybe try ignoring records that don't involve at least one example of the
# move set which is the longest or the number of moves gone through to get to the
# current move which is the largest
# LS maybe try a similar thing to LW but with the option that is the farest away
class Records:
    def __init__(self):
        self.test_A=[]
        self.answer_A=[]
        self.marks=0
        self.cycles=50
        self.sL2=0
        self.sL=0
        self.sequence_A=[]
        self.use=True
        self.data_group_num_A=[]
        self.data_group_num_A2=[]
        self.data_group_num_A3=[]
    def new_data(self,info,data_group_num):
        c=0
        L1=len(info)-1
        while c<L1:
            if c>=len(self.test_A):
                self.test_A.append([])
                self.answer_A.append([])
                self.data_group_num_A.append([])
            self.test_A[c].append(info[L1-c-1:L1])
            self.answer_A[c].append(info[L1])
            self.data_group_num_A[c].append(data_group_num)
            c=c+1
        #print("self.test_A",self.test_A)
        #print("self.answer_A",self.answer_A)
    def respond(self,info):
        c2=0
        c3=0
        L2=len(self.test_A)
        if self.use==True:
            L2=L2-self.sL2
        self.sL2=L2
        L3=len(info)
        d=L2-L3
        c5=0
        if d<=-1:
            c5=(-d)-1
            d=0
        #print("d",d)
        b=False
        act=True
        #print("L2",L2)
        while c2<L2:
            if -(c2+1+d)>-len(self.test_A):
                L4=len(self.test_A[-(c2+1+d)])
            else:
                L4=0
            #print("L4",L4)
            #c5=0 # this line used to set c5 to 1
            while c3<L4:
                #if c2-L3==-1:
                    #c5=0
                if info=="2=1+1+1" and c3==3:
                    pass
                if L3>L2 and self.use==False and act==True and (c2+c5+2)==L3:
                    c5=c5+1
                    act=False
                last_group=False
                for group in self.data_group_num_A3:
                    if self.data_group_num_A[-(c2+1+d)][c3]==group:
                        last_group=True
                        break
                if info[c2+c5:L3]==self.test_A[-(c2+1+d)][c3] and last_group==False:
                    self.answer=self.answer_A[-(c2+1+d)][c3]
                    self.data_group_num_A2.append(self.data_group_num_A[-(c2+1+d)][c3])
                    b=True
                    #print("self.test_A[-(c2+1+d)][c3]",self.test_A[-(c2+1+d)][c3])
                    #print("self.answer_A[-(c2+1+d)][c3]",self.answer_A[-(c2+1+d)][c3])
                    #print("info[c2:L3]",info[c2:L3])
                    #if self.answer==self.x:
                        #correct=True
                    #else:
                        #correct=False
                    #print("my prediction was",self.answer,"and",correct)
                    break
                c3=c3+1
            c3=0
            if b==True:
                break
            c2=c2+1
        if b==False:
            self.answer=str(random.randint(1,4))
            print("unkown so random")
        #print("answer",self.answer)
        return self.answer
    def transfer_data_group(self):
        self.data_group_num_A3=[]
        print("self.data_group_num_A2",self.data_group_num_A2)
        for group2 in self.data_group_num_A2:
            self.data_group_num_A3.append(group2)
        self.data_group_num_A2=[]
    def check(self,x,answer):
        if answer==x:
            self.correct=True
        else:
            self.correct=False
            self.marks=self.marks+1
        #print("my prediction was",answer,"and",self.correct)
    def central_loop(self):
        info=""
        c4=0
        while c4<self.cycles:
            answer=self.respond(info)
            print("say your number")
            #self.respond(info)
            print("info",info)
            x=input()
            self.check(x,answer)
            info=info+x
            self.new_data(info)
            c4=c4+1
        print("you got",self.marks,"out of",self.cycles)
        percent=(self.marks/self.cycles)*100
        print("that is",percent,"%")
    def central_loop_support(self,info):
        self.new_data(info)
        #info=""
        x=info[len(info)-1]
        answer=self.respond(info[0:len(info)-1])
        self.check(x,answer)
        #info=info+x
        return self.correct
    def test_full_sequence(self,sequence,data_group_num):
        self.sequence_A.append(sequence)
        L=len(sequence)-1
        self.sL=self.sL+L
        c16=0
        self.new_data(sequence[0:1],data_group_num)
        while c16<L:
            answer=self.respond(sequence[0:c16+1])
            self.check(sequence[c16+1],answer)
            if c16<L-1:
                self.new_data(sequence[0:c16+2],data_group_num)
            c16=c16+1
        self.new_data(sequence[0:L+1],data_group_num)
        percent=(((self.sL+1)-self.marks)/(self.sL+1))*100
        print("that is",percent,"%")
    def text_central_loop(self,sequence):
        #self.test_full_sequence(sequence)
        print("self.test_A",self.test_A)
        print("self.answer_A",self.answer_A)
        info=""
        x=input()
        info=info+x
        answer=""
        while answer!=".":
            answer=self.respond(info)
            if answer=="d":
                pass
            if answer==" ":
                self.transfer_data_group()
            info=info+answer
            print("info",info)
        print("info",info)
    def text_central_loop2(self,start):
        #self.test_full_sequence(sequence)
        #print("self.test_A",self.test_A)
        #print("self.answer_A",self.answer_A)
        self.info=start
        #x=input()
        #self.info=self.info+x
        answer=""
        while answer!=".":
            answer=self.respond(self.info)
            if answer=="d":
                pass
            self.info=self.info+answer
            #print("info",self.info)
        #print("info",self.info)
#records=Records()
#number_bonds=hard_coded_training_data_maker.Number_Bonds(10)
#for sequence in number_bonds.bonds:
    #records.test_full_sequence(sequence)
#sequence="where is the house? just over the road. because of gravity. what is an apple. an apple is a fruit. when is lunch? soon. i am jamie"
#sequence="where is the house? just over the road."
###
# add training data maths as each number from 1 to 9 add 1
# then make the AI replace part of the sums with whatever is on the other side of the equals sign then
# do the same thing but with before the equals sign
# this should turn 1+7=8 into 1+1+6=8 then 2+6=8 then retrain the AI on 2+6=8 then the AI should be able to do basic sums
# that are not in its training data and hopefullly other things 
###
# Add a special part to the AI ideas engine that replaces a list of linked words with another list of linked words
# when a word before the list is matched with another and the first list is outputed as info. The word that is matched
# before the list also has to have a connection to the other list.
#records.text_central_loop(sequence)
#records.central_loop()
#records.new_data(info)
#records.respond("4567")
#print(records.central_loop_support('1234567845'))
# records=Records()
#number_bonds=hard_coded_training_data_maker.Number_Bonds(5)
#for sequence in number_bonds.bonds:
    #records.test_full_sequence(sequence)
# shapes=["triangle","square"]
# colors=["green","yellow","red"]
# position=["to the left.","to the right.","by the edge."]
# data_A=hard_coded_training_data_maker.Leaf_Text_Maker(shapes,colors,position)
# r1=random.randint(0,len(data_A.leaf_A2)-1)
# r2=random.randint(0,len(data_A.leaf_A2)-1)
# r3=random.randint(0,len(data_A.leaf_A2)-1)
# records.test_full_sequence(data_A.leaf_A2[r1],4)
# records.test_full_sequence(data_A.leaf_A2[r2],5)
# records.test_full_sequence(data_A.leaf_A2[r3],6)
# records.test_full_sequence(data_A.leaf_A2[0],data_group_num=1)
# records.test_full_sequence(data_A.leaf_A2[6],data_group_num=2)
# records.test_full_sequence(data_A.leaf_A2[5],data_group_num=3)
# records.use=False
# sequence=""
# records.text_central_loop(sequence)
# print("data_A.leaf_A2[0]",data_A.leaf_A2[0])
# print("data_A.leaf_A2[6]",data_A.leaf_A2[6])
# print("data_A.leaf_A2[5]",data_A.leaf_A2[5])
# print("data_A.leaf_A2[r1]",data_A.leaf_A2[r1])
# print("data_A.leaf_A2[r2]",data_A.leaf_A2[r2])
# print("data_A.leaf_A2[r3]",data_A.leaf_A2[r3])