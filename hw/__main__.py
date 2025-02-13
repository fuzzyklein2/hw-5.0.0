from .startup import *
from .program import Program

if __name__ == '__main__':
    print(PROGRAM)
    log.info(f'Executing {PROGRAM} ...')
    
    p = Program()
    
    log.info(f'Execution complete.')
