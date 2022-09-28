class LogMixin:
    
    """staticmethod não precisa de instacia para existir"""
    @staticmethod
    def write(msg):
        with open('log.log','a+') as f:
            f.write(msg)
            f.write('\n')
            
            
    #dfasfda
    def log_info(self, msg):
        self.write(f'INFO: {msg}')
    
    def log_warn(self, msg):
        self.write(f'ERROR: {msg}')