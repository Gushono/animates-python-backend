from server import start_api
from server.configurations.enviroment_variables import HOST


def main():
    """
    Main function for server
    """
    app = start_api()
    app.run(host=HOST, port=8080, debug=False)


if __name__ == "__main__":
    main()
