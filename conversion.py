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

# Energy

def J_2_eV(varA):
    '''
        Convert joule to electronvolt.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in joule.
            
        returns:
            varB : [double] A value in electronvolt.
            
        example:
            E_eV = J_2_eV(5.0)
    '''
    varB = varA / e
    return varB

def eV_2_J(varA):
    '''
        Convert electronvolt to joule.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in electronvolt.
            
        returns:
            varB : [double] A value in joule.
            
        example:
            E_J = eV_2_J(1.0)
    '''
    varB = varA * e
    return varB

def J_2_K(varA):
    '''
        Convert joule to kelvin using Boltzmann constant.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in joule.
            
        returns:
            varB : [double] A value in kelvin.
            
        example:
            T = J_2_K(5.0)
    '''
    varB = varA / k_B
    return varB

def K_2_J(varA):
    '''
        Convert kelvin to joule using Boltzmann constant.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in kelvin.
            
        returns:
            varB : [double] A value in joule.
            
        example:
            E = K_2_J(5.0)
    '''
    varB = varA * k_B
    return varB

def eV_2_K(varA):
    '''
        Convert electronvolt to kelvin using Boltzmann constant.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in eV.
            
        returns:
            varB : [double] A value in kelvin.
            
        example:
            T = eV_2_K(1.0)
    '''
    varB = eV_2_J(varA) / k_B
    return varB

def K_2_eV(varA):
    '''
        Convert kelvin to electronvolt using Boltzmann constant.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in kelvin.
            
        returns:
            varB : [double] A value in electronvolt.
            
        example:
            T = K_2_eV(23.0)
    '''
    varB = J_2_eV(varA * k_B)
    return varB

# Pressure

def Pa_2_bar(varA):
    '''
        Convert pascal to bar.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in pascal.
            
        returns:
            varB : [double] A value in bar.
            
        example:
            P_bar = Pa_2_bar(12345.6)
    '''
    varB = varA / 1e5
    return varB

def bar_2_Pa(varA):
    '''
        Convert bar to pascal.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in bar.
            
        returns:
            varB : [double] A value in pascal.
            
        example:
            P_Pa = bar_2_Pa(1.0)
    '''
    varB = varA * 1e5
    return varB

def Pa_2_atm(varA):
    '''
        Convert pascal to standard atomsphere.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in pascal.
            
        returns:
            varB : [double] A value in atm.
            
        example:
            P_atm = Pa_2_atm(12345.6)
    '''
    varB = varA / atm
    return varB

def atm_2_Pa(varA):
    '''
        Convert standard atomsphere to pascal.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in atm.
            
        returns:
            varB : [double] A value in pascal.
            
        example:
            P_Pa = atm_2_Pa(1.0)
    '''
    varB = varA * atm
    return varB

def Pa_2_Torr(varA):
    '''
        Convert pascal to torr.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in pascal.
            
        returns:
            varB : [double] A value in torr.
            
        example:
            P_Torr = Pa_2_Torr(12345.6)
    '''
    varB = varA * 760 / atm
    return varB

def Torr_2_Pa(varA):
    '''
        Convert torr to pascal.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in torr.
            
        returns:
            varB : [double] A value in pascal.
            
        example:
            P_Pa = Torr_2_Pa(1.0)
    '''
    varB = varA * atm / 760
    return varB

# Number

def sn(varA, n):
    '''
        Represent number in scientific notation.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A number for conversion.
            n : [int] A number to indicate the decimal number.
            
        returns:
            varB : [double] The representation in scientific notation.
            
        example:
            sn(314159, 3)
    '''
    STRING = '{:.' + str(n) + 'e}'
    return STRING.format(varA)