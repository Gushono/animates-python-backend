from server import start_api

HOST = "127.0.0.1"


def main():
    """
    Main function for server
    """
    app = start_api()
    app.run(host=HOST, port=8080, debug=False)


if __name__ == "__main__":
    main()
