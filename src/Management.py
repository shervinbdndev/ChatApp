try:
    from tkinter.font import BOLD
    from dataclasses import dataclass
    from tkinter.constants import (CENTER , NORMAL , BOTH , GROOVE , LEFT)
    
except ModuleNotFoundError.__doc__ as mnfe:
    raise AttributeError(args='Cannot Import Materials') from None

finally:
    ...
    
    
    
    
    
@dataclass
class Materials:
    
    @dataclass
    class Fonts:
        pop: str = 'Poplar Std'
        
    @dataclass
    class State:
        normal: str = NORMAL
        
    @dataclass
    class Cursors:
        hand: str = 'hand2'
    
    @dataclass
    class FontWeight:
        bold: str = BOLD
    
    @dataclass
    class Reliefs:
        groove: str = GROOVE
    
    @dataclass
    class Themes:
        DARK: str = 'dark'
        LIGHT: str = 'light'
    
    @dataclass
    class Colors:
        dark: str = '#1C1C1C'
        white: str = '#ffffff'
        black: str = '#000000'
        medPurple: str = '#5964e5'
        
    @dataclass
    class Alignments:
        both: str = BOTH
        left: str = LEFT
        center: str = CENTER