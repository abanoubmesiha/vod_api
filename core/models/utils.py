def try_to_serialize(model, options={}):
    try:
        return model.serialize(options)
    except:
        return None