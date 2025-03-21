import yaml

def load_config(filename='config.yaml'):

    try:
        with open(filename, 'r') as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        print("Error: config.yaml not found")
        return {}
    except yaml.YAMLError as e:
        print(f"Error parsing config.yaml: {e}")
        return {}
