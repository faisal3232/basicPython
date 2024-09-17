"""this module reads configurations from configuration file"""
import configparser
import sd.I2CSensorConfig as SensorConfig

config_dict = {}

def str2int(strVal):    
    intVal = int(strVal, 16) if 'x' in strVal or 'X' in strVal else int(strVal)
    return intVal

def read_configs():
    """Reads Application Configurations"""
    config_reader = configparser.ConfigParser()

    data = config_reader.read('./SensorDrivers/config.ini')

    print(data)
    sections = config_reader.sections()

    print(sections)
    for section in sections:
        print("section :", section)
        if(section == "GPS_SENSOR"):
            config = SPISensorConfig()
            config.is_enabled = True if config_reader[section]['Enabled'] == 'True' else False
            config.interface = config_reader[section]['Interface']
            config.spi_bus = str2int(config_reader[section]['SPIBusNo'])
            config.spi_Addr = str2int(config_reader[section]['SPIAddr'])
            config.spi_speed = str2int(config_reader[section]['spi_speed'])
            config.data_capture_interval = str2int(config_reader[section]['DataCapInterval'])
            config.is_data_raw_stream = True if config_reader[section]['DataRawStream'] == 'True' else False
            config.no_of_acc_samples = str2int(config_reader[section]['NoOfAccSamples'])
            config.is_data_avg_stream = True if config_reader[section]['DataAvgStream'] == 'True' else False
        else:
            config = SensorConfig.SensorConfig()
            config.is_enabled = True if config_reader[section]['Enabled'] == 'True' else False
            config.interface = config_reader[section]['Interface']
            config.i2c_bus = str2int(config_reader[section]['I2CBusNo'])
            config.i2c_addr = str2int(config_reader[section]['I2CAddr'])
            config.data_capture_interval = str2int(config_reader[section]['DataCapInterval'])
            config.is_data_raw_stream = True if config_reader[section]['DataRawStream'] == 'True' else False
            config.no_of_acc_samples = str2int(config_reader[section]['NoOfAccSamples'])
            config.is_data_avg_stream = True if config_reader[section]['DataAvgStream'] == 'True' else False
        
        config_dict[section] = config
    return config_dict
