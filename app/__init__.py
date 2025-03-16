'''
    This code sets up logging, loads environment variables, and configures the command handler.
'''
import os
import pkgutil
import importlib
import logging
import logging.config
import sys
from dotenv import load_dotenv
from app.commands import CommandHandler
from app.commands import Command

class App:
    '''Main application class'''

    def __init__(self):
        '''
        Constructor: Sets up logging, 
        loads environment variables, and configures the command handler.
        '''
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'TESTING')
        self.command_handler = CommandHandler()

    def configure_logging(self):
        '''Configure logging settings using a config file'''
        logging_conf_path = 'logging.conf'

        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s'
            )

        logging.info("Logging configured.")
        logging.warning("This is a warning message.")
        logging.error("This is an error message.")

    def load_environment_variables(self):
        '''Load environment variables into a dictionary'''
        settings = dict(os.environ.items())
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        '''go into a specific environment variable using this setting'''
        return self.settings.get(env_var)

    def load_plugins(self):
        '''load plugins directory'''
        plugins_package = 'app.plugins'

        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                self.register_plugin_commands(plugin_module, plugin_name)

    def register_plugin_commands(self, plugin_module, plugin_name):
        '''Register plugin commands to the command handler'''
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                logging.info("Command '%s' from plugin '%s' registered.", item_name, plugin_name)

    def start(self):
        '''This code start the application, initiate plugin loading, and start the REPL loop'''
        self.load_plugins()
        print("Type 'exit' to exit.")

        while True:  # REPL (Read, Evaluate, Print, Loop)
            user_input = input(">>> ").strip()
            if user_input.lower() == 'exit':
                break
            self.command_handler.execute_command(user_input)


if __name__ == "__main__":
    app = App()
    app.start()
