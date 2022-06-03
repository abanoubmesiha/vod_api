def envelope(data, status = 200, message = "Successful Request"):
    return {
        'status': status,
        'message': message,
        'data': data
    }