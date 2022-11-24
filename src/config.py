from configobj import ConfigObj
from typing import Union
from dataclasses import dataclass

@dataclass(init=False)
class Config_data():
    POINT_SIZE: int
    SCREEN_WIDTH: int
    SCREEN_HEIGHT: int
    SCREEN_DIMS: tuple[int, int]
    
    SCREEN_SCALE: float
    SCREEN_SCALE_DIMS: tuple[int, int]
    
    BGCOLOR: tuple[int, int, int]


def init_cfg(default: bool = False) -> Config_data:
    config = ConfigObj("src/config.ini")

    assert len(config.keys()) == 2, f"Expected 2 config sections but loaded {len(config.keys)}"
    assert "DEFAULT" in config.keys(), "Cannot find 'DEFAULT' section in config."
    assert "DEFAULT" in config.keys(), "Cannot find 'USING' section in config."
    


    def load_config(return_type : list[str], keys: list[str], default: bool = False) -> any:
        assert len(keys) != 0, "Can't load config of nothing :D"

        def helper(tmp):
            for key in keys[1:]:
                tmp = tmp[key]
                
            if return_type[0] in ["tuple", "list"]:
                toReturn = []
                if return_type[1] == "int":
                    for item in tmp:
                        toReturn.append(int(item))
                elif return_type[1] == "float":
                    for item in tmp:
                        toReturn.append(float(item))
                else:
                    for item in tmp:
                        toReturn.append(item.lower() in ["y", "yes", "t", "true", "1"])
                
                if return_type[0] == "tuple":
                    return tuple(toReturn)
                return toReturn

            if return_type[0] == "int":
                return int(tmp)
            
            if return_type[0] == "float":
                return float(tmp)
            
            return item.lower() in ["y", "yes", "t", "true", "1"]
               

        if not default:
            try:
                tmp = helper(tmp=config["USING"][keys[0]])
                return tmp

            except IndexError:
                print("IndexError -> not enough type information.")
                print("This could be implemenation error. Exiting program.")
                exit(1)
            
            except KeyError:
                print(f"[WARN] Config specified by keys: {keys} not found. Using default value.")
            
            except ValueError:
                print(f"[WARN] Config specified by keys: {keys} is not correct,")
                print(f"[NOTE] Expexted type {return_type} but got key '{tmp}'.")
                print("[WARN] Using default config value")
        
        try:   
            tmp = helper(config["DEFAULT"][keys[0]])
            return tmp
        
        except IndexError:
            print("IndexError -> not enoughpy type information.")
            print("This could be implemenation error. Exiting program.")
            exit(1)
            
        except KeyError:
            print(f"[ERROR] Config specified by keys: {keys} not found even in DEFAULT config.")
            print("This could be implemenation error. Exiting program.")
            exit(1)
        
        except ValueError:
            print(f"[WARN] Config specified by keys: {keys} is not correct,")
            print(f"[NOTE] Expexted type {return_type} but got key '{tmp}'.")
            print("This could be implemenation error. Exiting program.")
            exit(1)


    def count_values(config: Union[dict, list]) -> int:
        if not isinstance(config, dict):
            return 1
        n = 0
        for key in config.keys():
            n += count_values(config[key])
        return n

    assert count_values(config["DEFAULT"]) == 5, "Unexpected config lenght."
    
    config_data = Config_data()
    
    config_data.POINT_SIZE:    int = load_config(["int"], ["point_size"],      default)
    config_data.SCREEN_WIDTH:  int = load_config(["int"], ["screen", "width"], default)
    config_data.SCREEN_HEIGHT: int = load_config(["int"], ["screen", "height"],default)
    config_data.SCREEN_DIMS = (config_data.SCREEN_WIDTH, config_data.SCREEN_HEIGHT)
    
    config_data.SCREEN_SCALE: float = load_config(["float"], ["screen", "scale"],  default)
    config_data.SCREEN_SCALE_DIMS = (
        int(config_data.SCREEN_WIDTH * config_data.SCREEN_SCALE), int(config_data.SCREEN_HEIGHT * config_data.SCREEN_SCALE))
    
    config_data.BGCOLOR: tuple = load_config(["tuple", "int"], ["background_color"],  default)
    
    
    
    return config_data
