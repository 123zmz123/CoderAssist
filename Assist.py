import re
class Assist:
    def __init__(self):
        pass
    def MainProgress(self):
        while(True):
            opt = self.MainPanel()
            if opt == 1:
                self.RepeatLines()
            elif opt == 2:
                pass



    def MainPanel(self):
        print("Welcome to Program Assist!\n")
        print("Pleas Choose the function\n")
        print("1.  Print Repeat lines")
        print("2.  Quick move files")

        option = int(input("Please input your option\n"))
        return option

    def RepeatLines(self):
        var = []
        pos = []
        lines=input("Input lines you want to repeat! Use $ to represent variable\n")
        lines=lines.replace("$","%d")
        init = int(input("Input Var Init"))
        count = int(input("Input Var Count"))
        step = int(input("Input Var Step"))
        self._repeat(lines,init,step,count)
    def _repeat(self,line,init,step,count):
        for i in range(init,count,step):
            print(line%(i))
    def Generate_Code(self):
        pass

    def readFile(self):
        # XXX_define 是对于变量基本类型的定义，随后某一个变量的具体值会被写为 基本定义值+序列号的形式
        st_define = 100  # define the type of static item!
        blk_define = 200  # define the type of block item!
        variable_define = 300  # define the type of variable item

        blk_begin = []  # each block begin and end position
        blk_end = []  # each block begin and end position
        blocks = []     # store each blocks content

        static = []  # store static
        variable = []  # store variable
        run_sequence = []  # store the  sequence that we defined
        f = open("cof.dd")

        index = 0
        container = f.readlines()

        def  transToCode():     # translate our definition to real code
            l = []
            i = 0
            code = ""
            for item in run_sequence:
                if item>variable_define:
                    pos=item - variable_define-1
                    b = variable[pos][0]
                    e = variable[pos][1]*variable[pos][2]+variable[pos][0]
                    s = variable[pos][2]
                    l.append([iter for iter in range(b,e,s)])
                    code += "{"+str(i)+"}"
                    i += 1
                    continue
                if item > blk_define:
                    l.append([iter for iter in blocks [item-blk_define -1]])
                    code += "{"+str(i)+"}"
                    i += 1
                    continue
                if item > st_define:
                    code += static[item-st_define-1]
                    continue

            for i in range(len(l[0])):
                l1 = [str(item[i]) for item in l]
                print(code.format(*l1))




        #此函数是把属于Block域的数据提取出来
        def getBlock(container):
            for b, e in zip(blk_begin,blk_end):
                blocks.append([item.strip('\n') for item in container[b:e]])#此处是去除每个block中item的\n 也就是换行符
            print(blocks)
        def getStatic():
            for item in static:
                print(item)
        def getVariables():
            for item in variable:
                print(item)
        def AssignExcuteSequence(run):
            for item in run:
                if re.match("st.+",item):
                    run_sequence .append(st_define +int(item.strip("st")))
                elif re .match("blk.+",item):
                    run_sequence .append(blk_define +int(item.strip("blk")))
                elif re.match("var.+",item):
                    run_sequence .append(variable_define+int(item.strip("var")))
                else:
                    pass



        def checkVariables(): # 检查几个变量是否满足条件
            check_pos_2=[] #此列表是为了存储 在第二个位置也就是循环次数，最终判定变量的循环次数是否相等
            for item in variable:#判断变量一行是否是三个数
                if len(item)!=3:
                    print("每个变量信息应该是三个数")
                    return False
                check_pos_2.append(item[1])#把每个变量的循环次数单独提取出来
            if len(set(check_pos_2))==1:#判断所有的变量循环次数是否都相等，如果不相等则报错
                return True
            else:
                print("变量循环次数不同")
            return False

        def assignCmd(item,index): #根据所得到的内容来分配指令
            if re.match("blk*",item): #如果匹配到block开头
                blk_begin.append(index+1)
            elif re.match("}",item): # 如果匹配到block结尾
                blk_end.append(index)
            elif re.match("st.+=",item): #如果匹配到常量
                s = re.findall("=.+", item)
                static.append(s[0][1:])
            elif re.match("var.+=",item):#如果匹配到变量
                s=re.findall("=.+",item)
                t=[int(x) for x in s[0][1:].split(',')] #此处把List中的字符串转换为int变量
                variable.append(t)
            elif re.match("run:",item):#如果匹配到 运算公式
                run=re.findall(":.+",item)
                run=run[0][1:].split("->")
                AssignExcuteSequence(run)
            else:
                pass
        for item in container:
            assignCmd(item,index)
            index+=1
        if blk_begin != [] and blk_end != []:
            getBlock(container)
        checkVariables()
        transToCode()







def Repeat(line,init,step,count):
    pass
if __name__ == "__main__":
    a = Assist()
    a.readFile()





