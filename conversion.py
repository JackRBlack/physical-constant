# Temperature

def C_2_F(varA):
    '''
        Convert Celsius to Fahrenheit.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in Celsius.
            
        returns:
            varB : [double] A value in Fahrenheit.
            
        example:
            T_F = C_2_F(26.5)
    '''
    
    if varA < -273.15:
        raise ValueError('Temperature cannot be lower than -273.15 °C (0 K)!')
    varB = varA * 1.8 + 32
    return varB

def F_2_C(varA):
    '''
        Convert Fahrenheit to Celsius.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in Fahrenheit.
            
        returns:
            varB : [double] A value in Celsius.
            
        example:
            T_C = F_2_C(40.5)
    '''
    
    if varA < -459.67:
        raise ValueError('Temperature cannot be lower than -459.67 °F (0 K)!')
    varB = (varA - 32) / 1.8
    return varB

def C_2_K(varA):
    '''
        Convert Celsius to Kelvin.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in Celsius.
            
        returns:
            varB : [double] A value in Kelvin.
            
        example:
            T_K = C_2_K(26.5)
    '''
    if varA < -273.15:
        raise ValueError('Temperature cannot be lower than -273.15 °C (0 K)!')
    varB = varA + 273.15
    return varB

def K_2_C(varA):
    '''
        Convert Kelvin to Celsius.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in Kelvin.
            
        returns:
            varB : [double] A value in Celsius.
            
        example:
            T_C = K_2_C(0)
    '''
    if varA < 0:
        raise ValueError('Temperature cannot be lower than 0 K!')
    varB = varA - 273.15
    return varB

def F_2_K(varA):
    '''
        Convert Fahrenheit to Kelvin.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in Fahrenheit.
            
        returns:
            varB : [double] A value in Kelvin.
            
        example:
            T_K = F_2_K(40.5)
    '''
    
    if varA < -459.67:
        raise ValueError('Temperature cannot be lower than -459.67 °F (0 K)!')
    varB = (varA - 32) / 1.8 + 273.15
    return varB

def K_2_F(varA):
    '''
        Convert Kelvin to Fahrenheit.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in Kelvin.
            
        returns:
            varB : [double] A value in Fahrenheit.
            
        example:
            T_F = K_2_F(0)
    '''
    if varA < 0:
        raise ValueError('Temperature cannot be lower than 0 K!')
    varB = (varA - 273.15) * 1.8 + 32
    return varB