import logging
import sys
import random

from PySide2.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QPushButton


class AdWindow(QDialog):
    """ This class represents ad window shown on the screen. """

    def __init__(self, ad_slogan, click_callback, parent=None):
        super(AdWindow, self).__init__(parent)
        self.setWindowTitle("Totally Unmissable Advertisement!")

        # Create a layout so that the ad slogan is shown.
        self.label = QLabel(ad_slogan)
        self.button = QPushButton("Claim Reward")
        self.button.clicked.connect(click_callback)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def closeEvent(self, event):
        # Ignore the close event so that the ad
        # can't be closed by pressing the close button.
        event.ignore()


class Adware(QApplication):
    """ This class represents implementation of adware. """

    def __init__(self, args):
        super(Adware, self).__init__(args)
        self.click_count = 0

    @property
    def advert_slogans(self):
        """ Slogans of the promoted ads with extra sarcasm. """
        return (
            'Because you clearly need more stuff you don\'t want!',
            'Buy now! Your life will totally change... or not.',
            'Don\'t miss out on this once-in-a-lifetime disappointment!',
        )

    def create_ad_window(self, ad_slogan):
        """ Creates a window showing the advertisement slogan.

        :param str ad_slogan: Text of the ad.
        """
        window = AdWindow(ad_slogan=ad_slogan, click_callback=self.handle_click)
        window.show()
        return window

    def show_ads(self):
        """ Creates the main GUI application and shows
        the ads based on `:class:~Adware.advert_slogans`
        """
        ad_windows = []
        for advert in self.advert_slogans:
            # Create a new ad window.
            ad_window = self.create_ad_window(advert)
            # Move this window to random location on screen.
            x_coordinate, y_coordinate = random.randint(1, 800), random.randint(1, 600)
            ad_window.move(x_coordinate, y_coordinate)
            ad_windows.append(ad_window)

        return ad_windows

    def handle_click(self):
        """ Handles the click on the ad button and teases the user. """
        self.click_count += 1
        reward_message = f"Wow, {self.click_count} clicks! You must REALLY want this totally fake reward!"
        logging.info(reward_message)

    def prompt_exit(self):
        """ Allows the user to exit if they know the magic phrase. """
        secret_phrase = input("If you want to escape, type the magic words (hint: let_me_out): ").strip()
        if secret_phrase == "let_me_out":
            print("Fine, you win this time. Closing adware...")
            sys.exit(0)
        else:
            print("Wrong! Looks like you're stuck with us. Enjoy the ads!")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # Create our adware and show the ads.
    adware = Adware(sys.argv)
    windows = adware.show_ads()

    while True:
        adware.prompt_exit()

    sys.exit(adware.exec_())
