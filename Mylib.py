class mylib:
    #%% Definición de la función data quality report
    def dqr(data):
        import pandas as pd
        #%% Lista de variables de la base de datos
        columns = pd.DataFrame(list(data.columns.values),
                               columns=['Nombres'],
                               index=list(data.columns.values))
        
        #%% Lista de tipos de datos 
        data_types = pd.DataFrame(data.dtypes,columns=['Data_Types'])
        
        #%% Lista de datos perdidos 
        missing_values = pd.DataFrame(data.isnull().sum(),
                                      columns=['Missing_Values'])
        #%% Lista de los datos presentes
        present_values = pd.DataFrame(data.count(),
                                      columns=['Present_Values'])
        #%% Lista de valores únicos 
        unique_values = pd.DataFrame(columns=['Unique_Values'])
        for col in list(data.columns.values):
            unique_values.loc[col] = [data[col].nunique()]
        
        #%% Lista de valores mínimos 
        min_values = pd.DataFrame(columns=['Min'])
        for col in list(data.columns.values):
            try:
                min_values.loc[col] = [data[col].min()]
            except: 
                pass
            
        #%% Lista de valores máximos
        max_values = pd.DataFrame(columns=['Max'])
        for col in list(data.columns.values):
            try:
                max_values.loc[col] = [data[col].max()]
            except: 
                pass
        
        #%% Juntar todas las tablas 
        return columns.join(data_types).join(missing_values).join(present_values).join(unique_values).join(min_values).join(max_values)
    
    #%% Remover signos de puntuación 
    def remove_punctuation(x):
        import string
        try: 
            x = ''.join(ch for ch in x if ch not in string.punctuation)
        except: 
            pass
        return x 
    
    #%% Remover dígitos
    def remove_digits(x):
        import string
        try: 
            x = ''.join(ch for ch in x if ch not in string.digits)
        except: 
            pass
        return x
    
    #%% Remover espacios en blanco 
    def remove_whitespace(x):
        try: 
            x = ''.join(x.split())
        except:
            pass
        return x
    
    #%% Reemplazar texto 
    def replace_text(x,to_replace,replacement):
        try: 
            x = x.replace(to_replace,replacement)
        except:
            pass
        return x 
    
    #%% Convertir a mayúsculas 
    def uppercase_text(x):
        try: 
            x = x.upper()
        except:
            pass
        return x 
    
    #%% Convertir a minusculas
    def lower_text(x):
        try: 
            x = x.lower()
        except:
            pass
        return x
    
    
    #%% Dejar solo dígitos
    def digits(x):
        import string
        try: 
            x = ''.join(ch for ch in x if ch in string.digits)
        except: 
            pass
        return x
    
    #%% Nueva funcion de missing
    def missing_10(x):
        try: 
            x = str(x)
            if (len(x)!=10): 
                x = 'missing'
        except:
            pass
        return x 
    
    #%%Segunda funcion de missing
    def missing_6(x):
        try: 
            x = str(x)
            if (len(x)!=6): 
                x = 'missing'
        except:
            pass
        return x     
    #%% Quitar muchos espacios
    def add_whitespace(x):
        try: 
            x = ' '.join(x.split())
        except:
            pass
        return x

    