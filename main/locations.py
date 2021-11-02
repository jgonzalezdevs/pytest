"""
 
     _  _     _                    _   _                ____ _               
   _| || |_  | |    ___   ___ __ _| |_(_) ___  _ __    / ___| | __ _ ___ ___ 
  |_  ..  _| | |   / _ \ / __/ _` | __| |/ _ \| '_ \  | |   | |/ _` / __/ __|
  |_      _| | |__| (_) | (_| (_| | |_| | (_) | | | | | |___| | (_| \__ \__ \
    |_||_|   |_____\___/ \___\__,_|\__|_|\___/|_| |_|  \____|_|\__,_|___/___/
                                                                             
 
"""

class TestLocations():
    def __init__(self):
        self.__start_point = ''
        self.__end_point = ''
        self.__transport_method = ''
        self.__walking_time = 55
        self.__public_transport_time = 35
        self.__car_time = 20
    """
 
         _  _     ____                              
       _| || |_  |  _ \ _   _ _ __  _ __   ___ _ __ 
      |_  ..  _| | |_) | | | | '_ \| '_ \ / _ \ '__|
      |_      _| |  _ <| |_| | | | | | | |  __/ |   
        |_||_|   |_| \_\\__,_|_| |_|_| |_|\___|_|   
                                                    
 
    """
    def run(self):
        self.__start_point = input('Ingrese el punto de partida: ')
        self.__end_point = input('Ingrese el punto de llegada: ')
        self.__transport_method = input('Ingrese el metodo de transporte: (1. Caminando, 2. Transporte Público y 3. Carro): ')
        self.comparer()
    """
 
         _  _     ____       _       _            
       _| || |_  |  _ \ _ __(_)_ __ | |_ ___ _ __ 
      |_  ..  _| | |_) | '__| | '_ \| __/ _ \ '__|
      |_      _| |  __/| |  | | | | | ||  __/ |   
        |_||_|   |_|   |_|  |_|_| |_|\__\___|_|   
                                                  
 
    """
    def printer(self, time, opt = 1):
        if opt == 1:
            output_string = 'La ruta más rápida {method} desde {start} a {end}, le tomará {time} minutos.'.format(method = self.__transport_method, start = self.__start_point, end = self.__end_point, time = time)
        if opt == 2:
            output_string = 'La ruta más rápida en {method} desde {start} a {end}, le tomará {time} minutos.'.format(method = self.__transport_method, start = self.__start_point, end = self.__end_point, time = time)
        if opt == 3:
            output_string = 'La ruta más rápida en {method} desde {start} a {end}, le tomará {time} minutos.'.format(method = self.__transport_method, start = self.__start_point, end = self.__end_point, time = time)
        print(output_string)
    """
 
         _  _      ____                                          
       _| || |_   / ___|___  _ __ ___  _ __   __ _ _ __ ___ _ __ 
      |_  ..  _| | |   / _ \| '_ ` _ \| '_ \ / _` | '__/ _ \ '__|
      |_      _| | |__| (_) | | | | | | |_) | (_| | | |  __/ |   
        |_||_|    \____\___/|_| |_| |_| .__/ \__,_|_|  \___|_|   
                                      |_|                        
 
    """
    def comparer(self):
        if ('caminando') in self.__transport_method.lower():
            self.printer(self.__walking_time, 1)
        elif 'transporte público' in self.__transport_method.lower() or 'transporte publico' in self.__transport_method.lower():
            self.printer(self.__public_transport_time, 2)
        elif ('carro') in self.__transport_method.lower():
            self.printer(self.__car_time, 3)
        else:
            print('Existe algun dato erroneo. por favor, verifique el ingreso de datos e intentelo nuevamente.')
