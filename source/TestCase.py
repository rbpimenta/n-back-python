from typing import List
from xmlrpc.client import Boolean
from enum import Enum

class ResultEnum(Enum):
    ACERTO = 1,
    ERRO = 2

class TestCase:

    def __init__(self, id, nBack, numberOfNotes) -> None:
        self.id = id
        self.nBack = nBack
        self.numberOfNotes = numberOfNotes
        self.notesExecuted = []
        self.result = ResultEnum.ERRO
        self.bpm = 60
        # todo prevent object to be created if isValidTestCase() returns FALSE

    def __str__(self):
        return f"id: {self.id}, nBack is {self.nBack}, numberOfNotes is {self.numberOfNotes}"
    
    id: int
    nBack: int
    numberOfNotes: int
    notesExecuted: List[int]
    bpm: int
    answer: int
    result: ResultEnum

    def execute(self):
        self.randomizeNumbers()
        self.doQuestion()
        self.validateAnswer()

    def validateAnswer(self):
        length = len(self.notesExecuted)

        # Check if n-back note equals to last note
        lastNote: int = self.notesExecuted[length - 1]
        nBackNote: int = self.notesExecuted[length - 1 - self.nBack]

        if (lastNote == nBackNote):
            if (self.answer == 1):
                self.result = ResultEnum.ACERTO
            else:
                self.result = ResultEnum.ERRO
        else:
            if (self.answer == 1):
                self.result = ResultEnum.ERRO
            else:
                self.result = ResultEnum.ACERTO

    def randomizeNumbers(self):
        for i in range(self.numberOfNotes):
            import source.IOUtils as IOUtils
            self.notesExecuted.append(IOUtils.printAndSleep(self.bpm))

    def doQuestion(self):
        while True:
            try:
                import source.ManualInputUtils as ManualInputUtils
                self.answer = ManualInputUtils.doQuestion(self.nBack)
                break
            except ValueError as e:
                print('Opção não encontrada. Tente novamente./n')

    def isValidTestCase(self) -> Boolean:
        if self.numberOfNotes < self.nBack:
            return False
        else:
            return True

    def executeFromFile():
        import source.FileUtils as FileUtils
        p = FileUtils.readFromFile()
        testCases = len(p.testCaseList)
        testCaseList = p.testCaseList

        i = 0
        while i < len(testCaseList):
            t : TestCase = testCaseList[i]
            t.execute()
            i += 1
        
        return testCaseList

    def executeLoop():
        import source.ManualInputUtils
        testCaseList = []
        testCases = source.ManualInputUtils.testCasesInput()
        i = 0
        while i < testCases:
            while True:
                try:
                    t = source.ManualInputUtils.createManualTestCase(i)
                    testCaseList.append(t)
                    t.execute()
                    break
                except Exception as e:
                    print (e)
                    pass

            i += 1
        
        return testCaseList

