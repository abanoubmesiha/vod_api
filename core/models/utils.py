def try_to_serialize(model):
    try:
        return model.serialize()
    except:
        return None