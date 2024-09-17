import sd.I2CSensorConfig as SensorConfig
import sd.read_config as rc
vbn=456
class BME280:
    '''BME280 Sensor Class'''
    def __init__(self, config: SensorConfig.SensorConfig):
        self.config = config
        print("constructor called of  class BME280 ")
        
m=BME280(vbn)     
  
# configs = rc.read_configs()
# keys = configs.keys()
# print("hello",keys)
# #m=BME280(configs[key])

		