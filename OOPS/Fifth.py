class Car:
    def __init__(self) -> None:
        self.engine=None

    class Engine:
        def __init__(self,type) -> None:
            self.type=type
            self.isRunning=False

        
        def start(self):
            if not  self.isRunning:
                self.isRunning=True
                print("Engine  started")

            else:
                print("Engine  is  not  installed")

        def stop(self):
            if self.isRunning:
                self.isRunning=False
                print("Engine  is  stopped")

            else:
                print("Engine is not installed")

    
    def start_engine(self):
       if  self.engine:
           self.engine.start()

    def stop_engine(self):
        if self.engine:
            self.engine.stop()

    def installeEngine(self,engine_type):
        self.engine=self.Engine(engine_type)
        print(engine_type," Engine is installed")


c=Car()
c.installeEngine("V12")
c.start_engine()
c.stop_engine()


